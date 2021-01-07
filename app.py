from chalice import Chalice, BadRequestError, NotFoundError
from marshmallow import ValidationError

from todos.models import Todo
from todos.serializers import TodoSerializer


app = Chalice(app_name='todo-chalice')


@app.route('/todos')
def get_todos():
    return [todo for todo in Todo.scan()]


@app.route('/todos/{todo_id}')
def get_todo(todo_id):
    return Todo.query(todo_id)


@app.route('/todos', methods=['POST'])
def add_todo():
    data = app.current_request.json_body

    try:
        result = TodoSerializer().load(data)

    except ValidationError as err:
        raise BadRequestError(err.messages) from err

    todo = Todo(**result)
    todo.save()

    return todo


@app.route('/todos/{todo_id}', methods=['PUT', 'PATCH'])
def update_todo(todo_id):
    return


@app.route('/todos/{todo_id}', methods=['DELETE'])
def delete_todo(todo_id):
    return
