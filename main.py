import json
from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

videos ={}


class Video(Resource):
    def get(self):
        return videos


api.add_resource(Video, "/video")





class HelloWorld(Resource):
    # def get(self):
    #     return {"data": "Hello World"}
    def get(self, name, age):
        return {"name": name, "age": age}

    def post(self, name, age):
        return {"data": "Post Hello World"}


# api.add_resource(HelloWorld, "/hello")
api.add_resource(HelloWorld, "/hello/<string:name>/<int:age>")


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
