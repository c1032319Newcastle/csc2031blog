from flask import Flask
import secrets

app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
from main.views import main_blueprint
app.register_blueprint(main_blueprint)

from blog.views import blog_blueprint
app.register_blueprint(blog_blueprint)

from users.views import users_blueprint
app.register_blueprint(users_blueprint)
app.config['SECRET_KEY'] = secrets.token_hex(16)


if __name__ == '__main__':
    app.run()
