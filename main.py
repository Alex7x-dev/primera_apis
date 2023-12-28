from flask import Flask, request, jsonify


app = Flask(__name__)
allUsers = []                   #ITERAR
user_new_get = []
# agregar id para acceder a allUsers???
@app.route('/app/v1/users/<id>', methods=['GET', 'DELETE'])   # INCLUIR EL DELETE AQUI
def user_action(id):
    if request.method == 'GET':
        for user in allUsers:
            if user.get('id') == id:
                user_new_get = user
                return user_new_get
        for user in allUsers:
            if user.get('id') != id:
                return 'usuario no valido', 404
    else: ##
        for user in allUsers:
            if user.get('id') == id:
                allUsers.remove(user)
                return jsonify(user)
            else:
                return 'usuario no existe', 404
        # if request.method == 'GET':                               # VALIDAR QUE EL USUARIO EXISTA ANTES DE OBTENER LA INFO O DE BORRARLO, CASO CONTRARIO DEVOLVER 404
    #     return jsonify(allUsers[int(id)])
    # else:
    #     user_del = allUsers[int(id)]
    #     allUsers.remove(user_del)
    #     return jsonify(user_del )
@app.route('/app/v1/users', methods=['GET', 'POST'])
def user_action_add():
    if request.method == 'GET':
        print(jsonify(allUsers))
        return jsonify(allUsers)
    else:
        user = {'id': request.form['id'], 'nombre': request.form['nombre']}
        if user.get('id') and user.get('nombre'):                         # VALIDAR QUE EL FORMULARIO TIENE ID Y TIENE NOMBRE CASO CONTRARIO DEVOLVER 400
            allUsers.append(user)
            return jsonify(user)
        else:
            return 'usuario no valido', 400


app.run(debug=True) #hot_reload






