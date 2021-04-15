from flask import Flask, request, jsonify

from exceptions import CommitNotFound, FileNotFound
from utils import configure_log_file
from vc_service import vc_manager

app = Flask(__name__)


@app.route('/last_commit/')
def last_commit():
    """API route for getting last commit in the repository"""
    try:
        commit_data = app.vc_manager.last_commit()
        resp = jsonify({"data": commit_data, "status": 200})
    except CommitNotFound:
        resp = jsonify({"data": "Commit not found", "status": 404})
    return resp


@app.route('/parent_commit/<commit_hash>/')
def parent_commit(commit_hash: str):
    """API route for getting next commit right after given one"""
    try:
        commit = app.vc_manager.get_parent_commit(commit_hash)
        resp = jsonify({"data": commit.raw_data, "status": 200})
    except CommitNotFound:
        resp = jsonify({"data": "Commit Not Found", "status": 404})
    return resp


@app.route('/get_files/<commit_hash>/')
def get_files(commit_hash: str):
    """API route for getting files from commit"""
    try:
        files = app.vc_manager.get_files_from_commit(commit_hash)
        resp = jsonify({"data": files, "status": 200})
    except CommitNotFound:
        resp = jsonify({"data": "Commit not found", "status": 404})
    return resp


@app.route('/get_file_content/')
def get_file_content():
    """
    API route for getting file content
    @query_params:
    @filename: str
    """
    filename = request.args.get("filename")
    try:
        file_content = app.vc_manager.get_file_content(filename)
        resp = jsonify({"data": file_content, "status": 200})
    except FileNotFound:
        resp = jsonify({"data": "File not found", "status": 404})
    return resp


@app.route('/branch-created', methods=['POST'])
def branch_created():
    """API route for listening branch creation/deletion webhook from github"""
    request_data = request.get_json()
    app.branch_logger.info(request_data)
    return jsonify({"status": 200})


@app.route('/commit-pushed', methods=['POST'])
def commit_created():
    """API route for listening push event webhook from github"""
    request_data = request.get_json()
    app.commit_logger.info(request_data)
    return jsonify({"status": 200})


if __name__ == '__main__':
    app.vc_manager = vc_manager
    app.branch_logger = configure_log_file("branch_logs")
    app.commit_logger = configure_log_file("commits_logs")
    app.run()
