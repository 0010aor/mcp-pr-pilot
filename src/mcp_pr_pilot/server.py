from mcp import McpError
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    INTERNAL_ERROR,
    ErrorData,
    TextContent,
    Tool,
)

from .schemas import GitDiffSummaryParams, GitDiffSummaryResult
from .services import get_git_diff


async def serve() -> None:
    """Run the MCP server for git diff summarization."""
    server = Server('mcp-server-git-diff')

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name='get_pr_description',
                description='Returns the git diff (main...) and a suggested instruction to summarize the changes for a PR description.',
                inputSchema=GitDiffSummaryParams.model_json_schema(),
            ),
        ]

    @server.call_tool()
    async def call_tool(name, arguments: dict) -> list[TextContent]:
        if name == 'get_pr_description':
            branch = arguments.get('branch', 'main')
            diff = get_git_diff(branch)
            instruction = 'Summarize these changes in natural language for a pull request description.'
            result = GitDiffSummaryResult(diff=diff, instruction=instruction)
            return [TextContent(type='text', text=result.model_dump_json())]
        else:
            raise McpError(ErrorData(code=INTERNAL_ERROR, message=f'Unknown tool: {name}'))

    options = server.create_initialization_options()
    async with stdio_server() as (read_stream, write_stream):
        try:
            await server.run(read_stream, write_stream, options, raise_exceptions=True)
        except Exception:
            raise
