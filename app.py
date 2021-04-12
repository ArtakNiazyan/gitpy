from flask import Flask
from flask import jsonify

from vc_service import GitHubManager

app = Flask(__name__)


@app.route('/last_commit')
def last_commit():
    github = GitHubManager()
    commit = github.last_commit()
    if commit:
        return jsonify(commit.raw_data)
    return jsonify({"message": "Commit not found", "status": 404})


@app.route('/next_commit/<commit_hash>/')
def next_commit(commit_hash):
    github = GitHubManager()
    commit = github.get_next_commit(commit_hash)
    if commit:
        return jsonify(commit.raw_data)
    return jsonify({"message": "Commit not found", "status": 404})


@app.route('/get_files/<commit_hash>/')
def get_files(commit_hash):
    github = GitHubManager()
    files = github.get_files_from_commit(commit_hash)
    if files:
        return jsonify(files)
    return jsonify({"message": "Commit not found", "status": 404})

@app.route('/get_file_content/<filename>/')
def get_file_content(filename):
    github = GitHubManager()
    file_content = github.get_file_content(filename)
    return jsonify({"content": file_content, "status": 200})


if __name__ == '__main__':
    app.run()
