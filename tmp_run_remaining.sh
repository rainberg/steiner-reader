#!/bin/bash
ssh root@66.154.112.162 'su - postgres -c "psql -d steiner_reader -f /tmp/tmp_remaining_check.sql"'
