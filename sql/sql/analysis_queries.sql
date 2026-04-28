SELECT sentiment, COUNT(*) AS total_posts
FROM SentimentData
GROUP BY sentiment;

SELECT TOP 10 * FROM SentimentData;
