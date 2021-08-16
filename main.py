from flask import Flask, jsonify, request
from http import HTTPStatus

"""Create an instance of the Flask class"""

app = Flask(__name__)

"""Define the strategies list. Start with just adding two strategies stored in memory"""

recipes = [
    {
        "id": 1,
        "name": "Business Blueprint",
        "description": "A deeply comprehensive breakdown of your business products/service, customers, supply chain, and competitive advantage."
    },
    {
        "id": 2,
        "name": "Social Storyboard",
        "description": "Map out a crosschannel brand story using the same techniques as story writers in film/tv."
    }
]

"""Use the route decorator to tell Flask that the /recipes route will route to the get_recipes function, 
and the methods argument to specify that the route decorator will only respond to GET requests. """

@app.route("/recipes", methods=["GET"])
def get_recipes():
    return jsonify({"data": recipes}) # Converts list to JSON format

"""Here we want to pull a specific strategy when someone uses the correct ID.
A function should loop through the strategies list and locate the strategy that has the id that we are looking for. 
If the strategy exists then we should return it. """

@app.route("/recipes/<int:recipe_id>", methods=["GET"])
def get_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe["id"] == recipe_id), None)

    if recipe:
        return jsonify(recipe)

    return jsonify({"message": "recipe not found"}), HTTPStatus.NOT_FOUND

"""Create a recipe function that creates a recipe in memory
Use a methods argument to specify that the route decorator will only respond to POST requests"""

@app.route("/recipes", methods=["POST"])
def create_recipe():
    data = request.get_json()

    name = data.get("name")
    description = data.get("description")

    recipe = {
        "id": len(recipes) + 1,
        "name": name,
        "description": description
    }

    recipes.append(recipe)

    return jsonify(recipe), HTTPStatus.CREATED

"""Now we want to  setup a piece of code for updating recipes. 
Feel free to reuse the same loop code snippet from before!"""

@app.route("/recipes/<int:recipe_id>", methods=["PUT"])
def update_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe["id"] == recipe_id), None)

    if not recipe:
        return jsonify({"message": "recipe not found"}), HTTPStatus.NOT_FOUND

    data = request.get_json()

    recipe.update(
        {
            "name": data.get("name"),
            "description": data.get("description")
        }
    )

    return jsonify(recipe)

if __name__ == "__main__":
    app.run()