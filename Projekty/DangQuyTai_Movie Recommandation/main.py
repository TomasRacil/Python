import requests
omdb_api_key = "fe23422a"
i = "tt3896198" #param_Omdp
tastedive_key = "367007-dangquyt-VSK39QKH"

def get_movies_from_tastedive(name):      
    """
    Function to extract from tastedive.com 
        parameter name :{str} name of movie

        url:
            k: Your API access key
            q: the search query; consists of a series (at least one) of bands, movies, TV shows, podcasts, books, authors and/or games, separated by commas
            type: type of results(music, movies, shows, podcasts, books, authors, games...)
            limit: maximum number of recommendations to retrieve.

            Base endpoint:
                #print(tastedive_req.url)
                #https://tastedive.com/api/similar?k=367007-dangquyt-VSK39QKH&q="movie_name"&type=movies&limit=5
        
        return {json}

    """
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {}
    params_diction["k"] = tastedive_key
    params_diction["q"] = name
    params_diction["type"] = "movies"
    params_diction["limit"] = 5
    tastedive_req = requests.get(baseurl, params = params_diction)
    return tastedive_req.json()


def extract_movie_titles(dict_from_tastedive):
    """
    Function to extract the list of movie titles from a dictionary returned by get_movies_from_tastedive
        parameter dict_from_tastedive :{dict} 
        return {list}
    """
    movies_titles = []
    for movie in dict_from_tastedive["Similar"]["Results"]:
        movies_titles.append(movie["Name"])
    return movies_titles



def get_related_movies(list_movies_title):
    """
    Function to call get_related_titles
        #It takes a list of movie titles as input.
        #It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list

        parameter list_movies_title : {list}

        return {list}

    """
    related_movies = []
    for movie in list_movies_title:
        if movie not in related_movies:
            related_movies.append(movie)
        data_2 = get_movies_from_tastedive(movie)
        movies_titles_2 = extract_movie_titles(data_2)
        for movie_2 in movies_titles_2:
            if movie_2 not in related_movies:
                related_movies.append(movie_2)
    return related_movies

#The function should return a dictionary with information about that movie.
def get_movie_data(movie):
    """
    Function to extract from omdbapi.com information about movie.
        parameter movie :{str} name of movie

        url:
            -i: A valid IMDb ID
            -apikey
            -t: Type of result to return (movie, series...)
            Base endpoint:
                #print(omdb_api_req.url)
                #https://www.omdbapi.com/?i=tt3896198&apikey=fe23422a&t="movie_name"

        return {json}
    """
    movie = movie.lower() 
    baseurl = "https://www.omdbapi.com/"
    params_diction = {}
    params_diction["i"] = i
    params_diction["apikey"] = omdb_api_key
    params_diction["t"] = movie
    omdb_api_req = requests.get(baseurl, params = params_diction)
    return omdb_api_req.json()


# It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer
def get_movie_rating(data_from_omdb):
    """
    Function to extracts the Rotten Tomatoes rating
        parameter data_from_omdb : {list}
        return {int}
    """
    if "Error" in data_from_omdb:
        return "Error"
    else:
        for dit in data_from_omdb["Ratings"]:
            if dit["Source"] == "Rotten Tomatoes":
                return dit["Value"]
        return "Dont have Rotteen's rating"
 
 
#Sort movie by socre
def sort_score(score):
    i = 0
    if "%" in score:
        i += 1
        if len(score) == 3:
            i += 1
    return i


def get_sorted_recommendations(related_movies): 
    """
    Function to get sorted list of related movie titles as output, up to five related movies for each input movie title.
        parameter related_movies : {list}
        return {list}
    """
    dict_movies = {}
    for movie in related_movies:
        dict_movies[movie] = get_movie_rating(get_movie_data(movie))
    final_list_movie = sorted(dict_movies.keys(), key= lambda x:(sort_score(dict_movies[x]), dict_movies[x], len(dict_movies[x])), reverse= True)
    for movie in dict_movies:
        print(movie + ":" + dict_movies[movie])
    return final_list_movie


def main():
    film_input = input(" Enter your film: ")
    print("Recomendatins of '{}' is:...'".format(film_input))
    data = get_movies_from_tastedive(film_input)
    data = extract_movie_titles(data)
    related_data = get_related_movies(data)
    movie_recomendations = get_sorted_recommendations(related_data)
    print(movie_recomendations)

if __name__ == '__main__':
    main()
