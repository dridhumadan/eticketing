from eticketing.models import Movie, Booking


def getMovies():
    movieList = Movie.objects
    return movieList


def getMovieDetails(movie_id):
    movieDetails = Movie.objects(movie_id = movie_id)[0]
    return movieDetails


def generateTicket(movie_id, phoneno, slot, tickets):
    movie = Movie.objects(movie_id=movie_id)[0]
    booking_id = int(Booking.objects.count()) + 1
    if int(slot) == 1:
        movie.update(dec__shows__slot1=int(tickets))
    else:
        movie.update(dec__shows__slot2=int(tickets))
    booking = Booking(booking_id=int(booking_id), phoneno=int(phoneno), movie_id=int(movie_id), slot=int(slot), tickets=int(tickets))
    booking.save()


def getTicketDetails(phoneno):
    bookings = Booking.objects(phoneno=int(phoneno))
    movies = Movie.objects()
    result = []
    for b in bookings:
        temp = {}
        temp['booking_id'] = b.booking_id
        temp['phoneno'] = b.phoneno
        temp['movie'] = movies[b.movie_id - 1].title
        temp['tickets'] = b.tickets
        if b.slot == 1:
            temp['slot'] = '9:30 AM'
        else:
            temp['slot'] = '4:30 PM'
        result.append(temp)
    return result, len(result)
