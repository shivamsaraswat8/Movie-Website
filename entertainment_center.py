import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=CxwTLktovTU")

#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
school_of_rock = media.Movie("School of Rock",
                             "A school teacher turned rockstar",
                             "https://en.wikipedia.org/wiki/File:School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

Django = media.Movie("Django",
                     "story about slaves",
                             "https://www.google.co.in/search?q=django+unchained+poster+link&sxsrf=ALeKk02yjLemu2AwwZPDCRQfcL9USVvd9A:1593129545364&tbm=isch&source=iu&ictx=1&fir=fRf7GvuusdPNcM%252CiXY0ORhAn3E7fM%252C_&vet=1&usg=AI4_-kQb_CeHRwaI2KFFPpOuRwnOrpZ7uQ&sa=X&ved=2ahUKEwjpuYeFlp7qAhWKcn0KHX_kCh0Q9QEwAXoECAoQEg#imgrc=fRf7GvuusdPNcM",
                             "https://www.youtube.com/watch?v=_iH0UBYDI4g")

idiots = media.Movie("3 idiots",
                             "engineering life based movie",
                             "https://en.wikipedia.org/wiki/File:3_idiots_poster.jpg",
                             "https://www.youtube.com/watch?v=K0eDlFX9GMc")

hungergames = media.Movie("Hunger games",
                             "post apocalypse movie",
                             "http://upload.wikipedia.org/wiki/File:HungerGamesPoster.jpg",
                             "https://www.youtube.com/watch?v=3PkkHsuMrho")
movies=[toy_story, avatar, school_of_rock, Django, idiots, hungergames]
fresh_tomatoes.open_movies_page(movies)
