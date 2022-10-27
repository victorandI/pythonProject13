from flask import Flask, request
from waitress import serve

app = Flask(__name__)

'''@app.route('/api/v1/hello-world-28', methods=['GET'])'''
def index():
    return "Hello world! 28"

'''if __name__=="__main__":
    serve(app, host='127.0.0.1', port=8)'''

    #http://localhost:8/api/v1/hello-world-28