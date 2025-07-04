


# from flask import Flask, session, jsonify
# from flask_session import Session
# from flask_cors import CORS
# import os
# import logging
# from logging.handlers import RotatingFileHandler

# # Import Blueprints
# from routes.interview import interview_bp
# from routes.report import report_bp
# from routes.session import session_bp
# from utils.helpers import init_interview_data


# def create_app():
#     app = Flask(__name__)
#     CORS(app, supports_credentials=True, origins=["http://localhost:5173","http://localhost:5174","http://localhost:5172","http://localhost:8080","https://ai-bot-modular.onrender.com"])
#     # ====== Basic Configs ======
#     app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

#     # Session Config
#     app.config['SESSION_TYPE'] = 'filesystem'
#     app.config['SESSION_COOKIE_NAME'] = 'session'
#     session_dir = os.path.join(os.getcwd(), 'flask_session_data')
#     os.makedirs(session_dir, exist_ok=True)
#     app.config['SESSION_FILE_DIR'] = session_dir

#     # Enable Session
#     Session(app)

#     # ====== CORS for React (localhost:3000) ======
#     CORS(app)

#     # ====== Logging ======
#     logs_dir = os.path.join(os.getcwd(), 'logs')
#     os.makedirs(logs_dir, exist_ok=True)
#     log_file = os.path.join(logs_dir, 'interview_app.log')
#     handler = RotatingFileHandler(log_file, maxBytes=10_000_000, backupCount=5)
#     handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
#     app.logger.addHandler(handler)
#     app.logger.setLevel(logging.DEBUG)

#     # ====== Register Blueprints ======
#     app.register_blueprint(interview_bp, url_prefix='/jobs')
#     app.register_blueprint(report_bp, url_prefix='/report')
#     app.register_blueprint(session_bp, url_prefix='/session')

#     # ====== Home Route (for testing connection) ======
#     @app.route('/')
#     def home():
#         app.logger.info("Home API accessed")
#         session.clear()
#         session['interview_data'] = init_interview_data()
#         return jsonify({
#             "message": "API is live",
#             "session": session.get("interview_data", {})
#         })

#     # ====== Error Handler ======
#     @app.errorhandler(404)
#     def not_found(error):
#         return jsonify({"error": "Not Found"}), 404

#     return app


# # Run the Flask app
# if __name__ == '__main__':
#     app = create_app()
#     app.run(host='0.0.0.0', port=5000, debug=True)





from flask import Flask, session, jsonify
from flask_session import Session
from flask_cors import CORS
import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv  # ✅ Load .env file

# Load environment variables BEFORE anything else
load_dotenv()

# Import Blueprints
from routes.interview import interview_bp
from routes.report import report_bp
from routes.session import session_bp
from utils.helpers import init_interview_data
import cohere

from config import Config

co = cohere.Client(Config.COHERE_API_KEY)




def create_app():
    app = Flask(__name__)
  

    # ✅ Only call CORS ONCE, with credentials & proper origins
    CORS(app, supports_credentials=True, origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5172",
        "http://localhost:8080",
        "https://ai-bot-modular.onrender.com"
    ])

    # ====== Basic Configs ======
    app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

    # Session Config
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_COOKIE_NAME'] = 'session'
    session_dir = os.path.join(os.getcwd(), 'flask_session_data')
    os.makedirs(session_dir, exist_ok=True)
    app.config['SESSION_FILE_DIR'] = session_dir
    app.config['SESSION_COOKIE_SAMESITE'] = 'None'  # 👈 Required for cross-site cookies
    app.config['SESSION_COOKIE_SECURE'] = True

    # Enable Session
    Session(app)

    # ====== Logging ======
    logs_dir = os.path.join(os.getcwd(), 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    log_file = os.path.join(logs_dir, 'interview_app.log')
    handler = RotatingFileHandler(log_file, maxBytes=10_000_000, backupCount=5)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

    # ====== Register Blueprints ======
    app.register_blueprint(interview_bp, url_prefix='/jobs')
    app.register_blueprint(report_bp, url_prefix='/report')
    app.register_blueprint(session_bp, url_prefix='/session')

    # ====== Home Route (for testing connection) ======
    @app.route('/')
    def home():
        app.logger.info("Home API accessed")
        session.clear()
        session['interview_data'] = init_interview_data()
        return jsonify({
            "message": "API is live",
            "session": session.get("interview_data", {})
        })

    # ====== Error Handler ======
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not Found"}), 404

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)