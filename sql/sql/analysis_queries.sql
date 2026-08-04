-- Monthly sentiment trend
SELECT
    FORMAT(post_date, 'yyyy-MM') AS month,
    sentiment,
    COUNT(*) AS total_posts
FROM SentimentData
GROUP BY FORMAT(post_date, 'yyyy-MM'), sentiment
ORDER BY month;

-- Days where negative posts crossed the overall average
SELECT post_date, COUNT(*) AS negative_posts
FROM SentimentData
WHERE sentiment = 'Negative'
GROUP BY post_date
HAVING COUNT(*) > (
    SELECT AVG(daily_count * 1.0)
    FROM (
        SELECT post_date, COUNT(*) AS daily_count
        FROM SentimentData
        WHERE sentiment = 'Negative'
        GROUP BY post_date
    ) AS daily
)
ORDER BY negative_posts DESC;

-- Index to speed up date-range filtering
CREATE INDEX idx_sentimentdata_post_date ON SentimentData (post_date);
