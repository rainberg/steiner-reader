#!/usr/bin/env python3
"""
Batch re-import all 61 bad books using their individual scripts.
Runs each script sequentially and logs results.
"""
import subprocess
import time
from pathlib import Path

BAD_BOOKS = [
    122, 114, 81, 73, 52, 4, 140, 107, 28, 118,
    180, 184, 29, 188, 186, 130, 123, 129, 67, 7,
    155, 141, 76, 183, 153, 138, 16, 3, 179, 12,
    109, 116, 17, 112, 62, 181, 158, 126, 120, 117,
    11, 136, 121, 119, 21, 176, 135, 132, 54, 24,
    127, 27, 8, 18, 143, 133, 128, 124, 108, 57, 55
]

SCRIPTS_DIR = Path("/home/ubuntu/steiner-reader/scripts/individual")
LOG_FILE = Path("/tmp/batch_reimport_log.txt")

def main():
    results = {"ok": 0, "fail": 0, "skip": 0}
    log_entries = []
    start_time = time.time()

    print(f"Batch re-import starting at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Log: {LOG_FILE}")
    print(f"Books to re-import: {len(BAD_BOOKS)}")
    print()

    for ga_num in BAD_BOOKS:
        ga_str = f"GA{ga_num:03d}"
        script_path = SCRIPTS_DIR / f"{ga_str}_import.py"

        if not script_path.exists():
            entry = f"{ga_str:6s} | SKIP (no script)"
            print(entry)
            log_entries.append(entry)
            results["skip"] += 1
            continue

        book_start = time.time()

        try:
            result = subprocess.run(
                ["python3", str(script_path)],
                capture_output=True, text=True, timeout=300
            )
            elapsed = time.time() - book_start

            if result.returncode == 0 and "imported successfully" in result.stdout:
                # Parse stats
                import re
                m = re.search(r'(\d+) chapters, (\d+) paragraphs, (\d+) sentences', result.stdout)
                stats = f"{m.group(2)}p/{m.group(3)}s" if m else "?"
                entry = f"{ga_str:6s} | ✅ {stats:20s} | {elapsed:.0f}s"
                results["ok"] += 1
            elif result.returncode == 0:
                entry = f"{ga_str:6s} | ⚠️  partial?     | {elapsed:.0f}s"
                results["ok"] += 1
            else:
                err = result.stderr[-100:].replace('\n', ' ')
                entry = f"{ga_str:6s} | ❌ {err[:30]:30s} | {elapsed:.0f}s"
                results["fail"] += 1

        except subprocess.TimeoutExpired:
            entry = f"{ga_str:6s} | ❌ TIMEOUT       | 300s"
            results["fail"] += 1
        except Exception as e:
            entry = f"{ga_str:6s} | ❌ {str(e)[:30]:30s} | -"

        print(entry)
        log_entries.append(entry)

    # Summary
    total_time = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"SUMMARY at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    print(f"  OK:   {results['ok']}")
    print(f"  Fail: {results['fail']}")
    print(f"  Skip: {results['skip']}")
    print(f"  Time: {total_time:.0f}s ({total_time/60:.1f}min)")

    # Write log
    with open(LOG_FILE, "w") as f:
        f.write(f"Batch Re-Import Log - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"{'='*60}\n")
        for entry in log_entries:
            f.write(entry + "\n")
        f.write(f"\n{'='*60}\n")
        f.write(f"OK={results['ok']} Fail={results['fail']} Skip={results['skip']} Time={total_time:.0f}s\n")

    print(f"\n  Log saved to: {LOG_FILE}")

if __name__ == "__main__":
    main()
