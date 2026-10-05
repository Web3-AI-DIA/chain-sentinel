from typing import Optional
from sentinel.evm.patterns import EVM_PATTERNS
from sentinel.core.reporter import Reporter

def _read_file(path: str) -> Optional[str]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"[ERROR] Could not read {path}: {e}")
        return None

def analyze_evm_file(path: str, reporter: Reporter):
    content = _read_file(path)
    if content is None:
        return

    # Basic line-based scanning for line numbers
    lines = content.splitlines()

    # Pattern-based scanning
    for pattern in EVM_PATTERNS:
        match_str = pattern["match"]
        if match_str in content:
            # Try to find first line where it appears
            line_num = None
            for idx, line in enumerate(lines, start=1):
                if match_str in line:
                    line_num = idx
                    break

            reporter.add(
                severity=pattern["severity"],
                category=pattern["category"],
                message=pattern["description"],
                file_path=path,
                line=line_num,
            )
