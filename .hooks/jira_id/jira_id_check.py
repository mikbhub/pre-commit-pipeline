import re
import sys

JIRA_ID_REGEX = re.compile(r"[A-Z]+-\d+")

MISSING_JIRA_ID_MSG = """
JIRA task ID not found.
Include JIRA task id in commit message, like so:

ABC-123 this is my commit message

where ABC-123 is a sample JIRA task id.
"""


def search_for_jira_id(commit_msg: str) -> bool:
    return bool(re.search(JIRA_ID_REGEX, commit_msg))


def commit_msg_hook(commit_msg_filepath: str):
    """Scans for valid jira task id in commit message

    https://pre-commit.com/#pre-commit-for-commit-messages"""

    with open(commit_msg_filepath) as commit_msg:
        if not search_for_jira_id(commit_msg.read()):
            print(MISSING_JIRA_ID_MSG)
            sys.exit(1)


if __name__ == "__main__":
    commit_msg_hook(sys.argv[1])
