from flask import Flask, request
import dill as pickle
from flask_cors import CORS, cross_origin

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

recommendation = model['get_recommendations']
indices = model['indices']
df_products = model['df_products']


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/<value>')
@cross_origin()
def hello_world(value):
   # r = request.args.get('value')
    recommendations = recommendation(value)
    a = str(recommendations).split('\n')
    a.pop(len(a)-1)
    d = []
    for i in range(len(a)):
        d.append(a[i][1:(len(a[i]))].strip())
    return d


app.run('localhost', 8000, debug=True)
