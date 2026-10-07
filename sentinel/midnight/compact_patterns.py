from typing import List, Dict

COMPACT_PATTERNS: List[Dict[str, str]] = [
    {
        "name": "public_entry_no_requires",
        "severity": "MEDIUM",
        "category": "auth",
        "description": "Public entry function; verify requires clauses and access control.",
        "match": "public entry",
    },
    {
        "name": "capability_usage",
        "severity": "INFO",
        "category": "capabilities",
        "description": "Capability used; ensure proper scoping and revocation.",
        "match": "capability",
    },
    {
        "name": "resource_duplication",
        "severity": "MEDIUM",
        "category": "resources",
        "description": "Potential resource duplication; verify move/copy semantics.",
        "match": "resource",
    },
    {
        "name": "unchecked_arithmetic",
        "severity": "INFO",
        "category": "economic",
        "description": "Potential unchecked arithmetic; verify invariants and bounds.",
        "match": "+",
    },
    {
        "name": "state_transition",
        "severity": "INFO",
        "category": "state",
        "description": "State transition; ensure all paths are validated.",
        "match": "transition",
    },
]
