from flask import Blueprint, jsonify, request
import pymysql
from conexion import get_db_connection

# Crea un Blueprint para el endpoint de etapa
maillot = Blueprint('maillot', __name__)

# Create a GET endpoint
@maillot.route('/maillot/<string:codigo>', methods=['PUT'])
def update_user(codigo):
    data = request.get_json()
    try:  
        conn = get_db_connection()
        cursor = conn.cursor()
        # Suponiendo que los datos incluyen 'nombre' y 'edad'
        sql = "UPDATE maillot SET tipo = %s, color = %s, premio = %s WHERE codigo = %s"
        cursor.execute(sql, (data['tipo'], data['color'], data['premio'], codigo))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'maillot no encontrado'}), 404
        return jsonify({'message': 'maillot actualizado exitosamente'})
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return jsonify('No se pudo actualizar el maillot'), 500
    finally:
        if conn:
            conn.close()
