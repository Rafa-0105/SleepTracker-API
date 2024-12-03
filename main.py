from flask import Flask, make_response

app = Flask("__name__")

@app.route('/dormir', methods=['POST'])
def post_dormir():

app.run()