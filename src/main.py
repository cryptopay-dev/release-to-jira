import os
from pprint import pprint

from jira_api import add_release_to_issue, get_or_create_release
from notes_parser import extract_changes, extract_issue_ids

release_name = f"{os.environ['GITHUB_REPO_NAME']}-{os.environ['GITHUB_REF_NAME']}"
release = get_or_create_release(release_name)
print("JIRA Release:")
pprint(release)

changes = extract_changes()
print("Release Issues:")
pprint(changes)

for change in changes:
    for issue_id in extract_issue_ids(change["title"]):
        print("Updating", issue_id)
        add_release_to_issue(release_name, issue_id)
