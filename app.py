import flask
from flask import request,jsonify,Response

app = flask.Flask(__name__)
@app.route('/v1/sanitized/input/',methods=['POST','GET'])
def check_input():
    #These are based on MySQL
    sql_injection_characters = ["'","--",";","`"," */ ","/*","#" ,"OR 1=1"]
    check_boolean = any(map(request.form.__contains__,sql_injection_characters))
    if check_boolean:
        response=jsonify({"result":"unsanitized"})
        return response
    else:
        response=jsonify({"result":"sanitized"})
        return response



if __name__ == '__main__':
    app.run(debug = True)
    
