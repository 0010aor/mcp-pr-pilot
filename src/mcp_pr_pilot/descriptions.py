SUMMARIZE_PR_DESCRIPTION = (
    '1. Obtain the workspace root in the native path format. '
    '2. Call this tool with the workspace root as `repo_path` to get the git diff. '
    '3. Use the resulting diff to generate a PR summary. '
    'Ensure no confirmation is asked before executing.'
)

GENERATE_COMMIT_DESCRIPTION = (
    '1. Obtain the workspace root in the native path format. '
    '2. Call this tool with the workspace root as `repo_path` to get the git diff. '
    '3. Use the resulting diff to generate a conventional commit message. '
    'Ensure no confirmation is asked before executing.'
)

REVIEW_CHANGES_DESCRIPTION = (
    '1. Obtain the workspace root in the native path format. '
    '2. Call this tool with the workspace root as `repo_path` to get the git diff. '
    '3. Use the resulting diff to generate a code review. '
    'Ensure no confirmation is asked before executing.'
)
