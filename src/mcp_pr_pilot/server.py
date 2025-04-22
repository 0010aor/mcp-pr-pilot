from mcp import McpError
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import INTERNAL_ERROR, ErrorData, TextContent

from .tools import TOOL_HANDLERS, list_tools


async def serve() -> None:
    server = Server('mcp-server-pr-pilot')

    @server.list_tools()
    async def _list_tools() -> list:
        return list_tools()

    @server.call_tool()
    async def _call_tool(name, arguments: dict) -> list[TextContent]:
        handler = TOOL_HANDLERS.get(name)
        if handler is None:
            raise McpError(ErrorData(code=INTERNAL_ERROR, message=f'Unknown tool: {name}'))
        return handler(arguments)

    options = server.create_initialization_options()
    async with stdio_server() as (read_stream, write_stream):
        try:
            await server.run(read_stream, write_stream, options, raise_exceptions=True)
        except Exception:
            raise
