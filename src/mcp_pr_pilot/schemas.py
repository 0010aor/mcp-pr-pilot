from pydantic import BaseModel


class GitDiffSummaryParams(BaseModel):
    """Parameters for git diff summary."""

    branch: str = 'main'
    repo_path: str


class GitDiffSummaryResult(BaseModel):
    diff: str
    instruction: str


class GitDiffCommitResult(BaseModel):
    diff: str
    instruction: str


class GitDiffReviewResult(BaseModel):
    diff: str
    instruction: str


class GitDiffDocsResult(BaseModel):
    diff: str
    instruction: str
