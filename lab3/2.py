#1
def imdb_score(movie):
    return  movie['imdb']>5.5

#2
def movies_5_5(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

#3
def movies_category(movies, category):
    return [movie for movie in movies if movie['category'].upper() == category.upper()]

#4
def average(movies):
    if not movies:  
        return 0
    return sum(movie['imdb'] for movie in movies) / len(movies)


#5
def average_imdb_by_category(movies, category):
    return average_imdb_score(movies_in_category(movies, category))




