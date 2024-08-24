from flask import Blueprint, jsonify, request
import pymysql
from conexion import get_db_connection

# Crea un Blueprint para el endpoint de etapa
equipo = Blueprint('equipo', __name__)

# Create a GET endpoint
@equipo.route('/equipo', methods=['GET'])
def get_users():
    conn = get_db_connection()  # Connect to the database
    cursor = conn.cursor(pymysql.cursors.DictCursor)  # Return results as dictionaries
    cursor.execute('SELECT * FROM equipo')  # Execute a SQL query
    equipos = cursor.fetchall()  # Fetch all rows from the result
    conn.close()  # Close the database connection

    return jsonify(equipos)  # Return the list as a JSON response

@equipo.route('/equipoBynombre', methods=['GET'])
def get_equipo_by_id():
    nombre = request.args.get('nombre')
    conn = get_db_connection()  # Connect to the database
    cursor = conn.cursor(pymysql.cursors.DictCursor)  # Return results as dictionaries
    cursor.execute('SELECT * FROM equipo where nomeq= "'+ nombre + '"')  # Execute a SQL query
    users = cursor.fetchall()  # Fetch all rows from the result
    conn.close()  # Close the database connection

    return jsonify(users)