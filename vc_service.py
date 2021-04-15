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
    def get_parent_commit(self, commit_hash: str):
        """
        Class method returns paren commit of given commit
        @param commit_hash: str
        """
        return NotImplemented

    @abstractmethod
    def get_files_from_commit(self, commit_hash: str):
        """
        Class method returns changed files in given commit
        @param commit_hash: str
        """
        return NotImplemented

    @abstractmethod
    def get_file_content(self, filename: str):
        """
        Class method returns content of given file
        @param filename: str
        """
        return NotImplemented


class GitHubManager(AbstractBaseVCManager):
    def __init__(self):
        self.githubapi = Github(os.environ.get("GITHUB_TOKEN"))
        self.repository = self.get_repository()

    def _get_commit(self, commit_hash):
        """Internal method for getting commit object"""
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
        parent = commit.parents[0]
        return parent

    def get_files_from_commit(self, commit_hash):
        commit = self._get_commit(commit_hash)
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
    vc = os.environ.get("VC_SYSTEM", "git")
    if vc.lower() == "git":
        return GitHubManager()
    else:
        raise NotImplementedError


vc_manager = get_vc_manager()
