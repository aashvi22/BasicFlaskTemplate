#store standard routes for website
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Game
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
# @login_required
def home():
    # FIXME: currently there is HTML content in `base.html` that requires the home view
    if request.method=='POST':
<<<<<<< HEAD
        address = request.form.get('inputAddress')
        name = request.form.get('gameName')
        sportSelect = request.form.get('sportSelect')
        numPeople = request.form.get('numPeople')
        makePublic = request.form.get('makePublic', type = bool)
        new_game = Game(name = name, game_type = sportSelect, num_people = numPeople)
=======
        name = request.form.get('gameName')
        sportSelect = request.form.get('sportSelect')
        currNumPeople = request.form.get('currNumPeople')
        totalNumPeople = request.form.get('totalNumPeople')
        #dateTime = request.form.get('dateTime')
        lat = request.form.get('lat')
        lng = request.form.get('lng')
        new_game = Game(user_id = current_user.id, name = name, game_type = sportSelect, total_number_people = totalNumPeople, initial_number_people = currNumPeople, latitude = lat, longitude = lng)
        #event_datetime = dateTime, ^
>>>>>>> 77e7470936cf004bae09a1e995383825a4adbd27
        db.session.add(new_game)
        db.session.commit()
        flash('Game created', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note=json.load(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
