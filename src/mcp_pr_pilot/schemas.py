from pydantic import BaseModel


class GitDiffSummaryParams(BaseModel):
    """Parameters for git diff summary."""

    branch: str = 'main'


class GitDiffSummaryResult(BaseModel):
    diff: str
    instruction: str
