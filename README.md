# Movie Recommender System

A content-based movie recommendation system built with Python and Streamlit, featuring movie posters from TMDB API.

This is an End to End ML project that uses the TMDB movie data to suggest you the best movies according to your liking.

## Features

- Recommends 5 similar movies based on your selection
- Displays movie posters using TMDB API
- Clean and interactive web interface
- Content-based filtering using movie metadata

## Setup

1. Clone the repository:
```bash
git clone https://github.com/maraffayofficial-arch/movie_recommender.git
cd movie_recommender
```

2. Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/Scripts/activate  # On Windows with bash
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Get your TMDB API key:
   - Sign up at https://www.themoviedb.org/signup
   - Go to https://www.themoviedb.org/settings/api
   - Request an API key (choose "Developer" option)

5. Create a `.env` file in the project root:
```bash
cp .env.example .env
```

6. Add your TMDB API key to the `.env` file:
```
TMDB_API_KEY=your_api_key_here
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## How It Works

The system uses:
- **Content-based filtering**: Analyzes movie metadata (genres, keywords, cast, crew)
- **Cosine similarity**: Finds movies with similar characteristics
- **TMDB API**: Fetches movie posters for visual display

## Files

- `app.py` - Main Streamlit application
- `movies.pkl` - Preprocessed movie data
- `similarities.pkl` - Precomputed similarity matrix
- `requirements.txt` - Python dependencies

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn (for similarity computation)
- TMDB API
- Pickle

## License

MIT License
