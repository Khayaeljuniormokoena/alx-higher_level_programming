#!/usr/bin/python3

import requests
import sys

def fetch_commits(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    return response.json()

def print_commits(commits):
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

def main():
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    commits = fetch_commits(owner_name, repo_name)

    if 'message' in commits and commits['message'] == 'Not Found':
        print(f"Repository '{repo_name}' not found for owner '{owner_name}'")
        sys.exit(1)

    print_commits(commits)

if __name__ == "__main__":
    main()
