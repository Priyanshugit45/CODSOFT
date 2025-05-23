import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie data: {movie: [action, comedy, drama, sci-fi]}
movies = {
    "The Matrix": [1, 0, 0, 1],
    "Inception": [1, 0, 1, 1],
    "Superbad": [0, 1, 0, 0],
    "The Shawshank Redemption": [0, 0, 1, 0],
    "Interstellar": [0, 0, 1, 1],
    "Step Brothers": [0, 1, 0, 0]
}

# User preferences: [action, comedy, drama, sci-fi]
user_prefs = [1, 0, 1, 1]  # Example: likes action, drama, sci-fi

def recommend_movies(user_prefs, movies, top_n=3):
    # Convert movie vectors to numpy array
    movie_names = list(movies.keys())
    movie_vectors = np.array(list(movies.values()))
    user_vector = np.array([user_prefs])
    
    # Calculate cosine similarity
    similarities = cosine_similarity(user_vector, movie_vectors)[0]
    
    # Get top N movie indices
    top_indices = np.argsort(similarities)[-top_n:][::-1]
    
    # Return recommended movies with similarity scores
    return [(movie_names[i], similarities[i]) for i in top_indices]

def main():
    print("Your preferences: Action, Drama, Sci-Fi")
    print("Top 3 recommended movies:")
    recommendations = recommend_movies(user_prefs, movies)
    for movie, score in recommendations:
        print(f"{movie}: {score:.2f} match")

if __name__ == "__main__":
    main()