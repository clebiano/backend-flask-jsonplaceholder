from . import todos


def register_blueprints(app):
    app.register_blueprint(todos.blueprint)
