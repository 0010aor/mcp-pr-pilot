import subprocess


def get_git_diff() -> str:
    """Runs 'git diff main...' and returns the output as a string."""
    try:
        result = subprocess.run(
            ['git', 'diff', 'main...'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error running git diff: {e.stderr.strip()}'
