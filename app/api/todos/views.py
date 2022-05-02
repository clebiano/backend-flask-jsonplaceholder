from flask import Blueprint, request
from flask_httpauth import HTTPTokenAuth
from services.todos import TodoService

blueprint = Blueprint('todos', __name__)
auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    "secret-token-test-1": "john",
    "secret-token-test-2": "susan"
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]


@blueprint.route('/todos', methods=['GET'])
@auth.login_required
def todo_tasks():
    if request.method == "GET":
        size = int(request.args.get("size")) if request.args.get("size") else None
        return TodoService().get_n_todos(size)
