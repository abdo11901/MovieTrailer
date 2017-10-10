import media
import fresh_tomatoes
#The 1st object that we have
toy_story = media.Movie("Toy story",
                        "toys are alive",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#The 2nd object that we have
avatar = media.Movie("Avatar",
                        "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                        "https://i.ytimg.com/vi/a0CDJZu4M5I/movieposter.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#The 3rd object that we have
seven_pounds = media.Movie("Seven Pounds",
                        "A man with a fateful secret embarks on an extraordinary journey of redemption by forever changing the lives of seven strangers.",
                        "http://userscontent2.emaze.com/images/d69d9fd6-75a1-43a0-9866-040165a125de/ad2e2ca4-aa1a-46b8-bbd7-dfede5727ee6.jpg",
                        "https://www.youtube.com/watch?v=MwrtEI-fcmM")

#The 4th object that we have
quick_and_dead = media.Movie("The Quick and the Dead",
                        "A female gunfighter returns to a frontier town where a dueling tournament is being held, which she enters in an effort to avenge her father's death.",
                        "http://i.imgur.com/vDF8UGEl.jpg",
                        "https://www.youtube.com/watch?v=NfRrEUz62Lw")

#The 5th object that we have
godfather = media.Movie("The Godfather",
                        "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                        "https://i.pinimg.com/564x/b6/e4/49/b6e449bcce2c44b4024323db4a01817b.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")

#The 6th object that we have
hacksaw = media.Movie("Hacksaw Ridge",
                        "WWII American Army Medic Desmond T. Doss, who served during the Battle of Okinawa, refuses to kill people, and becomes the first man in American history to receive the Medal of Honor without firing a shot.",
                        "https://i.pinimg.com/236x/92/b1/14/92b1148da96c11b7054a3f2ff3bc5e41--movies-coming-soon-english-movies.jpg",
                        "https://www.youtube.com/watch?v=s2-1hz1juBI")
#The array that include all the 6 movies
movies = [toy_story,avatar,seven_pounds,quick_and_dead,godfather,hacksaw]
#we used the open funtion in fresh tomatoes file to view the movies
fresh_tomatoes.open_movies_page(movies)
