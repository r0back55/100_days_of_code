import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

try:
    # Send GET request to the URL
    response = requests.get(URL)
    response.raise_for_status()  # Raise an exception for bad status codes
    empire_webpage = response.text

    # Parse the HTML content of the page
    soup = BeautifulSoup(empire_webpage, "html.parser")

    # Find all article title elements
    all_movies = soup.find_all(name="h3", class_="title")

    # Extract and reverse the list of movie titles
    movie_titles = [movie.getText() for movie in all_movies]
    movies = movie_titles[::-1]

    # Write movies to a file
    with open("./movies.txt", mode="w", encoding="utf-8") as file:
        for movie in movies:
            file.write(f"{movie}\n")

    print("Movie titles have been successfully written to movies.txt")

except requests.RequestException as e:
    print(f"An error occurred while fetching the webpage: {e}")
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")