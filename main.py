from flask import Flask

from controllers.search_controller import search_routes

app = Flask(__name__)

app.register_blueprint(search_routes)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5111)
