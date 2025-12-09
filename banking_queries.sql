-- example_queries.sql
-- Total transactions per customer
SELECT customer_id, COUNT(*) AS total_txn, SUM(amount) AS total_amount
FROM transactions
GROUP BY customer_id;

-- Monthly spending
SELECT DATE_TRUNC('month', timestamp) AS month, customer_id, SUM(amount) AS monthly_spend
FROM transactions
GROUP BY month, customer_id;

-- High-risk merchant spend
SELECT category, SUM(amount) AS total_spend
FROM transactions
WHERE category IN ('crypto','gambling')
GROUP BY category;
