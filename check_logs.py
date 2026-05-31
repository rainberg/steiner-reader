import subprocess

key = r"J:\99_备份\01_key\orcale\Oracle_Frankfurt.ppk"

def run_via_oracle(cmd):
    result = subprocess.run(
        ["plink", "-i", key, "ubuntu@89.168.93.94",
         f"ssh -o StrictHostKeyChecking=no root@66.154.112.162 {cmd}"],
        capture_output=True, text=True, timeout=30
    )
    return result.stdout.strip(), result.stderr.strip()

# Check backend process
out, err = run_via_oracle("'ps aux | grep uvicorn | grep -v grep'")
print("=== Backend processes ===")
print(out)

# Check translation status via API
out, err = run_via_oracle("'curl -s http://localhost:8000/api/lectures/6905/translation-status'")
print("\n=== Translation status ===")
print(out)

# Check if lecture 6905 is in running tasks
out, err = run_via_oracle("'curl -s http://localhost:8000/api/lectures/6905/translate -X POST -H \"Authorization: Bearer test\" 2>&1 | head -c 200'")
print("\n=== Translate attempt ===")
print(out)

# Check backend logs
out, err = run_via_oracle("'ls /opt/steiner-reader/backend/*.log /opt/steiner-reader/backend/nohup.out 2>/dev/null'")
print("\n=== Log files ===")
print(out)
