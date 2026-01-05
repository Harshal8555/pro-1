from flask import Flask, render_template

app = Flask(__name__)

# Sample movie data (you can replace with a database later)
movies = [
    {"id": 1, "title": "Avengers: Endgame", "poster": "https://via.placeholder.com/300x450?text=Avengers+Endgame", "rating": "8.4"},
    {"id": 2, "title": "Dune: Part Two", "poster": "https://via.placeholder.com/300x450?text=Dune+Part+Two", "rating": "8.8"},
    {"id": 3, "title": "Oppenheimer", "poster": "https://via.placeholder.com/300x450?text=Oppenheimer", "rating": "8.6"},
    {"id": 4, "title": "Deadpool & Wolverine", "poster": "https://via.placeholder.com/300x450?text=Deadpool+Wolverine", "rating": "8.0"},
    {"id": 5, "title": "Inception", "poster": "https://via.placeholder.com/300x450?text=Inception", "rating": "8.8"},
    {"id": 6, "title": "The Matrix", "poster": "https://via.placeholder.com/300x450?text=The+Matrix", "rating": "8.7"},
]

@app.route('/')
def home():
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)