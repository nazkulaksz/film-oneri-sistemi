import pandas as pd
import pickle


movies = pd.read_csv(r"C:\Users\PycharmProjects\project\data\movies.csv")


movies = movies[['title']]

movies = movies.dropna()
movies = movies.reset_index(drop=True)

pickle.dump(movies, open('movies.pkl', 'wb'))

print(movies.head())
print(movies.columns)
