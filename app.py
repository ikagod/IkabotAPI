import time

from flask import Flask, jsonify

from src.token.clean_up_driver_processes import clean_up_driver_processes
from src.token.TokenGenerator import TokenGenerator

app = Flask(__name__)

token_generator = None


@app.route("/")
def welcome():
    return jsonify("Welcome to the Ikabot API!")


@app.route("/new_token", methods=["GET"])
def get_token_route():
    try:
        start_time = time.time()
        token = token_generator.get_token()
        print("Token generated in %s seconds" % (time.time() - start_time))
        return jsonify(token), 200
    except Exception as e:
        print(e)
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "An error occurred during the token generation : {}".format(
                        e
                    ),
                }
            ),
            500,
        )


if __name__ == "__main__":
    clean_up_driver_processes()
    token_generator = TokenGenerator()
    app.run()
