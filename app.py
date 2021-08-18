
from flask import Flask,jsonify,request
app = Flask(__name__)
@app.route('/v1',methods=["GET"])
def payload():
    response = jsonify({"payload":"input"})
    response.status_code=220
    return response
@app.route ('/sanitized/',methods=["GET"])
def sanitized():
        response=jsonify({"result":"sanitised"})
        response.status_code=440
        return response
@app.route ('/input/',methods=["GET"])
def input():
        response=jsonify({"result":"unsanitised"})
        response.status_code=440
        return response
if __name__=='__main__':
    app.run(debug=True,port=5599)