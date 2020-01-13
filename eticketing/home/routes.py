from flask import Blueprint, render_template, url_for, request, redirect
from eticketing.models import Movie
from eticketing.home.utils import getMovies, getMovieDetails, generateTicket, getTicketDetails

home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@home.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@home.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


@home.route('/book', methods=['GET'])
def book():
    movieList = getMovies()
    return render_template('book.html', movieList=movieList)


@home.route('/book/<int:movie_id>', methods=['GET'])
def book_movie(movie_id):
    movie = getMovieDetails(movie_id)
    return render_template('book_movie.html', movie=movie)

@home.route('/bookticket/<int:movie_id>', methods=['POST'])
def book_ticket(movie_id):
    phoneno, slot, tickets = request.form.get('phoneno'), request.form.get('slot'), request.form.get('tickets')
    generateTicket(movie_id, phoneno, slot, tickets)
    return redirect(url_for('home.success'))

@home.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

@home.route('/details', methods=['GET'])
def details():
    return render_template('details.html')

@home.route('/userdetails', methods=['POST'])
def userDetails():
    phoneno = request.form.get('phoneno')
    result, tcount = getTicketDetails(phoneno)
    return render_template('ticketdetails.html', ticketList=result, tcount=tcount)
