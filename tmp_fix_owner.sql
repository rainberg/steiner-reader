ALTER TABLE credit_settings OWNER TO steiner;
GRANT ALL PRIVILEGES ON TABLE credit_settings TO steiner;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO steiner;
SELECT tablename, tableowner FROM pg_tables WHERE tablename='credit_settings';
