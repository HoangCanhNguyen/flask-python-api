from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

students = [{
    "name": "Dang Tran Toan",
    "birthday": "1999-12-27",
    "id": "17021065",
    "gender": "Nam",
    "vnuEmail": "17021065@vnu.edu.vn",
    "privateEmail": "toandt2701@gmail.com",
    "relations": [
        {
          "relation1": {
            "name": "Dang Hung Son",
            "phone": "0988381615",
          }
        }
    ]
}, {
    "name": "Nguyen Hoang Canh",
    "birthday": "1999-12-12",
    "id": "17023432",
    "gender": "Nam",
    "vnuEmail": "17023432@vnu.edu.vn",
    "privateEmail": "canhnguyen@gmail.com",
    "relations": [
        {
          "relation1": {
            "name": "Dang Hung Son",
            "phone": "0988381615",
          }
        }
    ]
}]


class Student(Resource):
    def get(self, student_id):
        return {"student": students[student_id]}


api.add_resource(Student, '/<int:student_id>')

if __name__ == '__main__':
    app.run(debug=True)
