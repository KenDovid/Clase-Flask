from flask import Blueprint, jsonify, request
import pymysql
from conexion import get_db_connection

# Crea un Blueprint para el endpoint de ciclista
ciclista = Blueprint('ciclista', __name__)


@ciclista.route('/etapaBynetapa', methods=['GET'])
def get_ciclista_by_id():
    codigo = request.args.get('netapa')
    conn = get_db_connection()  # Connect to the database
    cursor = conn.cursor(pymysql.cursors.DictCursor)  # Return results as dictionaries
    cursor.execute('SELECT * FROM etapa where netapa='+etapa)  # Execute a SQL query
    users = cursor.fetchall()  # Fetch all rows from the result
    conn.close()  # Close the database connection

    return jsonify(users)

@ciclista.route('/maillot', methods=['POST'])
def create_user():
    data = request.get_json()  # Obtener los datos JSON del cuerpo de la solicitud
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Suponiendo que los datos incluyen: 
        sql = "INSERT INTO maillot (codigo, tipo, color, premio) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (data['codigo'], data['tipo'], data['color'], data['premio']))
        conn.commit()  # Confirmar la transacción
        return jsonify({'message': 'maillot creado exitosamente'}), 204
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return jsonify('No se pudo crear el maillot'), 404
    finally:
        if conn:
            conn.close()

    
@ciclista.route('/etapa', methods=['GET'])
def get_users():
    
    try:
        conn = get_db_connection()  # Connect to the database
        cursor = conn.cursor(pymysql.cursors.DictCursor)  # Return results as dictionaries
        cursor.execute('SELECT * FROM etapa')  # Execute a SQL query
        users = cursor.fetchall()  # Fetch all rows from the result
        return jsonify(users)
    except Exception as e:
        print(f"Ocurrio un error: {e}")
        return jsonify('No se pudo ejecutar la consulta')
    finally:
        print('llega')
        if conn != None:
            conn.close()

@ciclista.route('/etapa/<int:netapa>', methods=['DELETE'])
def delete_user(netapa):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM etapa WHERE netapa = %s"
        cursor.execute(sql, (netapa,))
        conn.commit()
        
        if cursor.rowcount == 0:
            return jsonify({'message': 'Etapa no encontrado'}), 404
        return jsonify({'message': 'Etapa eliminado exitosamente'})
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return jsonify('No se pudo eliminar la etapa'), 500
    finally:
        if conn:
            conn.close()