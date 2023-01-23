import spacy

file = open('movies.txt', 'r')
contents = file.readlines()

planet_hulk_description = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'

def movie_match(description):
    movie_descriptions_nlp = []

    nlp = spacy.load('en_core_web_md')

    for line in contents:
        similarity_score = nlp(line).similarity(nlp(description))
        movie_descriptions_nlp.append(similarity_score)

    best_match = max(movie_descriptions_nlp)
    best_match_index = movie_descriptions_nlp.index(best_match)

    return f"The most similar movie to Planet Hulk is {contents[best_match_index][0:7]}."

print(movie_match(planet_hulk_description))
    


