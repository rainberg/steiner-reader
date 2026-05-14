#!/usr/bin/env python3
"""Batch download and import GA epub books."""
import os
import sys
import time
import subprocess
import re
import urllib.request
import ssl

IMPORTER = os.path.expanduser("/home/ubuntu/steiner-reader/scripts/epub_importer_pipe.py")
DOWNLOAD_DIR = "/tmp/epub_batch"
LOG_FILE = "/tmp/epub_batch_log.txt"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

GA_NUMBERS = list(range(1, 190))  # GA001-GA189

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def url_available(ga_n):
    url = f"https://odysseetheater.org/GA/eBook/epub/GA{ga_n:03d}.epub"
    try:
        req = urllib.request.Request(url, method="HEAD")
        resp = urllib.request.urlopen(req, timeout=5, context=ctx)
        return resp.status == 200
    except:
        return False

def download(ga_n):
    url = f"https://odysseetheater.org/GA/eBook/epub/GA{ga_n:03d}.epub"
    path = os.path.join(DOWNLOAD_DIR, f"GA{ga_n:03d}.epub")
    if os.path.exists(path) and os.path.getsize(path) > 1000:
        return path
    try:
        dl = urllib.request.urlopen(url, timeout=30, context=ctx)
        data = dl.read()
        with open(path, "wb") as f:
            f.write(data)
        return path
    except Exception as e:
        return None

def import_book(ga_n):
    path = os.path.join(DOWNLOAD_DIR, f"GA{ga_n:03d}.epub")
    if not os.path.exists(path):
        return "NO_FILE"
    
    result = subprocess.run(
        ["python3", IMPORTER, path],
        capture_output=True, text=True, timeout=120
    )
    stdout = result.stdout
    stderr = result.stderr
    
    # Check success
    if "imported successfully" in stdout:
        # Parse chapter count
        m = re.search(r'(\d+) chapters', stdout)
        chapters = m.group(1) if m else "?"
        return f"OK({chapters}ch)"
    elif "No valid code" in stdout:
        return "NO_CONTENT"
    else:
        # Return error snippet
        err = stdout[-300:] if stdout else stderr[-300:]
        return f"FAIL: {err[:100]}"

def main():
    print(f"Batch import starting at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Log: {LOG_FILE}")
    print()
    
    log_entries = []
    results = {"ok": 0, "empty": 0, "fail": 0, "skip": 0, "time": 0}
    
    for ga_n in GA_NUMBERS:
        start = time.time()
        ga_str = f"GA{ga_n:03d}"
        
        # Check availability
        avail = url_available(ga_n)
        if not avail:
            entry = f"{ga_str:6s} | SKIP (not available)"
            print(entry)
            log_entries.append(entry)
            results["skip"] += 1
            continue
        
        # Download
        path = download(ga_n)
        if not path:
            entry = f"{ga_str:6s} | SKIP (download failed)"
            print(entry)
            log_entries.append(entry)
            results["fail"] += 1
            continue
        
        # Import
        status = import_book(ga_n)
        elapsed = time.time() - start
        
        entry = f"{ga_str:6s} | {status:20s} | {elapsed:.0f}s"
        print(entry)
        log_entries.append(entry)
        
        if status.startswith("OK"):
            results["ok"] += 1
        elif status == "NO_CONTENT":
            results["empty"] += 1
        else:
            results["fail"] += 1
        
        results["time"] += elapsed
        
        # Small delay between imports to avoid overwhelming server
        if ga_n < max(GA_NUMBERS):
            time.sleep(0.5)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"SUMMARY at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    print(f"  OK:     {results['ok']}")
    print(f"  Empty:  {results['empty']}")
    print(f"  Fail:   {results['fail']}")
    print(f"  Skip:   {results['skip']}")
    print(f"  Time:   {results['time']:.0f}s ({results['time']/60:.1f}min)")
    
    # Write log
    with open(LOG_FILE, "w") as f:
        f.write(f"Batch Import Log - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"{'='*60}\n")
        for entry in log_entries:
            f.write(entry + "\n")
        f.write(f"\n{'='*60}\n")
        f.write(f"OK={results['ok']} Empty={results['empty']} Fail={results['fail']} Skip={results['skip']} Time={results['time']:.0f}s\n")
    
    print(f"\n  Log saved to: {LOG_FILE}")

if __name__ == "__main__":
    main()
