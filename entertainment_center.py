import index
import media

lava = media.Movie("Lava",
                   "A story that takes place over millions of years and is inspired by the beauty of tropical islands and the allure of ocean volcanoes.",
                   "https://upload.wikimedia.org/wikipedia/en/6/64/Lava_%282015_film%29_poster.jpg",
                   "https://www.youtube.com/watch?v=Cs4DrHIIhEY")

star_trek_beyond = media.Movie("Star Trek Beyond",
                               "Stranded on a hostile planet, Capt. Kirk (Chris Pine), Spock (Zachary Quinto) and the rest of the Enterprise crew face an alien threat.",
                               "https://upload.wikimedia.org/wikipedia/en/b/ba/Star_Trek_Beyond_poster.jpg",
                               "https://www.youtube.com/watch?v=bzD8H6o1awQ")

the_revenant = media.Movie("The Revenant",
                           "When all is lost, you fight.",
                           "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
                           "https://www.youtube.com/watch?v=LoebZZ8K5N0")

ghostbusters = media.Movie("Ghostbusters",
                           "Following a ghost invasion of Manhattan, paranormal enthusiasts band together to stop the otherworldly threat.",
                           "https://upload.wikimedia.org/wikipedia/en/d/d0/Ghostbusters_2016_film_poster.jpg",
                           "https://www.youtube.com/watch?v=w3ugHP-yZXw")

rogue_one = media.Movie("Rogue One",
                        "Rebels set out on a mission to steal the plans for the Death Star.",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",
                        "https://www.youtube.com/watch?v=Ze2kpOZx_kU")

dune = media.Movie("Dune",
                   "A Duke's son leads desert warriors against the galactic emperor and his father's evil nemesis after they assassinate his father.",
                   "https://upload.wikimedia.org/wikipedia/en/5/51/Dune_1984_Poster.jpg",
                   "https://www.youtube.com/watch?v=WHh8dzxTSNw")

movies = [lava, rogue_one, star_trek_beyond, the_revenant, ghostbusters, dune]
index.open_movies_page(movies)
