from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class StudentModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	surname = db.Column(db.String(100), nullable=False)
	age = db.Column(db.Integer, nullable=False)
	gender = db.Column(db.String(100), nullable=False)

def __repr__(self):
	return "Student %s (name, surname, age, gender)"
        

student_put_args = reqparse.RequestParser()
student_put_args.add_argument("name", type=str, help="name of the student is required", required=True)
student_put_args.add_argument("surname", type=str, help="surname of the student", required=True)
student_put_args.add_argument("age", type=int, help="age of the student", required=True)
student_put_args.add_argument("gender", type=str, help="gender of the student", required=True)

student_update_args = reqparse.RequestParser()
student_update_args.add_argument("name", type=str, help="name of the student is required")
student_update_args.add_argument("surname", type=str, help="surname of the student")
student_update_args.add_argument("age", type=int, help="age of the student")
student_update_args.add_argument("gender", type=str, help="gender of the student")

student_delete_args = reqparse.RequestParser()
student_delete_args.add_argument("name", type=str, help="name of the student is required")
student_delete_args.add_argument("surname", type=str, help="surname of the student")
student_delete_args.add_argument("age", type=int, help="age of the student")
student_delete_args.add_argument("gender", type=str, help="gender of the student")


resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'surname': fields.Integer,
	'age': fields.Integer,
    'gender': fields.String,
}

class Student(Resource):
	@marshal_with(resource_fields)
	def get(self, student_id):
		result = StudentModel.query.filter_by(id=student_id).first()
		if not result:
			abort(404, message="Could not find student with that id")
		return result

	@marshal_with(resource_fields)
	def put(self, student_id):
		args = student_put_args.parse_args()
		result = StudentModel.query.filter_by(id=student_id).first()
		if result:
			abort(409, message="Student id taken...")

		student = StudentModel(id=student_id, name=args['name'], surname=args['surname'], age=args['age'], gender=args['gender'])
		db.session.add(student)
		db.session.commit()
		return student, 201

	@marshal_with(resource_fields)
	def patch(self, student_id):
		args = student_update_args.parse_args()
		result = StudentModel.query.filter_by(id=student_id).first()
		if not result:
			abort(404, message="Student doesn't exist, cannot update")

		if args['name']:
			result.name = args['name']
		if args['surname']:
			result.surname = args['surname']
		if args['age']:
			result.age = args['age']
		if args['gender']:
			result.age = args['gender']

		db.session.commit()

		return result
    
	@marshal_with(resource_fields)
	def delete(self, student_id):
		return '', 204
	db.session.delete()
	db.session.commit()
	    

api.add_resource(Student, "/student/<int:student_id>")

if __name__ == "__main__":
    app.run(debug=True)