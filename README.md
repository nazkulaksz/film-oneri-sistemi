# Movie Recommendation System

This project is a Streamlit-based web application that recommends movies based on user input.

## Features

- Recommends 5 similar movies based on the selected movie
- Handles misspelled inputs using fuzzy matching
- Fetches movie posters using the TMDB API
- Simple and responsive user interface
- Modern card-based design with hover effects

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- TMDB API

## How to Run

`bash
pip install -r requirements.txt
streamlit run app.py

## API Key

This project uses the TMDB API to fetch movie posters.

To run the project, you need to get your own API key:

https://www.themoviedb.org/settings/api

After getting your API key, replace this line in the code:

``python
API_KEY = "YOUR_API_KEY"


## Project Structure

film-oneri/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
└── README.md


