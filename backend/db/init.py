import psycopg2
from db import gets
from db import sets
import os
from dotenv import load_dotenv
load_dotenv()

# Conectar a la base de datos
conn = psycopg2.connect(
    host=os.getenv('DB_HOST'),
    database=os.getenv('DB_DATABASE'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD')
)

def get_all_jobs():
    resp = gets.get_all_jobs(conn)
    return resp

def get_credentials(username):
    resp = gets.get_credentials(conn, username)
    return resp

def list_jobs_taked_details():
    resp = gets.list_jobs_taked_details(conn)
    return resp

def list_jobs_takeds_names():
    resp = gets.list_jobs_takeds_names(conn)
    return resp

def get_all_user_for_job(job):
    resp =  gets.get_all_user_for_job(conn, job)
    return resp

def get_history(user):
    resp = gets.get_history(conn, user)
    return resp

def get_users(rol):
    resp = gets.get_users(conn, rol)
    return resp

def add_user(data, tipo_usuario):
    resp = sets.add_user(conn, data, tipo_usuario)
    return resp

def get_star_average(id):
    resp = gets.get_star_average(conn, id)
    return resp

def get_user_details(id):
    resp = gets.get_user_details(conn, id)
    return resp