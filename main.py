import pandas as pd
import pickle

# 📂 DOĞRU PATH

movies = pd.read_csv(r"C:\Users\egemen\PycharmProjects\project\movie-recommend\data\movies.csv")

# 🎯 sadece title

movies = movies[['title']]

movies = movies.dropna()
movies = movies.reset_index(drop=True)

pickle.dump(movies, open('movies.pkl', 'wb'))

print(movies.head())
print(movies.columns)