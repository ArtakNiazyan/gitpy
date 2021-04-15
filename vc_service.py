import os
from abc import ABC, abstractmethod

from github import Github
from github.GithubException import GithubException, UnknownObjectException

from exceptions import CommitNotFound, FileNotFound
from settings import REPOSITORY_URL


class AbstractBaseVCManager(ABC):
    """Abstract Base class for Version Control Manager app"""
    @abstractmethod
    def get_repository(self):
        return NotImplemented

    @abstractmethod
    def last_commit(self):
        """Class method returns last commit on repository"""
        return NotImplemented

    @abstractmethod
    def get_parent_commit(self, commit_hash):
        """Class method returns paren commit of given commit"""
        return NotImplemented

    @abstractmethod
    def get_files_from_commit(self, commit_hash):
        """Class method returns changed files in given commit"""
        return NotImplemented

    @abstractmethod
    def get_file_content(self, filename):
        """Class method returns content of given file"""
        return NotImplemented


class GitHubManager(AbstractBaseVCManager):
    def __init__(self):
        self.githubapi = Github(os.environ.get("GITHUB_TOKEN"))
        self.repository = self.get_repository()

    def _get_commit(self, commit_hash):
        try:
            commit = self.repository.get_commit(commit_hash)
            return commit
        except GithubException:
            raise CommitNotFound

    def get_repository(self):
        return self.githubapi.get_repo(REPOSITORY_URL)

    def last_commit(self):
        commits = self.repository.get_commits()
        if commits.totalCount > 0:
            return commits[0].raw_data, 200
        return None, 404

    def get_parent_commit(self, commit_hash):
        commit = self._get_commit(commit_hash)
        if commit:
            next_commit = commit.parents[0]
            return next_commit.raw_data, 200

    def get_files_from_commit(self, commit_hash):
        commit = self._get_commit(commit_hash)
        if commit:
            files_arr = list()
            for file in commit.files:
                files_arr.append(file.raw_data)
            return files_arr

    def get_file_content(self, filename):
        try:
            file_content = self.repository.get_contents(filename)
        except UnknownObjectException:
            raise FileNotFound
        return file_content.decoded_content.decode()


def get_vc_manager():
    vc = os.environ.get("VC_MANAGER", "github")
    if vc.lower() == "github":
        return GitHubManager()
    else:
        raise NotImplementedError


vc_manager = get_vc_manager()
