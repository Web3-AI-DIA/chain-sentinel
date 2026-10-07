import argparse
from sentinel.core.loader import run_scan

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        prog="chain-sentinel",
        description="Multi-chain smart contract security scanner (EVM, Move, Midnight, Rust).",
    )

    parser.add_argument("target", help="File or directory to scan")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of text")
    parser.add_argument("--evm", action="store_true", help="Force EVM mode")
    parser.add_argument("--move", action="store_true", help="Force Move mode")
    parser.add_argument("--midnight", action="store_true", help="Force Midnight mode")
    parser.add_argument("--rust", action="store_true", help="Force Rust mode")

    return parser.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)
    run_scan(
        path=args.target,
        json_output=args.json,
        evm=args.evm,
        move=args.move,
        midnight=args.midnight,
        rust=args.rust,
    )

if __name__ == "__main__":
    main()
