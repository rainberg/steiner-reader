-- Migration: Steiner Reader users → Auth Service
-- Generated: 2026-05-27
-- 
-- Source data (4 users):
--   6  | test1    | test1@example.com | credits=14489 | role=user
--   9  | test4    | test4@example.com | credits=100   | role=user
--   11 | Guangrui | ooJerry@gmail.com | credits=196   | role=admin  (ALREADY EXISTS, merge credits only)
--   19 | 廣瑞     | gr@3mudi.com      | credits=418   | role=user
--
-- Strategy:
--   - 3 new users: INSERT into users + user_apps + credit_logs
--   - 1 existing user (ooJerry@gmail.com): UPDATE credits only

BEGIN;

-- ============================================================
-- 1. INSERT new users (preserving bcrypt password_hash)
-- ============================================================

-- User: test1 <test1@example.com>
INSERT INTO users (id, email, password_hash, display_name, role, credits, credits_reserved, is_active, created_at, updated_at)
VALUES (
    gen_random_uuid(),
    'test1@example.com',
    '$2b$12$auKIvzv2UnFo9mP5e8OSEuaJaQbQLdeGL.QH5t71MlymhZ4y9kVI.',
    'test1',
    'user',
    14489.00,
    0,
    true,
    '2026-04-25 05:29:10.297411+00',
    '2026-04-25 05:29:10.297411+00'
);

-- User: test4 <test4@example.com>
INSERT INTO users (id, email, password_hash, display_name, role, credits, credits_reserved, is_active, created_at, updated_at)
VALUES (
    gen_random_uuid(),
    'test4@example.com',
    '$2b$12$VUnkQ6EWe0AqoPyorzyH3upH917.6ePHmq/Zg6snuFfK3fFHEY7FW',
    'test4',
    'user',
    100.00,
    0,
    true,
    '2026-04-25 05:29:11.346222+00',
    '2026-04-25 05:29:11.346222+00'
);

-- User: 廣瑞 <gr@3mudi.com>
INSERT INTO users (id, email, password_hash, display_name, role, credits, credits_reserved, is_active, created_at, updated_at)
VALUES (
    gen_random_uuid(),
    'gr@3mudi.com',
    '$2b$12$wh3jvleJNCj.HJCgSpV5iusKSmCQXJtEdgoTg8iYywIztMJlziUee',
    '廣瑞',
    'user',
    418.00,
    0,
    true,
    '2026-05-16 08:43:55.038783+00',
    '2026-05-16 08:43:55.038783+00'
);

-- ============================================================
-- 2. INSERT user_apps for new users (app_name='steiner')
-- ============================================================

INSERT INTO user_apps (id, user_id, app_name, app_role, joined_at)
SELECT gen_random_uuid(), u.id, 'steiner', u.role, u.created_at
FROM users u
WHERE u.email IN ('test1@example.com', 'test4@example.com', 'gr@3mudi.com')
  AND NOT EXISTS (
    SELECT 1 FROM user_apps ua WHERE ua.user_id = u.id AND ua.app_name = 'steiner'
  );

-- ============================================================
-- 3. INSERT credit_logs for new users
-- ============================================================

INSERT INTO credit_logs (id, user_id, action, amount, balance_after, reserved_after, description, reference_id, created_at)
SELECT gen_random_uuid(), u.id, 'topup', u.credits, u.credits, 0, '从 Steiner Reader 本地迁移', gen_random_uuid()::text, u.created_at
FROM users u
WHERE u.email IN ('test1@example.com', 'test4@example.com', 'gr@3mudi.com')
  AND u.credits > 0;

-- ============================================================
-- 4. MERGE existing user: ooJerry@gmail.com
--    - Add 196 credits from Steiner Reader
--    - Set admin role
--    - Ensure steiner app access
-- ============================================================

-- Add credits
UPDATE users
SET credits = credits + 196.00,
    updated_at = now()
WHERE email = 'ooJerry@gmail.com';

-- Log the credit addition
INSERT INTO credit_logs (id, user_id, action, amount, balance_after, reserved_after, description, reference_id, created_at)
SELECT gen_random_uuid(), u.id, 'topup', 196.00, u.credits, u.credits_reserved, '从 Steiner Reader 本地迁移（合并积分）', gen_random_uuid()::text, now()
FROM users u
WHERE u.email = 'ooJerry@gmail.com';

-- Set admin role
UPDATE users SET role = 'admin', updated_at = now() WHERE email = 'ooJerry@gmail.com';

-- Ensure steiner app access
INSERT INTO user_apps (id, user_id, app_name, app_role, joined_at)
SELECT gen_random_uuid(), u.id, 'steiner', 'admin', now()
FROM users u
WHERE u.email = 'ooJerry@gmail.com'
  AND NOT EXISTS (
    SELECT 1 FROM user_apps ua WHERE ua.user_id = u.id AND ua.app_name = 'steiner'
  );

-- Update existing steiner app role to admin if already exists
UPDATE user_apps
SET app_role = 'admin'
WHERE user_id = (SELECT id FROM users WHERE email = 'ooJerry@gmail.com')
  AND app_name = 'steiner';

COMMIT;
