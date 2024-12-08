from flask import Flask, make_response, jsonify, request
from infra.DB import Sleep

app = Flask("__name__")

@app.route('/dormir', methods=['POST'])
def post_dormir():
    sleep = request.json
    Sleep.append(sleep)
    return make_response(jsonify(Sleep))

@app.route('/resultados_dormir', methods=['GET'])
def get_sleep():
    return make_response(
        jsonify(Sleep=Sleep,
        )
    )

app.run()