from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.solution import Solution
from flask_app.models.tower import Tower
import json

@app.route('/')
def index():
    return render_template("main.html")


@app.route('/moves', methods=['POST'])
def moves():
    session['disc'] = request.form['disc']

    return redirect("/show")

@app.route('/show', methods=['GET','POST'])
def show_moves():
    n = int(session['disc'])
    t = Solution()
    s = t.hanoi(n,1,2,3)
    array= t.seq

    session['s'] = s
    jsonStr = json.dumps(array)

    data = {
        'disc':session['disc'],
        'move':session['s'],
        'detail':jsonStr,
    }
    Tower.save(data)
    return render_template('view.html', seq=array, move=session['disc'], count = s)

@app.route('/previous')
def all_towers():

    tower = Tower.get_all_towers()

    return render_template('previous.html', all_towers = tower)

@app.route('/show/<int:tower_id>', methods=['GET'])
def moves_show(tower_id):
    data = {
        'id' : tower_id
    }
    return render_template('show.html', moves_show = Tower.get_by_id(data))

@app.route('/delete/<int:tower_id>')
def delete_tower(tower_id):
    data = {
        'id' : tower_id
    }
    Tower.destroy(data)
    return redirect('/previous')
