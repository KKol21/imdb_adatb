from dash import *
from layouts import *
from main import app
from db_connector import db_conn
from dao import userDao, actorDao, movieDao, seriesDao, ratingsDao
from flask import session

actor_dao = actorDao.ActorDAO(db_conn=db_conn)
movie_dao = movieDao.MovieDAO(db_conn=db_conn)
series_dao = seriesDao.SeriesDAO(db_conn=db_conn)
ratings_dao = ratingsDao.RatingsDAO(db_conn=db_conn)

