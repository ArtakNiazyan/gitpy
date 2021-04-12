import requests
import json
from abc import ABC, abstractmethod

from github import Github
from github.GithubException import GithubException

from settings import GITHUB_TOKEN, REPOSITORY_URL


class AbstractVCManager(ABC):

    @abstractmethod
    def last_commit(self):
        return NotImplemented

    @abstractmethod
    def get_repository(self):
        return NotImplemented

    @abstractmethod
    def get_commit(self, commit_hash):
        return NotImplemented

    @abstractmethod
    def get_next_commit(self, commit_hash):
        return NotImplemented

    @abstractmethod
    def get_files_from_commit(self, commit_hash):
        return NotImplemented

    @abstractmethod
    def get_file_content(self, filename):
        return NotImplemented

    @abstractmethod
    def revert_commit(self, commit_hash):
        return NotImplemented

    @abstractmethod
    def commit_changes(self):
        return NotImplemented


class GitHubManager(AbstractVCManager):
    def __init__(self):
        self.githubapi = Github(GITHUB_TOKEN)
        self.repository = self.get_repository()

    def get_commit(self, commit_hash):
        try:
            commit = self.repository.get_commit(commit_hash)
            return commit
        except GithubException:
            return None

    def last_commit(self):
        repository = self.repository
        commits = repository.get_commits()
        if commits.totalCount > 0:
            return commits[0]
        # while since >= repository.created_at:
        #     if commits.totalCount > 0:
        #         return commits[0]
        #     since = since - datetime.timedelta(days=1)

    def get_next_commit(self, commit_hash):
        commit = self.get_commit(commit_hash)
        if commit:
            next_commit = commit.parents[0]
            return next_commit

    def get_files_from_commit(self, commit_hash):
        commit = self.get_commit(commit_hash)
        if commit:
            files_arr = list()
            for file in commit.files:
                files_arr.append(file.raw_data)
            return files_arr

    def get_file_content(self, filename):
        file_content = self.repository.get_contents("app.py")
        print(file_content.decoded_content.decode())
        return file_content.decoded_content.decode()

    def get_repository(self):
        return self.githubapi.get_repo(REPOSITORY_URL)

    def revert_commit(self, commit_hash):
        pass

    def commit_changes(self):
        pass
