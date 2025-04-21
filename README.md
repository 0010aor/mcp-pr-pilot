# MCP Server PR Pilot

A Model Context Protocol (MCP) server that helps you create pull request (PR) descriptions based on the actual code changes in your repository. It provides the output of `git diff main...` and a summarization instruction, making it easy to generate meaningful PR descriptions using LLMs or other tools.

### Available Tools

-   `get_pr_description` - Returns the git diff (`<branch>...`, default: `main`) and a suggested instruction to summarize the changes for a PR description.
    -   **Input:** Optional `branch` parameter (defaults to `main`).
    -   **Output:** JSON with two fields:
        -   `diff`: The raw output of `git diff <branch>...`
        -   `instruction`: A string instructing to "Summarize these changes in natural language for a pull request description."

## Installation and Running

This project uses [`uv`](https://docs.astral.sh/uv/) for dependency management and running scripts.

### Using uv (recommended)

Ensure `uv` is installed. You can run the server directly from the project directory:

```bash
# Navigate to the project root directory first
cd path/to/mcp-servers/mcp-pr-pilot

# Install dependencies (if needed) and run the server script
uv run mcp-server-pr-pilot
```

## Configuration

Add an entry to your client's MCP server configuration. The exact key can be chosen by you.

```json
"mcpServers": {
  "pr-pilot": {
    "command": "uv",
    "args": [
      "--directory",
      "/path/to/mcp-servers/mcp-pr-pilot",
      "run",
      "mcp-server-pr-pilot"
    ]
  }
}
```

## License

mcp-server-pr-pilot is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License.