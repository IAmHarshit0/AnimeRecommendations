import pandas as pd 
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

anime = pd.read_csv('anime.csv')
movie = pd.read_csv('movies.csv')

# Pre Processing Of Data
anime.dropna(axis=0, subset=['genre', 'type', 'rating'], inplace=True)

selected_features = ['genres','keywords','tagline','cast','director']
for feature in selected_features:
  movie[feature] = movie[feature].fillna('')

# Vectorizing The Text
vectorize = TfidfVectorizer()

anime['combined'] =  anime['genre'] + " " + anime['type']
movie['combined'] = movie['genres']+' '+movie['keywords']+' '+movie['tagline']+' '+movie['cast']+' '+movie['director']

anime_vectorized = vectorize.fit_transform(anime['combined'])
movie_vectorized = vectorize.fit_transform(movie['combined'])

# Creating The Similarity Matrices
anime_similarity = cosine_similarity(anime_vectorized)
movie_similarity = cosine_similarity(movie_vectorized)

# Normalizing Ratings
anime['rating_normalized'] = (anime['rating']/10.0)

# Making Functions
def recommend_anime(title, df, similarity, top, alpha=0.2):
    match = difflib.get_close_matches(title, df['name'].tolist())
    index = df[df['name'] == match[0]].index[0]

    score = list(enumerate(similarity[index]))

    score = sorted(score, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i, sim in score:
        rating = df.iloc[i]['rating_normalized']
        hybrid = alpha*sim + (1-alpha)*rating

        # recommendations.append((i, hybrid))
        recommendations.append({
            'Name': df.iloc[i]['name'],
            'Genre': df.iloc[i].get('genre', 'N/A'),
            'Rating': round(df.iloc[i].get('rating', 0), 2),
            'Similarity In %': round(hybrid, 2) * 100
        })

    recommendations = sorted(recommendations, key=lambda x: x['Similarity In %'], reverse=True)

    return pd.DataFrame(recommendations[:top])

def recommend_movies(movie_name, movies_data, similarity, top_n):
    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if not find_close_match:
        print("No close match found.")
        return

    close_match = find_close_match[0]
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    movie_title = []
    i = 1
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]
        if i < top_n:
            sim_score = movie[1]
            # print(i, '.', title_from_index)
            movie_title.append({
                'Name': title_from_index,
                'Genre': movies_data.iloc[i].get('genres', 'N/A'),
                'Rating': movies_data.iloc[i].get('vote_average', 0),
                'Similarity In %': (round(sim_score, 2) * 100.0)            
                })
            i += 1
    return pd.DataFrame(movie_title)