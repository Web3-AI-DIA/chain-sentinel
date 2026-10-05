import json
from typing import List, Optional, Dict, Any

class Reporter:
    def __init__(self, json_output: bool = False):
        self.json_output = json_output
        self.findings: List[Dict[str, Any]] = []

    def add(
        self,
        severity: str,
        category: str,
        message: str,
        file_path: str,
        line: Optional[int] = None
    ):
        finding = {
            "severity": severity,
            "category": category,
            "message": message,
            "file": file_path,
            "line": line,
        }
        self.findings.append(finding)

    def _print_text(self):
        if not self.findings:
            print("[OK] No findings.")
            return

        by_file: Dict[str, List[Dict[str, Any]]] = {}
        for f in self.findings:
            by_file.setdefault(f["file"], []).append(f)

        for file_path, file_findings in by_file.items():
            print(f"\n=== {file_path} ===")
            for f in file_findings:
                loc = f" (line {f['line']})" if f["line"] is not None else ""
                print(f"[{f['severity']}] [{f['category']}] {f['message']}{loc}")
        print()

    def _print_json(self):
        print(json.dumps(self.findings, indent=2))

    def flush(self):
        if self.json_output:
            self._print_json()
        else:
            self._print_text()
