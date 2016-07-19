import index
import media

lava = media.Movie("Lava",
                   "A story that takes place over millions of years and is ins"+
                   "pired by the beauty of tropical islands and the allure of "+
                   "ocean volcanoes.",
                   "https://upload.wikimedia.org/wikipedia/en/6/64/Lava_%28201"+
                   "5_film%29_poster.jpg",
                   "https://www.youtube.com/watch?v=Cs4DrHIIhEY")

star_trek_beyond = media.Movie("Star Trek Beyond",
                               "Stranded on a hostile planet, Capt. Kirk (Chri"+
                               "s Pine), Spock (Zachary Quinto) and the rest o"+
                               "f the Enterprise crew face an alien threat.",
                               "https://upload.wikimedia.org/wikipedia/en/b/ba"+
                               "/Star_Trek_Beyond_poster.jpg",
                               "https://www.youtube.com/watch?v=bzD8H6o1awQ")

the_revenant = media.Movie("The Revenant",
                           "When all is lost, you fight.",
                           "https://upload.wikimedia.org/wikipedia/en/b/b6/The"+
                           "_Revenant_2015_film_poster.jpg",
                           "https://www.youtube.com/watch?v=LoebZZ8K5N0")

ghostbusters = media.Movie("Ghostbusters",
                           "Following a ghost invasion of Manhattan, paranorma"+
                           "l enthusiasts band together to stop the otherworld"+
                           "ly threat.",
                           "https://upload.wikimedia.org/wikipedia/en/d/d0/Gho"+
                           "stbusters_2016_film_poster.jpg",
                           "https://www.youtube.com/watch?v=w3ugHP-yZXw")

rogue_one = media.Movie("Rogue One",
                        "Rebels set out on a mission to steal the plans for th"+
                        "e Death Star.",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_"+
                        "One%2C_A_Star_Wars_Story_poster.png",
                        "https://www.youtube.com/watch?v=Ze2kpOZx_kU")

dune = media.Movie("Dune",
                   "A Duke's son leads desert warriors against the galactic em"+
                   "peror and his father's evil nemesis after they assassinate"+
                   " his father.",
                   "https://upload.wikimedia.org/wikipedia/en/5/51/Dune_1984_P"+
                   "oster.jpg",
                   "https://www.youtube.com/watch?v=WHh8dzxTSNw")

movies = [lava, rogue_one, star_trek_beyond, the_revenant, ghostbusters, dune]
index.open_movies_page(movies)
