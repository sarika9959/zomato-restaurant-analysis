import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df = pd.read_excel(r'C:\Users\DELL\OneDrive\Desktop\zomato-project\zomato.xlsx', sheet_name='zomato')
print(df.shape)
print(df.head())
df = df[['Restaurant Name', 'City', 'Cuisines', 'Average Cost for two', 'Has Online delivery', 'Aggregate rating', 'Votes']]
df.columns = ['name', 'city', 'cuisines', 'cost', 'online_delivery', 'rating', 'votes']
df = df[df['rating'] > 0]
df = df[df['cost'] > 0]
df = df.dropna()
df['value_score'] = (df['rating'] / df['cost']) * 1000
print(df.shape)
print("Data cleaned successfully!")
city_rating = df.groupby('city')['rating'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=city_rating.values, y=city_rating.index, palette='Greens_r')
plt.title('Top 10 Cities by Average Restaurant Rating')
plt.xlabel('Average Rating')
plt.tight_layout()
plt.savefig(r'C:\Users\DELL\OneDrive\Desktop\zomato-project\chart1_city_ratings.png', dpi=150)
plt.show()
print("Chart 1 saved!")
plt.figure(figsize=(7, 4))
sns.boxplot(x='online_delivery', y='rating', data=df, palette='Set2')
plt.title('Online Delivery vs Restaurant Rating')
plt.xlabel('Has Online Delivery')
plt.ylabel('Rating')
plt.tight_layout()
plt.savefig(r'C:\Users\DELL\OneDrive\Desktop\zomato-project\chart2_delivery.png', dpi=150)
plt.show()
print("Chart 2 saved!")
plt.figure(figsize=(10, 5))
value_city = df.groupby('city')['value_score'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=value_city.values, y=value_city.index, palette='Blues_r')
plt.title('Top 10 Best Value-for-Money Cities on Zomato')
plt.xlabel('Value Score')
plt.tight_layout()
plt.savefig(r'C:\Users\DELL\OneDrive\Desktop\zomato-project\chart3_value_score.png', dpi=150)
plt.show()
print("Chart 3 saved!")
df.to_csv(r'C:\Users\DELL\OneDrive\Desktop\zomato-project\zomato_cleaned.csv', index=False)
print("Cleaned data saved!")
