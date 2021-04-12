from flask import Flask
from flask import jsonify

from vc_service import GitHubManager

app = Flask(__name__)


@app.route('/last_commit')
def last_commit():
    github = GitHubManager()
    commit = github.last_commit()
    return jsonify(commit.raw_data)


@app.route('/next_commit/<commit_hash>/')
def next_commit(commit_hash):
    github = GitHubManager()
    commit = github.get_next_commit(commit_hash)
    return jsonify(commit.raw_data)

@app.route('/get_files/<commit_hash>/')
def get_files(commit_hash):
    github = GitHubManager()
    files = github.get_files_from_commit(commit_hash)
    return jsonify(files)


if __name__ == '__main__':
    app.run()
