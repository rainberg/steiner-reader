#!/bin/bash
BACKUP_FILE="/tmp/steiner_reader_before_bild_cleanup_$(date +%Y%m%d_%H%M%S).sql.gz"
ssh root@66.154.112.162 "su - postgres -c \"pg_dump steiner_reader\" | gzip > $BACKUP_FILE"
echo "Backup saved to: $BACKUP_FILE"
ssh root@66.154.112.162 "ls -lh $BACKUP_FILE"
