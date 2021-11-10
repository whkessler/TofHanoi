from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, redirect, request, session, flash
from flask_app import app
import re

class Solution():
    def __init__(self):
        self.count = 0
        self.A = 1
        self.B = 2
        self.C =  3
        self.seq = []


    def hanoi(self,n,A,B,C):
        if n > 0:
            self.hanoi(n-1,A,C,B)
            self.seq.append([A,C])
            self.count += 1
            self.hanoi(n-1,B,A,C)
        return self.count


