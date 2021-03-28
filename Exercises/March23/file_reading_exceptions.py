def getMovies():
    movies = []




    #get the movie from the file
    try:
        with open("movies.txt") as file:
            for line in file:
                movie = line.replace("\n", "")
                movies.append(movie)
            return movies
    except FileNotFoundError:
        print("The movie file could not be located. Check permissions.")
        return movies

#using my movie program
print("Awesome movies")
movies = getMovies()

for movie in movies:
    print(movie)