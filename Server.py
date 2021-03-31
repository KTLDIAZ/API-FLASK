from flask import Flask
from flask_restful import Api

from Predict import SumOfCards, PredictBlackjack, PredictWith2Cards

app = Flask(__name__)
api = Api(app)

api.add_resource(PredictWith2Cards, '/2cards')
api.add_resource(PredictBlackjack, '/bljk')
api.add_resource(SumOfCards, '/sum')

if __name__ == '__main__':
    app.run(debug=True)
    