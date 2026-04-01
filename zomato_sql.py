import duckdb
import pandas as pd

df = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\zomato-project\zomato_cleaned.csv')

con = duckdb.connect()
con.register('zomato', df)

print("Query 1 - Top 10 cities by average rating:")
print(con.execute("""
    SELECT city,
           ROUND(AVG(rating), 2) AS avg_rating,
           COUNT(*) AS total_restaurants
    FROM zomato
    GROUP BY city
    ORDER BY avg_rating DESC
    LIMIT 10
""").df())

print("\nQuery 2 - Online delivery vs rating:")
print(con.execute("""
    SELECT online_delivery,
           ROUND(AVG(rating), 2) AS avg_rating,
           ROUND(AVG(cost), 0) AS avg_cost,
           COUNT(*) AS count
    FROM zomato
    GROUP BY online_delivery
""").df())

print("\nQuery 3 - Best value cities:")
print(con.execute("""
    SELECT city,
           ROUND(AVG(rating), 2) AS avg_rating,
           ROUND(AVG(cost), 0) AS avg_cost,
           ROUND(AVG(value_score), 2) AS avg_value_score
    FROM zomato
    GROUP BY city
    ORDER BY avg_value_score DESC
    LIMIT 10
""").df())

print("\nQuery 4 - High rated affordable restaurants:")
print(con.execute("""
    SELECT name, city, cost, rating, value_score
    FROM zomato
    WHERE rating >= 4.0 AND cost <= 500
    ORDER BY value_score DESC
    LIMIT 10
""").df())
