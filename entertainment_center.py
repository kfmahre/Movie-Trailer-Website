import fresh_tomatoes
import media

lava = media.Movie("Lava",
                   "A story that takes place over millions of years and is inspired by the beauty of tropical islands and the allure of ocean volcanoes.",
                   "http://ia.media-imdb.com/images/M/MV5BMTA3ODk3Mzk3NjheQTJeQWpwZ15BbWU4MDk4NzU3NTIx._V1_SY1000_CR0,0,763,1000_AL_.jpg",
                   "https://www.youtube.com/watch?v=Cs4DrHIIhEY")

star_trek_beyond = media.Movie("Star Trek Beyond",
                               "Stranded on a hostile planet, Capt. Kirk (Chris Pine), Spock (Zachary Quinto) and the rest of the Enterprise crew face an alien threat.",
                               "http://ia.media-imdb.com/images/M/MV5BMTU0ODk1MTIxM15BMl5BanBnXkFtZTgwNTk3MTc5ODE@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
                               "https://www.youtube.com/watch?v=bzD8H6o1awQ")

the_revenant = media.Movie("The Revenant",
                           "When all is lost, you fight.",
                           "http://ia.media-imdb.com/images/M/MV5BMjU4NDExNDM1NF5BMl5BanBnXkFtZTgwMDIyMTgxNzE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=LoebZZ8K5N0")

ghostbusters = media.Movie("Ghostbusters",
                           "Following a ghost invasion of Manhattan, paranormal enthusiasts band together to stop the otherworldly threat.",
                           "http://ia.media-imdb.com/images/M/MV5BMTU0OTQ5NDMzNV5BMl5BanBnXkFtZTgwMTUxODMxOTE@._V1_SY1000_CR0,0,673,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=w3ugHP-yZXw")

rogue_one = media.Movie("Rogue One",
                        "Rebels set out on a mission to steal the plans for the Death Star.",
                        "http://ia.media-imdb.com/images/M/MV5BMjQyMzI2OTA3OF5BMl5BanBnXkFtZTgwNDg5NjQ0OTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=Ze2kpOZx_kU")

dune = media.Movie("Dune",
                   "A Duke's son leads desert warriors against the galactic emperor and his father's evil nemesis after they assassinate his father.",
                   "http://ia.media-imdb.com/images/M/MV5BNTkxMjkxNzg3Nl5BMl5BanBnXkFtZTgwNjUyMDI3NjE@._V1_.jpg",
                   "https://www.youtube.com/watch?v=WHh8dzxTSNw")

movies = [lava, rogue_one, star_trek_beyond, the_revenant, ghostbusters, dune]
fresh_tomatoes.open_movies_page(movies)
