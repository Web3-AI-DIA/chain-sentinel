from typing import List, Dict

# Simple pattern-based checks for Move modules.
# Focus on auth, resource handling, and entry functions.

MOVE_PATTERNS: List[Dict[str, str]] = [
    {
        "name": "public_entry_no_auth",
        "severity": "MEDIUM",
        "category": "auth",
        "description": "Public entry function; verify access control and signer usage.",
        "match": "public entry",
    },
    {
        "name": "signer_usage",
        "severity": "INFO",
        "category": "auth",
        "description": "Signer used; ensure proper authorization checks.",
        "match": "&signer",
    },
    {
        "name": "unchecked_arithmetic",
        "severity": "INFO",
        "category": "economic",
        "description": "Potential unchecked arithmetic; verify invariants.",
        "match": "+",
    },
    {
        "name": "resource_move",
        "severity": "INFO",
        "category": "resources",
        "description": "Resource move; ensure correct ownership and lifetime.",
        "match": "move(",
    },
]
