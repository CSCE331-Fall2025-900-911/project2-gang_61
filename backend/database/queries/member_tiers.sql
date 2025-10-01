SELECT 
  CASE
    WHEN reward_points >= 500 THEN 'Elite'
    WHEN reward_points >= 400 THEN 'Platinum'
    WHEN reward_points >= 300 THEN 'Diamond'
    WHEN reward_points >= 200 THEN 'Gold'
    WHEN reward_points >= 100 THEN 'Silver'
    ELSE 'Bronze'
  END as member_tier,
  COUNT(*) as member_count
FROM members
GROUP BY member_tier
ORDER BY member_count DESC;