from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin

import pymssql

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

api = Api(app)

server = 'mysqlservertjong999.database.windows.net' 
database = 'mySampleDatabase' 
username = 'azureuser' 
password = 'P0rsche911' 

STUDENTS = {
    '1': {'name':'Robertje', 'age':64, 'spec':'Azure'},
    '2': {'name':'John', 'age':54, 'spec':'SQL'},
    '3': {'name':'Mariella', 'age':42, 'spec':'Architect'},
    '3': {'name':'Maria', 'age':42, 'spec':'Cleaner'}
}

SPECIALITIES = {
    '1' : {'name':'Azure AD'},
    '2' : {'name':'SQL'}
}
parser = reqparse.RequestParser()


class StudentList(Resource):
    def get(self):
        return STUDENTS 
    def post(self):
        parser.add_argument("name", type=str, location='args')
        parser.add_argument("age", type=int, location='args')
        parser.add_argument("spec", type=str, location='args')
        args = parser.parse_args()
        student_id = int(max(STUDENTS.keys())) + 1
        student_id = '%i' % student_id
        STUDENTS[student_id] = {
            "name": args["name"],
            "age": args["age"],
            "spec": args["spec"],
            }
        return STUDENTS[student_id], 201

class SpecList(Resource):
    def get(self):
         return SPECIALITIES

class SQL(Resource):
    def get(self):
        conn = pymssql.connect(server=server, user=username, password=password, database=database) 
        cursor = conn.cursor()  
        cursor.execute('SELECT c.CustomerID, c.CompanyName,COUNT(soh.SalesOrderID) AS OrderCount FROM SalesLT.Customer AS c LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID GROUP BY c.CustomerID, c.CompanyName ORDER BY OrderCount DESC;')  
        row = cursor.fetchone()  
        return row[1]

api.add_resource(StudentList, '/students')
api.add_resource(SpecList, '/specialities')
api.add_resource(SQL, '/SQL')

if __name__ == '__main__':
	app.run(host="0.0.0.0")