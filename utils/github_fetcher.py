import requests
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

class GitHubFetcher:
    def __init__(self, token=GITHUB_TOKEN):
        self.headers = {"Authorization": f"token {token}"} if token else {}

    def fetch_repo_contents(self, repo_url, path=""):
        """
        Fetches contents of a GitHub repository.
        Expected format: user/repo
        """
        api_url = f"https://api.github.com/repos/{repo_url}/contents/{path}"
        response = requests.get(api_url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return {"error": response.json()}

    def get_file_content(self, download_url):
        """Fetches raw content of a file from GitHub."""
        response = requests.get(download_url, headers=self.headers)
        return response.text
