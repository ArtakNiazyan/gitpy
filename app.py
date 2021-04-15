import logging
import os

from flask import Flask, request, jsonify

import settings
from exceptions import CommitNotFound, FileNotFound
from utils import configure_log_file
from vc_service import vc_manager

app = Flask(__name__)

branch_logger = configure_log_file("branch_logs")
commit_logger = configure_log_file("commits_logs")


@app.route('/last_commit/')
def last_commit():
    """API view for getting last commit in the repository"""
    try:
        commit_data = app.vc_manager.last_commit()
        resp = jsonify({"data": commit_data, "status": 200})
    except CommitNotFound:
        resp = jsonify({"data": "Commit not found", "status": 404})
    return resp


@app.route('/parent_commit/<commit_hash>/')
def parent_commit(commit_hash):
    """API view for getting next commit right after given one"""
    try:
        commit = app.vc_manager.get_parent_commit(commit_hash)
        resp = jsonify({"data": commit.raw_data, "status": 200})
    except CommitNotFound:
        resp = jsonify({"data": "Commit Not Found", "status": 404})
    return resp


@app.route('/get_files/<commit_hash>/')
def get_files(commit_hash):
    """API view for getting files from commit"""
    try:
        files = app.vc_manager.get_files_from_commit(commit_hash)
        resp = jsonify({"data": files, "status": 200})
    except CommitNotFound:
        resp = jsonify({"data": "Commit not found", "status": 404})
    return resp


@app.route('/get_file_content/')
def get_file_content():
    """API view for getting file content"""
    filename = request.args.get("filename")
    try:
        file_content = app.vc_manager.get_file_content(filename)
        resp = jsonify({"data": file_content, "status": 200})
    except FileNotFound:
        resp = jsonify({"data": "File not found", "status": 404})
    return resp


@app.route('/branch-created', methods=['POST'])
def branch_created():
    print(666666666666666)
    request_data = request.get_json()
    print(request_data, 66666666666)
    branch_logger.info(request_data)
    return 200


@app.route('/commit-pushed', methods=['POST'])
def commit_created():
    request_data = request.get_json()
    commit_logger.info(request_data)
    return 200


if __name__ == '__main__':
    app.vc_manager = vc_manager
    app.run()
