from flask import Flask, request, jsonify 
import jwt 

app = Flask(__name__)

SECRET = "123456" 
FLAG = "FLAG{jwt_adm1n_acc3ss}" 

@app.route("/") 
def home(): 
    return "Go to /login"
@app.route("/login") 
def login(): 
    token = jwt.encode({"user": "admin"}, SECRET, algorithm="HS256") 
    return jsonify({"token": token}) 
@app.route("/admin") 
def admin(): 
    token = request.headers.get("Authorization") 
    try:
        data = jwt.decode(token, SECRET, algorithms=["HS256"],options={"verify_signature": False}) 
        if data.get("user") == "admin": 
            return FLAG 
        else: 
            return "Not admin" 
    except: 
        return "Invalid token" 
    
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)