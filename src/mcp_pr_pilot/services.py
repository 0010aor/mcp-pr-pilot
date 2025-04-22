import subprocess

from .diff_types import DiffType


def get_git_diff(diff_type: DiffType = DiffType.WORKING, branch: str = 'main', repo_path: str = '.') -> str:
    try:
        if diff_type == DiffType.WORKING:
            cmd = ['git', 'diff']
        elif diff_type == DiffType.BRANCH_COMPARE:
            cmd = ['git', 'diff', f'{branch}...']
        elif diff_type == DiffType.STAGED:
            cmd = ['git', 'diff', '--cached']
        elif diff_type == DiffType.COMMITTED:
            cmd = ['git', 'diff', f'{branch}..HEAD']
        result = subprocess.run(
            cmd,
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error running git diff: {e.stderr.strip()}'
