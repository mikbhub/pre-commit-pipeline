import pytest

from ..jira_id_check import commit_msg_hook

MOCK_PATH = ".hooks/jira_id/test/mock"


def test_jira_id_in_commit_msg():
    r_val = commit_msg_hook(f"{MOCK_PATH}/commit-msg-with-jira-id.txt")
    success = r_val is None
    assert success


def test_jira_id_missing():
    with pytest.raises(SystemExit) as e:
        commit_msg_hook(f"{MOCK_PATH}/commit-msg-missing-jira-id.txt")
    assert e.type == SystemExit
    assert e.value.code != 0
