from typing import List, Dict

# Simple pattern-based checks for Solidity/EVM contracts.
# Each pattern is:
#   - name: short identifier
#   - severity: LOW/MEDIUM/HIGH/CRITICAL
#   - category: auth/reentrancy/economic/upgradeability/general
#   - description: human-readable explanation
#   - match: substring to search for (basic v1)

EVM_PATTERNS: List[Dict[str, str]] = [
    {
        "name": "tx_origin_auth",
        "severity": "HIGH",
        "category": "auth",
        "description": "Use of tx.origin for authorization is dangerous.",
        "match": "tx.origin",
    },
    {
        "name": "delegatecall_usage",
        "severity": "HIGH",
        "category": "upgradeability",
        "description": "delegatecall can lead to code injection or storage corruption.",
        "match": "delegatecall",
    },
    {
        "name": "selfdestruct_usage",
        "severity": "MEDIUM",
        "category": "general",
        "description": "Contract can be destroyed; verify who can call selfdestruct.",
        "match": "selfdestruct",
    },
    {
        "name": "low_level_call_value",
        "severity": "MEDIUM",
        "category": "reentrancy",
        "description": "Low-level call with value; check for reentrancy vulnerabilities.",
        "match": ".call{value",
    },
    {
        "name": "low_level_call",
        "severity": "MEDIUM",
        "category": "reentrancy",
        "description": "Low-level call; ensure proper checks and reentrancy protection.",
        "match": ".call(",
    },
    {
        "name": "transfer_usage",
        "severity": "INFO",
        "category": "economic",
        "description": "Uses transfer; check gas assumptions and potential failures.",
        "match": ".transfer(",
    },
    {
        "name": "approve_usage",
        "severity": "INFO",
        "category": "economic",
        "description": "ERC20 approve; check for race conditions and allowance issues.",
        "match": "approve(",
    },
    {
        "name": "onlyOwner_modifier",
        "severity": "INFO",
        "category": "auth",
        "description": "Owner-only function; check centralization and privilege risks.",
        "match": "onlyOwner",
    },
    {
        "name": "reward_rate_variable",
        "severity": "INFO",
        "category": "economic",
        "description": "Reward rate variable; verify emission logic and economic assumptions.",
        "match": "rewardRate",
    },
    {
        "name": "total_supply_usage",
        "severity": "INFO",
        "category": "economic",
        "description": "totalSupply used; check for inflation/deflation and share math.",
        "match": "totalSupply(",
    },
]
