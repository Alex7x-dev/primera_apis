from flask import Flask, request, jsonify


app = Flask(__name__)
allUsers = []                   
user_new_get = []

@app.route('/app/v1/users/<id>', methods=['GET', 'DELETE'])   
def user_action(id):
    if request.method == 'GET':
        for user in allUsers:
            if user.get('id') == id:
                user_new_get = user
                return user_new_get
        for user in allUsers:
            if user.get('id') != id:
                return jsonify({'error_message': 'usuario no valido'}), 404
    else: ##
        user_found = None
        for user in allUsers:
            if user.get('id') == id:
                user_found = user
                break
            
        if user_found:
            allUsers.remove(user_found)
            return jsonify(user_found)
        else:
            return jsonify({'error_message': 'usuario no valido'}), 404
        
@app.route('/app/v1/users', methods=['GET', 'POST'])
def user_action_add():
    if request.method == 'GET':
        print(jsonify(allUsers))
        return jsonify(allUsers)
    else:
        user = {'id': request.form['id'], 'nombre': request.form['nombre']}
        if user.get('id') and user.get('nombre'):                         
            allUsers.append(user)
            return jsonify(user)
        else:
            return 'usuario no valido', 400


app.run(debug=True) 






