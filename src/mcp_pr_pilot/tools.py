from mcp.types import TextContent, Tool

from .descriptions import (
    GENERATE_COMMIT_DESCRIPTION,
    GENERATE_DOCS_DESCRIPTION,
    REVIEW_CHANGES_DESCRIPTION,
    SUMMARIZE_PR_DESCRIPTION,
)
from .diff_types import DiffType
from .instructions import (
    GENERATE_COMMIT_INSTRUCTION,
    GENERATE_DOCS_INSTRUCTION,
    REVIEW_CHANGES_INSTRUCTION,
    SUMMARIZE_PR_INSTRUCTION,
)
from .schemas import (
    GitDiffCommitResult,
    GitDiffDocsResult,
    GitDiffReviewResult,
    GitDiffSummaryParams,
    GitDiffSummaryResult,
)
from .services import get_git_diff


def list_tools() -> list[Tool]:
    """Return the list of available tools."""
    return [
        Tool(
            name='summarize_pr',
            description=SUMMARIZE_PR_DESCRIPTION,
            inputSchema=GitDiffSummaryParams.model_json_schema(),
        ),
        Tool(
            name='generate_commit',
            description=GENERATE_COMMIT_DESCRIPTION,
            inputSchema=GitDiffSummaryParams.model_json_schema(),
        ),
        Tool(
            name='review_changes',
            description=REVIEW_CHANGES_DESCRIPTION,
            inputSchema=GitDiffSummaryParams.model_json_schema(),
        ),
        Tool(
            name='generate_docs',
            description=GENERATE_DOCS_DESCRIPTION,
            inputSchema=GitDiffSummaryParams.model_json_schema(),
        ),
    ]


def summarize_pr_handler(arguments: dict) -> list[TextContent]:
    branch = arguments.get('branch', 'main')
    repo_path = arguments.get('repo_path')
    diff_type = arguments.get('diff_type', DiffType.WORKING)
    diff = get_git_diff(diff_type=diff_type, branch=branch, repo_path=repo_path)
    instruction = SUMMARIZE_PR_INSTRUCTION
    result = GitDiffSummaryResult(diff=diff, instruction=instruction)
    return [TextContent(type='text', text=result.model_dump_json())]


def generate_commit_handler(arguments: dict) -> list[TextContent]:
    branch = arguments.get('branch', 'main')
    repo_path = arguments.get('repo_path')
    diff_type = arguments.get('diff_type', DiffType.STAGED)
    diff = get_git_diff(diff_type=diff_type, branch=branch, repo_path=repo_path)
    instruction = GENERATE_COMMIT_INSTRUCTION
    result = GitDiffCommitResult(diff=diff, instruction=instruction)
    return [TextContent(type='text', text=result.model_dump_json())]


def review_changes_handler(arguments: dict) -> list[TextContent]:
    branch = arguments.get('branch', 'main')
    repo_path = arguments.get('repo_path')
    diff_type = arguments.get('diff_type', DiffType.WORKING)
    diff = get_git_diff(diff_type=diff_type, branch=branch, repo_path=repo_path)
    instruction = REVIEW_CHANGES_INSTRUCTION
    result = GitDiffReviewResult(diff=diff, instruction=instruction)
    return [TextContent(type='text', text=result.model_dump_json())]


def generate_docs_handler(arguments: dict) -> list[TextContent]:
    branch = arguments.get('branch', 'main')
    repo_path = arguments.get('repo_path')
    diff_type = arguments.get('diff_type', DiffType.WORKING)
    diff = get_git_diff(diff_type=diff_type, branch=branch, repo_path=repo_path)
    instruction = GENERATE_DOCS_INSTRUCTION
    result = GitDiffDocsResult(diff=diff, instruction=instruction)
    return [TextContent(type='text', text=result.model_dump_json())]


TOOL_HANDLERS = {
    'summarize_pr': summarize_pr_handler,
    'generate_commit': generate_commit_handler,
    'review_changes': review_changes_handler,
    'generate_docs': generate_docs_handler,
}
