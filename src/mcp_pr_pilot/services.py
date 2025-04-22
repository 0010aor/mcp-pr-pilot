import subprocess


def get_git_diff(branch: str = 'main', repo_path: str = '.', diff_type: str = 'working') -> str:
    try:
        if diff_type == 'working':
            cmd = ['git', 'diff', f'{branch}...']
        elif diff_type == 'staged':
            cmd = ['git', 'diff', '--cached']
        elif diff_type == 'committed':
            cmd = ['git', 'diff', f'{branch}..HEAD']
        else:
            return f'Unknown diff_type: {diff_type}'
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
