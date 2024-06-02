import subprocess
import os


def batch_commit(repo_path, commit_message):
    """
    Batch commit changes in the given repository path with the provided commit message.

    :param repo_path: Path to the repository
    :param commit_message: Commit message for the changes
    """
    # Change the current working directory to the repository path
    os.chdir(repo_path)

    # Stage all changes
    subprocess.run(["git", "add", "."], check=True)

    # Commit the changes
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Push the changes to the remote repository
    subprocess.run(["git", "push"], check=True)


if __name__ == "__main__":
    # Example usage    # Replace with the path to your repository
    repo_path = "D:/Projects/useful-scripts"
    commit_message = "Batch commit changes"  # Replace with your commit message

    batch_commit(repo_path, commit_message)