#!/usr/bin/env python3
import argparse
import sys
from sentinel.core.loader import load_targets
from sentinel.core.reporter import Reporter
from sentinel.evm.analyzer import analyze_evm_file
from sentinel.move.analyzer import analyze_move_file
from sentinel.midnight.compact_analyzer import analyze_compact_file
from sentinel.midnight.dapp_analyzer import analyze_midnight_dapp_file
from sentinel.rust.analyzer import analyze_rust_file

def main():
    parser = argparse.ArgumentParser(
        prog="chain-sentinel",
        description="Multi-chain smart contract security scanner (EVM, Move, Midnight, Rust)."
    )
    parser.add_argument("target", help="File or directory to scan")
    parser.add_argument(
        "--evm", action="store_true",
        help="Force EVM mode (Solidity/EVM contracts)"
    )
    parser.add_argument(
        "--move", action="store_true",
        help="Force Move mode (Aptos/Sui modules)"
    )
    parser.add_argument(
        "--midnight", action="store_true",
        help="Force Midnight mode (Compact + Midnight dApps)"
    )
    parser.add_argument(
        "--rust", action="store_true",
        help="Force Rust mode (Rust-based smart contracts)"
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Output JSON instead of human-readable text"
    )
    args = parser.parse_args()

    targets = load_targets(args.target)
    if not targets:
        print(f"[ERROR] No valid targets found for: {args.target}")
        sys.exit(1)

    reporter = Reporter(json_output=args.json)

    for path in targets:
        if args.evm or path.endswith(".sol"):
            analyze_evm_file(path, reporter)
        elif args.move or path.endswith(".move"):
            analyze_move_file(path, reporter)
        elif args.midnight or path.endswith(".compact") or path.endswith(".midnight.json"):
            if path.endswith(".compact"):
                analyze_compact_file(path, reporter)
            else:
                analyze_midnight_dapp_file(path, reporter)
        elif args.rust or path.endswith(".rs"):
            analyze_rust_file(path, reporter)
        else:
            reporter.add(
                severity="LOW",
                category="general",
                message=f"Unknown file type, skipping: {path}",
                file_path=path,
                line=None
            )

    reporter.flush()

if __name__ == "__main__":
    main()
