from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, redirect, request, session, flash
from flask_app import app

class Tower():
    def __init__(self, data):
        self.id = data['id']
        self.disc = data['disc']
        self.move = data['move']
        self.detail = data['detail']
        self.created_at = data['created_at']


    @classmethod
    def save(cls, data):
        connection = connectToMySQL('hanoi_schema')
        query = "INSERT INTO towers(disc, move, detail, created_at) VALUES(%(disc)s, %(move)s, %(detail)s, NOW());"
        new_tower_id = connection.query_db(query, data)

        return new_tower_id

    @classmethod
    def get_all_towers(cls):
        connection = connectToMySQL('hanoi_schema')
        towers = connection.query_db("SELECT * FROM towers;")

        results = []

        for tower in towers:
            results.append(cls(tower))

        return results
    @classmethod
    def get_by_id(cls, data):
        connection = connectToMySQL('hanoi_schema')
        query = "SELECT * FROM towers WHERE towers.id = %(id)s;"
        results = connection.query_db(query, data)
        
        return Tower(results[0])

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM towers WHERE id = %(id)s;"
        return connectToMySQL('hanoi_schema').query_db(query, data)
