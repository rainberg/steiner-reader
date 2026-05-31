const { Client } = require('ssh2');

const conn = new Client();
const commands = [
  'uname -a',
  'cat /etc/os-release | head -3',
  'free -h',
  'df -h /',
  'nproc',
  'systemctl is-active steiner-backend steiner-frontend nginx postgresql',
  'systemctl status steiner-backend --no-pager -l 2>/dev/null | head -15',
  'systemctl status steiner-frontend --no-pager -l 2>/dev/null | head -15',
  'ls -la /opt/steiner-reader/',
  'cat /opt/steiner-reader/backend/.env 2>/dev/null || echo "No .env file"',
  'cat /etc/nginx/conf.d/default.conf 2>/dev/null || cat /etc/nginx/sites-enabled/default 2>/dev/null || echo "No nginx config found"',
  'sudo -u postgres psql -l 2>/dev/null | head -10',
  'ps aux | grep -E "uvicorn|next|nginx|postgres" | grep -v grep',
  'ls -la /opt/steiner-reader/images/ 2>/dev/null | head -10',
  'ls -la /opt/steiner-reader/uploads/ 2>/dev/null | head -5',
  'cat /var/log/steiner-reader/backend.log 2>/dev/null | tail -20',
];

let output = '';
let cmdIndex = 0;

conn.on('ready', () => {
  function runNext() {
    if (cmdIndex >= commands.length) {
      conn.end();
      console.log(output);
      return;
    }
    const cmd = commands[cmdIndex];
    conn.exec(cmd, (err, stream) => {
      if (err) {
        output += `\n=== CMD ${cmdIndex + 1}: ${cmd} ===\nERROR: ${err.message}\n`;
        cmdIndex++;
        runNext();
        return;
      }
      output += `\n=== CMD ${cmdIndex + 1}: ${cmd} ===\n`;
      stream.on('data', (data) => { output += data.toString(); });
      stream.on('stderr', (data) => { output += '[STDERR] ' + data.toString(); });
      stream.on('close', () => {
        cmdIndex++;
        runNext();
      });
    });
  }
  runNext();
});

conn.on('error', (err) => {
  console.error('Connection error:', err.message);
  process.exit(1);
});

conn.connect({
  host: '66.154.112.162',
  port: 22,
  username: 'root',
  password: '3Ai9px4N5p',
  readyTimeout: 15000,
});
