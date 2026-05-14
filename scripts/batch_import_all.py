#!/usr/bin/env python3
"""Batch re-import all 61 bad books using individual scripts."""
import subprocess, sys, time
from pathlib import Path

scripts_dir = Path("/home/ubuntu/steiner-reader/scripts/individual")
scripts = sorted(scripts_dir.glob("GA*_import.py"))
print(f"Found {len(scripts)} import scripts")

passed = 0
failed = []

for i, sp in enumerate(scripts, 1):
    ga = sp.stem.split("_")[0]
    print(f"\n[{i}/{len(scripts)}] Importing {ga}...")
    sys.stdout.flush()

    result = subprocess.run(
        ["python3", str(sp)],
        capture_output=True, text=True, timeout=300
    )

    if result.returncode == 0:
        passed += 1
        # Get last output line for summary
        for line in result.stdout.strip().split("\n")[-3:]:
            if "IMPORTED" in line or "imported" in line:
                print(f"  ✅ {line.strip()}")
                break
        else:
            print(f"  ✅ OK")
    else:
        failed.append(ga)
        # Show last 5 lines of stderr
        err_lines = result.stderr.strip().split("\n")[-5:]
        print(f"  ❌ FAILED (exit={result.returncode})")
        for line in err_lines:
            print(f"     {line}")

print(f"\n{'='*60}")
print(f"Results: {passed}/{len(scripts)} passed")
if failed:
    print(f"Failed: {', '.join(failed)}")
