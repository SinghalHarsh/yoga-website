import os
from flask import Flask
from routes.main import main_bp
from routes.pranayama import pranayama_bp

app = Flask(__name__)


@app.context_processor
def inject_site_name():
    return {'site_name': 'Yoga Website'}


app.register_blueprint(main_bp)
app.register_blueprint(pranayama_bp)


if __name__ == '__main__':
    debug = os.environ.get('FLASK_DEBUG', '1') == '1'
    port = int(os.environ.get('PORT', 5002))
    host = os.environ.get('HOST', '0.0.0.0')
    app.run(debug=debug, host=host, port=port)
