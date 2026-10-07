from typing import List, Dict

RUST_PATTERNS: List[Dict[str, str]] = [
    {
        "name": "unsafe_block",
        "severity": "HIGH",
        "category": "memory",
        "description": "unsafe block used; verify memory safety and invariants.",
        "match": "unsafe {",
    },
    {
        "name": "unchecked_arithmetic",
        "severity": "MEDIUM",
        "category": "economic",
        "description": "Potential unchecked arithmetic; verify overflow/underflow handling.",
        "match": "+",
    },
    {
        "name": "missing_account_validation",
        "severity": "HIGH",
        "category": "auth",
        "description": "Accounts may not be validated; verify signer and ownership checks.",
        "match": "AccountInfo",
    },
    {
        "name": "cpi_call",
        "severity": "INFO",
        "category": "cpi",
        "description": "Cross-program invocation; verify target program and data.",
        "match": "invoke(",
    },
    {
        "name": "deserialize_unchecked",
        "severity": "MEDIUM",
        "category": "serialization",
        "description": "Deserialization; verify data format and bounds.",
        "match": "try_from_slice",
    },
]
