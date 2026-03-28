from flask import Flask
from api.routes import api_blueprint
from frontend.views import frontend_blueprint

app = Flask(__name__)

app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(frontend_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)