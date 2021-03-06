import media
import fresh_tomatoes

# Start session to get the movies and trailers
matrix = media.Movie("MATRIX", "https://upload.wikimedia.org/wikipedia/pt" +
                     "/c/c1/The_Matrix_Poster.jpg", "https://www.youtube." +
                     "com/watch?v=m8e-FF8MsqU")


star_wars_last_jedi = media.Movie("Star Wars The Last Jedi", "https://" +
                                  "upload.wikimedia.org/wikipedia/en/7" +
                                  "/7f/Star_Wars_The_Last_Jedi.jpg",
                                  "https://www.youtube.com/watch?v=Q0C" +
                                  "bN8sfihY")


total_recall = media.Movie("Total Recall", "https://upload.wikimedia.org" +
                           "/wikipedia/pt/a/a5/TotalRecall2012Poster.jpg",
                           "https://www.youtube.com/watch?v=GljhR5rk5eY")


transformers = media.Movie("Transformers", "https://upload.wikimedia.org" +
                           "/wikipedia/pt/e/ee/Transformers-poster.jpg",
                           "https://www.youtube.com/watch?v=AntcyqJ6brc")


doctor_strange = media.Movie("Doctor Strange", "https://upload.wikimedia." +
                             "org/wikipedia/pt/c/c7/Doctor_Strange_poster" +
                             ".jpg", "https://www.youtube.com/watch?v=MWR" +
                             "UNTLisPo")


national_treasure = media.Movie("National Treasure", "https://upload.wikime" +
                                "dia.org/wikipedia/pt/3/38/National_treasure" +
                                ".jpg", "https://www.youtube.com/watch?v=" +
                                "mcf4tXYjaxo")

# A list of movies is saved into an array to be used as parameter 
movies = [matrix, star_wars_last_jedi, total_recall, transformers,
          doctor_strange, national_treasure]
# Call to create the web page
fresh_tomatoes.open_movies_page(movies)
