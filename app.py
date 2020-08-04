from flask import Flask, request, jsonify  # импортируем из библиотеки flask класс Flask

app = Flask(__name__)  # создаем объект app на основе класса Flask, (__name__) - имя нашего файла

# use Python Dict as DB
storage = dict()
# structure of storage: key - username, value - dict(default empty) in future will contain info about current user


# put some default users into db
storage.update(
    {
        "username1": {},
        "username2": {},
        "username3": {},
        "username4": {}
    }
)


@app.route('/')  # отслеживает URL ('/') - main page)
def hello_world():
    return 'Hello, World!'


@app.route('/users/list/')
def user_list():
    username_list = storage.keys()
    return '<br>'.join(username_list)


@app.route('/users/delete/<username>')
def delete_user(username):
    old_users = storage.copy()
    storage.pop(username, False)
    if username in old_users:
        return 'User  was deleted'
    else:
        return 'User doesn`t exist or already deleted'


# 2) Заменяем в текущей реализации ответ со строки в JSON с помощью jsonify
@app.route('/users/add/<username>', methods=["POST", "GET"])
def add_user_list():
    data = request.get_json()  # get json return dict loaded from json body
    try:
        username = data['username']
    except Exception as e:
        response = {'msg': f'The field {e} is required'}
        username = False

    if username:
        storage[username] = dict()
        response = {'msg': 'user was added'}
    return jsonify(response)


if __name__ == '__main__':
    app.debug = True
    app.run()
