from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

STUDENTS = {
    '1': {'name':'Robertje', 'age':64, 'spec':'Azure'},
    '2': {'name':'John', 'age':54, 'spec':'SQL'},
    '3': {'name':'Mariella', 'age':42, 'spec':'Architect'}
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

api.add_resource(StudentList, '/students')
api.add_resource(SpecList, '/specialities')

if __name__ == '__main__':
	app.run(host="0.0.0.0")