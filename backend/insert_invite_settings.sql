INSERT INTO credit_settings (action, price, description) VALUES
  ('invite_codes_per_user', 3, '每人可生成的邀请码数量'),
  ('invite_credits', 50, '邀请码奖励积分')
ON CONFLICT (action) DO NOTHING;
