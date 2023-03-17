from flask import Flask, request
import dill as pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

recommendation = model['get_recommendations']
indices = model['indices']
df_products = model['df_products']

app = Flask(__name__)


@app.route('/similar-products/<product_name>')
def get_similar_products(product_name):
    try:
        # Find the index of the current product
        idx = indices[product_name]
    except KeyError:
        return f"Product '{product_name}' not found in dataset.", 404

    # Get the recommendations for the current product
    recommendations = recommendation(idx)

    # Get the names of the recommended products
    recommended_product_names = [
        df_products.loc[i, 'name'] for i in recommendations]

    # Return the recommended product names as a JSON object
    return {'similar_products': recommended_product_names}


app.run('localhost', 8000, debug=True)
