# 🛡️ chain‑sentinel
### Multi‑Chain Smart Contract Security Scanner
### EVM • Move • Midnight (Compact + dApps) • Rust

chain‑sentinel is a Termux‑friendly, Python‑powered, multi‑chain security scanner designed for blockchain developers, auditors, and researchers.  
It performs static analysis across multiple smart contract languages and dApp formats, detecting risky patterns, unsafe constructs, and misconfigurations.

Built for mobile auditing.  
Built for multi‑chain ecosystems.  
Built for speed.

---

## ⚡ Features

- **EVM / Solidity scanning**  
  Detects reentrancy risks, unsafe low‑level calls, auth issues, economic flaws, upgradeability hazards, and more.

- **Move scanning (Aptos / Sui)**  
  Flags unsafe entry functions, resource misuse, unchecked arithmetic, capability issues, and invariant risks.

- **Midnight Network scanning**  
  - **Compact smart contracts**  
    Detects capability misuse, resource duplication, unsafe transitions, missing `requires`, and more.  
  - **Midnight dApps**  
    Scans `.midnight.json` manifests, agent configs, zk suite definitions, and privy rules.

- **Rust smart contract scanning**  
  Supports Solana, CosmWasm, NEAR, and Substrate patterns including unsafe blocks, unchecked arithmetic, CPI calls, account validation issues, and deserialization risks.

- **Directory scanning**  
  Recursively scans entire project folders.

- **JSON output**  
  Machine‑readable reports for CI pipelines and automated tooling.

- **Zero external dependencies**  
  Lightweight, fast, and portable.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Web3-AI-DIA/chain-sentinel.git
cd chain-sentinel

Install inside any Python environment (Termux, Linux, macOS, WSL):

pip install .

This installs the chain-sentinel CLI globally inside your active environment.

🚀 Usage

Scan a single file

chain-sentinel path/to/Contract.sol

Scan a directory

chain-sentinel path/to/project/

Force a specific chain/language

chain-sentinel file.compact --midnight
chain-sentinel file.rs --rust
chain-sentinel file.move --move
chain-sentinel file.sol --evm

JSON output

chain-sentinel path/to/Contract.sol --json

🔗 Supported Languages & File Types

Ecosystem

File Types

Description

EVM / Solidity

.sol

Smart contracts for Ethereum, BSC, Polygon…

Move

.move

Aptos & Sui modules

Midnight Network

.compact, .midnight.json

Compact contracts + Midnight dApp manifests

Rust Contracts

.rs

Solana, CosmWasm, NEAR, Substrate

🧠 How It Works

chain‑sentinel uses pattern‑based static analysis to detect:

authorization flaws

reentrancy risks

unsafe low‑level calls

unchecked arithmetic

resource misuse

capability misuse

state machine inconsistencies

unsafe agent permissions

misconfigured zk suite definitions

unsafe CPI calls

missing account validation

unsafe deserialization

Each language has its own analyzer and pattern engine:

sentinel/
  core/
  evm/
  move/
  midnight/
    compact_patterns.py
    compact_analyzer.py
    dapp_patterns.py
    dapp_analyzer.py
  rust/

📁 Example Output

Human‑readable

=== SimpleStaking.sol ===
[MEDIUM] [reentrancy] Low-level call with value; check for reentrancy vulnerabilities. (line 88)
[INFO]   [auth]       Owner-only function; check centralization and privilege risks. (line 12)

JSON

[
  {
    "severity": "MEDIUM",
    "category": "reentrancy",
    "message": "Low-level call with value; check for reentrancy vulnerabilities.",
    "file": "SimpleStaking.sol",
    "line": 88
  }
]

🛠️ Roadmap

v0.2.x

Severity scoring engine

Pattern categories in output

Configurable rule sets

Ignore lists

Directory‑level summaries

v0.3.x

Bytecode scanning (EVM)

Move AST scanning

Compact AST scanning

Rust AST scanning

v0.4.x

Plugin system

CI integration templates

VS Code extension

Midnight Network developer tools integration

🤝 Contributing

Pull requests are welcome. To contribute:

Fork the repository

Create a feature branch

Add tests for new analyzers or patterns

Submit a PR

📄 License

MIT License — free to use, modify, and distribute.

🧑‍💻 Author

Derrick MeredithBlockchain Engineer • Smart Contract Auditor • Midnight Network DeveloperLeitchfield, KY


