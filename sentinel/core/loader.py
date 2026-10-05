import os
from typing import List

def load_targets(target: str) -> List[str]:
    """
    Given a file or directory path, return a list of files to scan.
    Supports .sol (EVM) and .move (Move) files.
    """
    if os.path.isfile(target):
        return [target]

    if os.path.isdir(target):
        files = []
        for root, _, filenames in os.walk(target):
            for name in filenames:
                if name.endswith(".sol") or name.endswith(".move"):
                    files.append(os.path.join(root, name))
        return files

    return []
