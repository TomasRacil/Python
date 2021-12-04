from re import DEBUG
from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import logging

logging.basicConfig(level=DEBUG)

app = Flask(__name__)
api = Api(app)

# parser = reqparse.RequestParser()
# parser.add_argument('rate', type=str, help='World to change')
# args = parser.parse_args()

@api.route('/hello')
class HelloWorld(Resource):

    test='world'

    def get(self):
        return {'hello': self.test}
    def post(self):
        self.test=request.form['data']
        logging.debug(request.form['data'])
        return {'hello': self.test}

@api.route('/test')
class Test(Resource):
    def get(self):
        return "test"

if __name__ == '__main__':
    app.run(debug=True)