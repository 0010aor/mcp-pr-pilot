from pydantic import BaseModel


class GitDiffSummaryParams(BaseModel):
    """No parameters needed for git diff summary."""

    pass


class GitDiffSummaryResult(BaseModel):
    diff: str
    instruction: str
