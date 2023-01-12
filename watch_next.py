import spacy

nlp = spacy.load('en_core_web_md')

def movie_recommendations(last_movie_watched):
    with open('movies.txt', 'r') as movies:
        movies_string = movies.readlines()
        movie_list = []
        percentage_list = []
        x = 0
        for line in movies_string:
            movie_list.append(line)
            similarity_percentage = nlp(movie_list[x]).similarity(last_movie_watched)
            percentage_list += [similarity_percentage]
            x += 1
        recommended_movie = max(percentage_list)
        print(recommended_movie)

planet_hulk = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."
"""

movie_recommendations(planet_hulk)


