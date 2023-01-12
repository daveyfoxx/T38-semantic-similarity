""""
This program will use Natural Language Processing (NLP)
to make movie recommendations for the user based on the movie they last watched.

We will run the description of the last movie watched through our language model
and compare the similarity of the words in the description. 

Then we will be able to recommend the movie with the most similar description to 
our user.
"""

# First off, we need to import spaCy
import spacy

# Then load our language model and save it in the nlp variable
# We'll use the 'en_core_web_md' model so that we have access to word vectors.
nlp = spacy.load('en_core_web_md')

# Here, we'll make a function that takes in the description of the last movie watched
# Then compares it with each item in a list of other movie descriptions
# before recommending the movie with the most similar description.
def movie_recommendations(last_movie_watched):
    """
    Run last movie watched argument through language model
    Open movies.txt file
    Read in and add movies from file to list
    Create list for storing similarity percentages
    Loop through movies and compare to last movie watched
    Store each similarity percentage in list
    Find the index of the highest percentage
    Find the same index in movie list
    Recommend best match to user
    """
    last_movie_watched = nlp(last_movie_watched)
    with open('movies.txt', 'r') as movies:
        movie_list = movies.readlines()
        percentage_list = []
        for movie in movie_list:
            movie = nlp(movie)
            similarity_percentage = movie.similarity(last_movie_watched)
            percentage_list += [similarity_percentage]
        best_match = percentage_list.index(max(percentage_list))
        recommended_movie = movie_list[best_match]
        print(f"Recommended for you: {recommended_movie}")

# Here is the description of our last movie watched
planet_hulk = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."
"""
# We'll then call our function and pass our movie description through it
movie_recommendations(planet_hulk)