# import libraries
from flask import Flask, jsonify
# from flask_restful import Api
from flask_restplus import Resource, Api, Namespace  # Flask_Restplus for Swagger UI

from mysql.connector import Error
import mysql.connector

# Import dB
from dbconfig import db_config

# Initializing App
app = Flask(__name__)
api = Api(app)

search_gene = Namespace('search_gene', description='Search Gene and get result')
api.add_namespace(search_gene)


@search_gene.route('/<string:name>', strict_slashes=False)  # If only name in url
@search_gene.route('/<string:name>/<string:species>', strict_slashes=False)  # If only name and species
class GeneFetch(Resource):
    @staticmethod
    def get(name, species=None):
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(buffered=True)
        if species is not None:
            cursor.execute(
                "SELECT stable_id,display_label,species FROM gene_autocomplete WHERE display_label LIKE" + " '"+name+"%'" "AND species = %s",(species,)
            )
        else:
            cursor.execute(
                "SELECT stable_id,display_label,species FROM gene_autocomplete WHERE display_label LIKE" + " '"+name+"%'"

            )
        # gets the number of rows
        results = cursor.fetchall()
        cursor.close()
        if results:
            results = [{'id': result[0], 'name': result[1], 'species': result[2]} for result in results]  # key-value pair
        return jsonify(results)

# Main Function server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")