import media
import fresh_tomatoes

back_to_the_future = media.Movie("Back To The Future",
            "https://resizing.flixster.com/9irKiQGCh4Z6-GShsFgreSGrhi4=/206x305/v1.bTsxMTE3Mzg1MjtqOzE3ODU5OzEyMDA7ODAwOzEyMDA",
            "https://www.youtube.com/watch?v=qvsgGtivCgs")

seven_years_in_tibet = media.Movie("Seven Years In Tibet",
            "https://resizing.flixster.com/LBmXK-aL_f6uOHh5udIIPzoIO5Y=/206x305/v1.bTsxMTIwODM5MjtqOzE3ODU5OzEyMDA7MTUzNjsyMDQ4",
            "https://www.youtube.com/watch?v=LSyr_vJ5t3k")

matrix = media.Movie("The Matrix",
            "https://resizing.flixster.com/1yzfFpXiDM59PoCjAyTIEQWAZCA=/206x305/v1.bTsxMTE2ODA5NjtqOzE3ODU5OzEyMDA7ODAwOzEyMDA",
            "https://www.youtube.com/watch?v=vKQi3bBA1y8")

godfather = media.Movie("The Godfather",
            "https://resizing.flixster.com/MpYibY-hSnt_8CvoNjp5_AAoztw=/206x305/v1.bTsxMTE3MTYxMjtqOzE3ODU5OzEyMDA7ODAwOzEyMDA",
            "https://www.youtube.com/watch?v=w0VGcWHkNeA")

shutter_island = media.Movie("Shutter Island",
            "https://resizing.flixster.com/tJZ7CD3xRyPGegfugsFPoqXvetU=/206x305/v1.bTsxMTE2OTI1NDtqOzE3ODU5OzEyMDA7ODAwOzEyMDA",
            "https://www.youtube.com/watch?v=YDGldPitxic")

carandiru = media.Movie("Carandiru",
            "https://resizing.flixster.com/jqrIz0PE6jlwvN5xtbd6gX1PUU8=/206x305/v1.bTsxMTQ1MzQ4NDtqOzE3ODYyOzEyMDA7MjcwMDszNjAw",
            "https://www.youtube.com/watch?v=BdLvrNz9tUk")

movies = [back_to_the_future, seven_years_in_tibet, matrix, godfather, shutter_island, carandiru]

fresh_tomatoes.open_movies_page(movies)
