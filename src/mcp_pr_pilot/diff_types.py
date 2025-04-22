from enum import Enum


class DiffType(Enum):
    WORKING = 'working'
    BRANCH_COMPARE = 'branch_compare'
    STAGED = 'staged'
    COMMITTED = 'committed'
