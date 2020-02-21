from flask import Flask
from flask_restful import Api, Resource, reqparse

# to demonstrate RESTful API that is used to store users details,
# which will have CRUD functions. source: codeburst.io
app = Flask(__name__)
api = Api(app)

#usually this is a database
users = [
    {
        "name": "Vinayak",
        "role": "R & D Engineer",
        "age": 24
    },
    {
        "name": "Suraj",
        "role": "C.A",
        "age": 24
    },
    {
        "name": "Venkatesh",
        "role": "Student",
        "age": 18
    }
]


class User(Resource):

    def get(self, name):
        """
        read operation
        """
        for user in users:
            if name == user.get("name"):
                return user , 200  # success
        return "user not found", 404  # data not found

    def post(self, name):
        """
        write operation
        """
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("role")
        args = parser.parse_args()

        for user in users:
            if name == user.get("name"):
                return "User with name {} already exists".format(name), 400 #request error
        user = {
            "name": name,
            "age": args["age"],
            "role": args["role"]
        }

        users.append(user)
        return user, 201 # created

    def put(self, name):
        """
        update operation
        """
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("role")
        args = parser.parse_args()

        for user in users:
            if name == user.get("name"):
                user["age"]= args["age"]
                user["role"] = args["role"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "role": args["role"]
        }

        users.append(user)
        return user, 201


    def delete(self, name):
        """
        delete operation
        """
        global users
        users = [user for user in users if user.get("name") != name]
        return "{} is deleted".format(name), 200

@app.route('/')
def index():
    return "HELLO WORLD, I AM KAIZEN...:)"

@app.route('/userlist')
def userlist():
    return str(users)

api.add_resource(User, "/user/<string:name>")
app.run(debug=True)