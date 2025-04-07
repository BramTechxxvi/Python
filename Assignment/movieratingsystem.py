from datetime import datetime

def get_header():
    return "==========  MOVIE RATING SYSTEM  ==========\n"

def get_features():
    return " 1. Add a Movie\n 2. Rate a Movie\n 3. View ratings\n 4. View average ratings\n 5. Exit"

def get_date():
    return datetime.now().strftime("%Y-%m-%d")

def get_movie_name(movie_name):
    if not movie_name or movie_name.isspace():
        print("Movie name is empty")
        return False
    else:
        return movie_name.strip().title()

def rate_movie(movie_storage):
    movie_name = input("Enter movie name: ").strip().title()
    if movie_name in movie_storage:
        while True:
            try:
                rating = float(input("Enter rating: "))
                if 1 <= rating <= 5:
                    movie_storage[movie_name]['Rating'].append(rating)
                    print("Rating added successfully \n")
                    break
                else:
                    print("Invalid rating... Enter number between 1 - 5")
            except ValueError:
                print("invalid input... Enter number again")
    else:
        print("Movie not fount! Add movie first")

def view_ratings(movie_storage):
    if not movie_storage:
        print("No movies found")
    else:
        print("\nMovie List")
        for movie, details in movie_storage.items():
            print(f"{movie}: {details}")

def view_average_ratings(movie_storage):
    if not movie_storage:
        print("\nNo movies to rate")
        return
    for movie_name in movie_storage:
        ratings = movie_storage[movie_name]['Rating']
        if ratings:
            average = sum(ratings) / len(ratings)
            print(f" Average rating of {movie_name} is {average:.2f} \n")
        else :
            print(f"No rating yet for {movie_name}")
def main():
    movie_storage = {}
    print(get_header())
    while True:
        print(get_features())
        try:
            features = int(input("Enter an option: "))
            match features:
                case 1:
                    movie_name = input("Enter movie name: ")
                    valid_movie = get_movie_name(movie_name)
                    if valid_movie is False:
                        continue
                    if not valid_movie in movie_storage:
                        movie_details = {
                            'Date': get_date(),
                            'Movie Title': valid_movie,
                            'Rating': []
                            }
                        movie_storage[valid_movie] = movie_details
                        print(f"Movie {valid_movie} added!")
                    else:
                        print(f"Movie already exists!")
                case 2:
                    rate_movie(movie_storage)
                case 3:
                    view_ratings(movie_storage)
                case 4:
                    view_average_ratings(movie_storage)
                case 5:
                    print("Exiting Application...")
                    break
                case _:
                    print("Invalid... Enter number between 1 - 5 \n")
        except ValueError:
            print("Invalid input... Enter number again\n")
main()