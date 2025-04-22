from mcp import McpError
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    INTERNAL_ERROR,
    ErrorData,
    TextContent,
    Tool,
)

from .descriptions import GENERATE_COMMIT_DESCRIPTION, REVIEW_CHANGES_DESCRIPTION, SUMMARIZE_PR_DESCRIPTION
from .instructions import GENERATE_COMMIT_INSTRUCTION, REVIEW_CHANGES_INSTRUCTION, SUMMARIZE_PR_INSTRUCTION
from .schemas import GitDiffCommitResult, GitDiffReviewResult, GitDiffSummaryParams, GitDiffSummaryResult
from .services import get_git_diff


async def serve() -> None:
    server = Server('mcp-server-pr-pilot')

    @server.list_tools()
    async def list_tools() -> list[Tool]:
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
        ]

    @server.call_tool()
    async def call_tool(name, arguments: dict) -> list[TextContent]:
        diff_type = arguments.get('diff_type')
        if name == 'summarize_pr':
            branch = arguments.get('branch', 'main')
            repo_path = arguments.get('repo_path')
            diff = get_git_diff(branch, repo_path, diff_type=diff_type or 'working')
            instruction = SUMMARIZE_PR_INSTRUCTION
            result = GitDiffSummaryResult(diff=diff, instruction=instruction)
            return [TextContent(type='text', text=result.model_dump_json())]
        elif name == 'generate_commit':
            branch = arguments.get('branch', 'main')
            repo_path = arguments.get('repo_path')
            diff = get_git_diff(branch, repo_path, diff_type=diff_type or 'staged')
            instruction = GENERATE_COMMIT_INSTRUCTION
            result = GitDiffCommitResult(diff=diff, instruction=instruction)
            return [TextContent(type='text', text=result.model_dump_json())]
        elif name == 'review_changes':
            branch = arguments.get('branch', 'main')
            repo_path = arguments.get('repo_path')
            diff = get_git_diff(branch, repo_path, diff_type=diff_type or 'working')
            instruction = REVIEW_CHANGES_INSTRUCTION
            result = GitDiffReviewResult(diff=diff, instruction=instruction)
            return [TextContent(type='text', text=result.model_dump_json())]
        else:
            raise McpError(ErrorData(code=INTERNAL_ERROR, message=f'Unknown tool: {name}'))

    options = server.create_initialization_options()
    async with stdio_server() as (read_stream, write_stream):
        try:
            await server.run(read_stream, write_stream, options, raise_exceptions=True)
        except Exception:
            raise
