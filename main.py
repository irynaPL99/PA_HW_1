from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello Flask!'

@app.route('/user/<username>')  # dynamic путь
def show_user_profile(username):
    return f'User {username}'

if __name__ == '__main__':
    app.run()
