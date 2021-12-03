from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)



@api.route('/hello')
class HelloWorld(Resource):

    test='world'

    def get(self):
        return {'hello': self.test}
    def put(self, data):
        self.test=data
        return {'hello': data}

@api.route('/test')
class Test(Resource):
    def get(self):
        return "test"

if __name__ == '__main__':
    app.run(debug=True)