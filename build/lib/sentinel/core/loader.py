import os
from typing import List

SUPPORTED_EXTENSIONS = (
    ".sol",        # EVM / Solidity
    ".move",       # Move
    ".compact",    # Compact smart contracts (Midnight)
    ".rs",         # Rust smart contracts
    ".midnight.json",  # Midnight dApp manifest
)

def load_targets(target: str) -> List[str]:
    """
    Given a file or directory path, return a list of files to scan.
    Supports EVM (.sol), Move (.move), Compact (.compact),
    Rust (.rs), and Midnight dApp manifests (.midnight.json).
    """
    if os.path.isfile(target):
        return [target]

    if os.path.isdir(target):
        files = []
        for root, _, filenames in os.walk(target):
            for name in filenames:
                for ext in SUPPORTED_EXTENSIONS:
                    if name.endswith(ext):
                        files.append(os.path.join(root, name))
                        break
        return files

    return []
