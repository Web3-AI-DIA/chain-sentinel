#!/usr/bin/env python3
import argparse
import sys
from sentinel.core.loader import load_targets
from sentinel.core.reporter import Reporter
from sentinel.evm.analyzer import analyze_evm_file
from sentinel.move.analyzer import analyze_move_file

def main():
    parser = argparse.ArgumentParser(
        prog="chain-sentinel",
        description="Multi-chain smart contract security scanner (EVM + Move)."
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
