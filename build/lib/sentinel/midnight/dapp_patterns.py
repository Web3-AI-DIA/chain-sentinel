from typing import List, Dict

# Pattern-based checks for Midnight dApp manifests and configs (.midnight.json).
# Focus on agent permissions, zk suite config, privy rules, and endpoints.

MIDNIGHT_DAPP_PATTERNS: List[Dict[str, str]] = [
    {
        "name": "missing_manifest_name",
        "severity": "MEDIUM",
        "category": "config",
        "description": "Manifest missing 'name' field; dApp metadata incomplete.",
        "match": "\"name\"",
    },
    {
        "name": "missing_privy_rules",
        "severity": "HIGH",
        "category": "privacy",
        "description": "Privy rules missing; verify access control for sensitive data.",
        "match": "\"privy\"",
    },
    {
        "name": "unsafe_agent_permissions",
        "severity": "HIGH",
        "category": "agents",
        "description": "AI agent has broad permissions; verify allowed actions.",
        "match": "\"agents\"",
    },
    {
        "name": "zk_suite_config",
        "severity": "INFO",
        "category": "zk",
        "description": "Zk suite configured; verify proof requirements and constraints.",
        "match": "\"zkSuite\"",
    },
    {
        "name": "http_endpoint",
        "severity": "MEDIUM",
        "category": "endpoints",
        "description": "HTTP endpoint defined; verify input validation and auth.",
        "match": "\"endpoint\"",
    },
]
