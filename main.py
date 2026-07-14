import pandas as pd
import pickle
import streamlit as st
import requests
import difflib
import os

API_KEY = "YOUR API KEY"

if not os.path.exists("movies.pkl"):
    movies = pd.read_csv("data/movies.csv")
    movies = movies[['title']]
    movies = movies.dropna()
    movies = movies.reset_index(drop=True)

    pickle.dump(movies, open('movies.pkl', 'wb'))
    print("movies.pkl oluşturuldu")

movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
    data = requests.get(url).json()

    if data['results']:
        poster_path = data['results'][0].get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path

    return "https://via.placeholder.com/300x450?text=No+Image"


def find_closest(title):
    titles = movies['title'].tolist()
    match = difflib.get_close_matches(title, titles, n=1)
    return match[0] if match else None


def recommend(movie):
    matches = movies[movies['title'].str.lower() == movie.lower()]

    if matches.empty:
        return [], []

    movie_index = matches.index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []

    for i in movies_list:
        title = movies.iloc[i[0]].title
        names.append(title)
        posters.append(fetch_poster(title))

    return names, posters

st.set_page_config(page_title="Film Öneri", layout="wide")

st.markdown("""
<style>
.movie-card {
    background-color:#1f1f1f;
    padding:10px;
    border-radius:10px;
    text-align:center;
    color:white;
    transition: all 0.3s ease;
    margin:10px;
}
.movie-card:hover {
    transform: scale(1.08);
    box-shadow: 0 10px 25px rgba(0,0,0,0.6);
    cursor: pointer;
}
.movie-card:active {
    transform: scale(0.95);
}
.movie-card img {
    transition: 0.3s;
}
.movie-card:hover img {
    filter: brightness(1.2);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🎬 Film Öneri Sistemi</h1>", unsafe_allow_html=True)

selected_movie = st.text_input("Sevdiğin bir filmi yaz")

if st.button("Öner"):

    if selected_movie.strip() == "":
        st.warning("Lütfen bir film adı gir")

    else:
        names, posters = recommend(selected_movie)

        if len(names) == 0:
            closest = find_closest(selected_movie)

            if closest:
                st.info(f"Şunu mu demek istedin: **{closest}**")
                names, posters = recommend(closest)
            else:
                st.error("❌ Film bulunamadı!")
                st.stop()

        st.markdown("## Eğer bu filmi sevdiysen bunları da sevebilirsin")

        cols = st.columns(5)

        for i in range(len(names)):
            with cols[i]:
                st.markdown(f"""
                <div class="movie-card" tabindex="0">
                    <img src="{posters[i]}" style="width:100%; border-radius:10px;">
                    <p>{names[i]}</p>
                </div>
                """, unsafe_allow_html=True)
