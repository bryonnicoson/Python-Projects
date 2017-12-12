import media
import fresh_tomatoes

suicide_squad = media.Movie("Suicide Squad",
                            "A group of supervillains is freed in order to undertake a government assignment",
                            "https://upload.wikimedia.org/wikipedia/en/5/53/Suicide_Squad_poster.png",
                            "https://www.youtube.com/watch?v=WI3hecGO_04")
                                 
deadpool = media.Movie("Deadpool",
                       "Marvel's most unconventional anti-hero hunts down the man who nearly destroyed his life",
                       "http://www.deadpool.com/images/poster3.jpg",
                       "https://www.youtube.com/watch?v=frRFOrbPfNc")

apocalypse = media.Movie("X-Men: Apocalypse",
                         "With the emergence of the world's first mutant, Apocalypse, the X-men must unite to defeat his extinction-level plan",
                         "https://upload.wikimedia.org/wikipedia/en/0/04/X-Men_-_Apocalypse.jpg",
                         "https://www.youtube.com/watch?v=COvnHv42T-A")

warcraft = media.Movie("Warcraft",
                       "Fleeing their dying home to colonize another, fearsome orc warriors invade the peaceful realm of Azeroth",
                       "https://upload.wikimedia.org/wikipedia/en/5/56/Warcraft_Teaser_Poster.jpg",
                       "https://www.youtube.com/watch?v=2Rxoz13Bthc")

dawn_of_justice = media.Movie("Batman v Superman: Dawn of Justice",
                              "Mankind faces a new threat as Batman embarks on a personal vendetta against Superman",
                              "https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg",
                              "https://www.youtube.com/watch?v=0WWzgGyAH6Y")

civil_war = media.Movie("Captain America: Civil War",
                        "A feud between Captain America and Ironman leaves the Avengers in turmoil",
                        "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                        "https://www.youtube.com/watch?v=uVdV-lxRPFo")

# print(media.Movie.__doc__)

movies=[deadpool, suicide_squad, apocalypse, dawn_of_justice, civil_war, warcraft]
fresh_tomatoes.open_movies_page(movies)


