import json
import logging
import traceback
from logging.handlers import RotatingFileHandler
from time import strftime

from flask import Flask, Response, request

from api.router import register_blueprints


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    register_blueprints(app)

    @app.after_request
    def after_request(response):
        timestamp = strftime('[%Y-%b-%d %H:%M]')
        logger.error('%s %s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status, response.json)
        return response

    @app.errorhandler(Exception)
    def exceptions(e):
        tb = traceback.format_exc()
        timestamp = strftime('[%Y-%b-%d %H:%M]')
        logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, tb)
        return Response(
            json.dumps({"error": {"reason": str(e)}}, indent=4, sort_keys=True, default=str),
            status=500,
            mimetype="application/json"
        )

    handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=3)
    logger = logging.getLogger('tdm')
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)

    return app


app = create_app()
