import re
import sys

JIRA_ID_REGEX = re.compile(r"[A-Z]+-\d+")

MISSING_JIRA_ID_MSG = """
Commit message is missing [JIRA task id].

Include [JIRA task id] in commit message, like so:
#################################
ABC-123 this is my commit message
#################################
where ABC-123 is a sample [JIRA task id].

For more details check:
https://confluence.atlassian.com/adminjiracloud/integrating-with-development-tools-776636216.html
"""


def jira_id_in_commit_msg(commit_msg: str) -> bool:
    return bool(re.search(JIRA_ID_REGEX, commit_msg))


def commit_msg_hook(commit_msg_filepath: str) -> None:
    """Scans for valid jira task id in commit message

    https://pre-commit.com/#pre-commit-for-commit-messages"""

    with open(commit_msg_filepath) as commit_msg:
        if not jira_id_in_commit_msg(commit_msg.read()):
            sys.exit(MISSING_JIRA_ID_MSG)


if __name__ == "__main__":
    commit_msg_hook(sys.argv[1])
