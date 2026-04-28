CREATE VIEW v_SentimentOverall AS
SELECT sentiment, COUNT(*) AS total_posts
FROM SentimentData
GROUP BY sentiment;

CREATE VIEW v_SentimentMonthly AS
SELECT 
    sentiment,
    post_date,
    COUNT(*) AS daily_count
FROM SentimentData
GROUP BY sentiment, post_date;
