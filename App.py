from flask import Flask, request, jsonify 
app = Flask(__name__) 
@app.route("/") 
def home(): 
 return "Hello, Flask!" 

@app.route("/users", methods=["POST"]) 
def create_user(): 
   return "Utilisateur créé" 

@app.route("/users") 
def get_users(): 
 return "Liste des utilisateurs" 

@app.route("/data", methods=["POST"]) 
def receive_data(): 
  content = request.json 
  return jsonify({ 
    "message": "Données reçues", 
    "data": content 
    }), 201 

if __name__ == "__main__": 
 app.run(debug=True)