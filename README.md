# Chain Sentinel

Chain Sentinel is a multi-chain smart contract security scanner designed to help developers identify vulnerabilities across diverse blockchain ecosystems. It provides a unified command-line interface for scanning EVM, Move, Midnight Compact, and Rust-based smart contracts using fast, pattern-driven analysis.

## Features

- **Multi-chain support** — Scan EVM (`.sol`), Move (`.move`), Midnight Compact (`.compact`), and Rust smart contracts.
- **Pattern-based vulnerability detection** — Lightweight, fast scanning using customizable rule patterns.
- **Unified CLI tool** — Run scans from any directory with a single command.
- **JSON output mode** — Integrate results into CI pipelines, dashboards, or automated tooling.
- **Zero external dependencies** — Pure Python; no blockchain node required.

## Installation

Install Chain Sentinel from PyPI:

```bash
pip install chain-sentinel

Usage

Basic scan

chain-sentinel .

JSON output

chain-sentinel . --json

Example output

=== ./contracts/Payment.compact ===
[HIGH] [economic] Division detected; verify non-zero divisor and rounding. (line 50)

=== Summary ===
Total findings: 1
By severity:
  HIGH: 1
By category:
  economic: 1
By directory:
  ./contracts: 1

Expected Project Structure

Chain Sentinel automatically scans supported file types inside your project:

project/
├── contracts/
│   ├── MyContract.sol
│   ├── Token.move
│   ├── AccessControl.compact
│   └── verifier.rs
└── ...

Supported Chains & Languages

Chain / Platform

File Type

Analyzer

Ethereum / EVM

.sol

Solidity pattern scanner

Move (Aptos/Sui)

.move

Move pattern scanner

Midnight

.compact

Compact analyzer

Rust-based blockchains

.rs

Rust pattern scanner

Extending Chain Sentinel

Chain Sentinel is designed to be modular. You can:

Add new pattern rules

Extend analyzers

Add new chain support

Build custom CI integrations

Contributing

Contributions are welcome! Submit issues or pull requests on GitHub:

https://github.com/Web3-AI-DIA/chain-sentinel

License

Chain Sentinel is licensed under the MIT License.


