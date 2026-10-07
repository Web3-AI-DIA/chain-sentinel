from typing import Any, Dict, List, Optional
import json
import os

class Reporter:
    """
    Collects findings and prints them in either human-readable or JSON form.
    Also tracks aggregate statistics for directory-level summaries.
    """

    def __init__(self, json_output: bool = False):
        self.json_output = json_output
        self.findings: List[Dict[str, Any]] = []

        # Aggregate stats
        self.count_by_severity: Dict[str, int] = {}
        self.count_by_category: Dict[str, int] = {}
        self.count_by_directory: Dict[str, int] = {}

    def add(
        self,
        severity: str,
        category: str,
        message: str,
        file_path: str,
        line: Optional[int] = None,
        score: Optional[float] = None,
        rule_id: Optional[str] = None,
    ):
        finding = {
            "severity": severity,
            "category": category,
            "message": message,
            "file_path": file_path,
            "line": line,
            "score": score,
            "rule_id": rule_id,
        }
        self.findings.append(finding)

        # Normalize keys
        sev = severity.upper()
        cat = category.lower()

        self.count_by_severity[sev] = self.count_by_severity.get(sev, 0) + 1
        self.count_by_category[cat] = self.count_by_category.get(cat, 0) + 1

        directory = os.path.dirname(file_path) or "."
        self.count_by_directory[directory] = self.count_by_directory.get(directory, 0) + 1

    def _print_human(self):
        # Per-file findings
        current_file = None
        for f in self.findings:
            if f["file_path"] != current_file:
                current_file = f["file_path"]
                print()
                print(f"=== {current_file} ===")

            line_str = f"(line {f['line']})" if f["line"] is not None else ""
            print(f"[{f['severity']}] [{f['category']}] {f['message']}. {line_str}")

        # Summary
        print()
        print("=== Summary ===")

        total = len(self.findings)
        print(f"Total findings: {total}")

        if self.count_by_severity:
            print("By severity:")
            for sev, count in sorted(self.count_by_severity.items()):
                print(f"  {sev}: {count}")

        if self.count_by_category:
            print("By category:")
            for cat, count in sorted(self.count_by_category.items()):
                print(f"  {cat}: {count}")

        if self.count_by_directory:
            print("By directory:")
            for d, count in sorted(self.count_by_directory.items()):
                print(f"  {d}: {count}")

    def _print_json(self):
        summary = {
            "total_findings": len(self.findings),
            "by_severity": self.count_by_severity,
            "by_category": self.count_by_category,
            "by_directory": self.count_by_directory,
        }
        output = {
            "findings": self.findings,
            "summary": summary,
        }
        print(json.dumps(output, indent=2))

    def flush(self):
        if self.json_output:
            self._print_json()
        else:
            self._print_human()
