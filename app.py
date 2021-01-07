from chalice import Chalice, Response, BadRequestError, NotFoundError
from marshmallow import ValidationError

from todos.models import Todo
from todos.serializers import TodoSerializer


app = Chalice(app_name='todo-chalice')


def _get_todo_instance(todo_id):
    try:
        return Todo.get(todo_id)

    except Todo.DoesNotExist as err:
        raise NotFoundError(err) from err


@app.route('/todos')
def get_todos():
    schema = TodoSerializer()
    return [schema.dump(todo) for todo in Todo.scan()]


@app.route('/todos/{todo_id}')
def get_todo(todo_id):
    schema = TodoSerializer()
    todo = _get_todo_instance(todo_id)

    return schema.dump(todo)


@app.route('/todos', methods=['POST'])
def add_todo():
    data = app.current_request.json_body
    schema = TodoSerializer()

    try:
        validated_data = schema.load(data)

    except ValidationError as err:
        raise BadRequestError(err.messages) from err

    todo = Todo(**validated_data)
    todo.save()

    return schema.dump(todo)


@app.route('/todos/{todo_id}', methods=['PUT', 'PATCH'])
def update_todo(todo_id):
    schema = TodoSerializer()
    data = app.current_request.json_body
    todo = _get_todo_instance(todo_id)

    try:
        validated_data = schema.load(data, partial=True)

    except ValidationError as err:
        raise BadRequestError(err.messages) from err

    for field, value in validated_data.items():
        setattr(todo, field, value)
    todo.save()

    return schema.dump(todo)


@app.route('/todos/{todo_id}', methods=['DELETE'])
def delete_todo(todo_id):
    todo = _get_todo_instance(todo_id)
    todo.delete()

    return Response(body='', status_code=204)
