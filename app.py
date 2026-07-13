from flask import Flask, render_template, request, redirect, url_for, session, flash
from sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Year-12-Assessment-2.db"  
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  