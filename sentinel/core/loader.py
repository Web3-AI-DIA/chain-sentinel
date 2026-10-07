import os
from typing import List

SUPPORTED_EXTENSIONS = (
    ".sol",            # EVM / Solidity
    ".move",           # Move
    ".compact",        # Midnight Compact smart contracts
    ".rs",             # Rust smart contracts
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


# -----------------------------
# CORE SCANNING ORCHESTRATOR
# -----------------------------

from sentinel.core.reporter import Reporter

# Correct imports based on your actual analyzer files
from sentinel.evm.analyzer import analyze_evm_file
from sentinel.move.analyzer import analyze_move_file
from sentinel.midnight.compact_analyzer import analyze_compact_file
from sentinel.midnight.dapp_analyzer import analyze_midnight_dapp_file
from sentinel.rust.analyzer import analyze_rust_file

def run_scan(
    path: str,
    json_output: bool = False,
    evm: bool = False,
    move: bool = False,
    midnight: bool = False,
    rust: bool = False,
):
    """
    Core scanning orchestrator.
    Loads targets, selects analyzers, runs analysis, and prints results.
    """

    reporter = Reporter(json_output=json_output)
    targets = load_targets(path)

    if not targets:
        print(f"[ERROR] No valid targets found for: {path}")
        return

    for file_path in targets:
        # EVM / Solidity
        if file_path.endswith(".sol") and (evm or not any([move, midnight, rust])):
            analyze_evm_file(file_path, reporter)

        # Move
        elif file_path.endswith(".move") and (move or not any([evm, midnight, rust])):
            analyze_move_file(file_path, reporter)

        # Midnight Compact
        elif file_path.endswith(".compact") and (midnight or not any([evm, move, rust])):
            analyze_compact_file(file_path, reporter)

        # Midnight dApp manifest
        elif file_path.endswith(".midnight.json") and (midnight or not any([evm, move, rust])):
            analyze_midnight_dapp_file(file_path, reporter)

        # Rust smart contracts
        elif file_path.endswith(".rs") and (rust or not any([evm, move, midnight])):
            analyze_rust_file(file_path, reporter)

    reporter.flush()
