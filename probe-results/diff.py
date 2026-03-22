#!/usr/bin/env python3
"""Compare two probe-all JSON reports and show what changed."""
import json, sys

a_path, b_path = sys.argv[1], sys.argv[2]
a = json.load(open(a_path))
b = json.load(open(b_path))

a_meta, b_meta = a["meta"], b["meta"]
print(f"\n{'─'*60}")
print(f"  A: {a_meta['device']} iOS {a_meta['ios_version']} ({a_meta['build_version']})")
print(f"  B: {b_meta['device']} iOS {b_meta['ios_version']} ({b_meta['build_version']})")
print(f"{'─'*60}\n")

def services(data, status):
    return {e["service"] for e in data["results"].get(status, [])}

for status in ["SUCCESS", "DENIED", "NOT_FOUND", "REQUIRES_TUNNEL", "FAIL"]:
    a_set = services(a, status)
    b_set = services(b, status)
    only_a = a_set - b_set
    only_b = b_set - a_set
    if only_a or only_b:
        print(f"[{status}] differences:")
        for s in sorted(only_a): print(f"  only in A: {s}")
        for s in sorted(only_b): print(f"  only in B: {s}")
        print()

a_success = services(a, "SUCCESS")
b_success = services(b, "SUCCESS")
both = a_success & b_success
print(f"[SUCCESS] on both ({len(both)}):")
for s in sorted(both): print(f"  {s}")
