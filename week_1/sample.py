"""
A very basic example of using PyGithub to fetch and print the README.md content of a GitHub repository.
Make sure to set the GITHUB_TOKEN environment variable with your personal access token before running this script.
Make sure you handle the exceptions properly as they are important for a production environment.
"""
from github import Github
import os

def fetch_readme(repo_name: str) -> None:
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN environment variable not set")

    github = Github(token)

    try:
        repo = github.get_repo(repo_name)
        readme = repo.get_readme()
        content = readme.decoded_content.decode("utf-8")

        print("\n===== README.md CONTENT =====\n")
        print(content)

    except Exception as e:
        print(f"Error fetching README.md: {e}")

if __name__ == "__main__":
    repository = input("Enter repository (owner/repo): ")
    fetch_readme(repository)
