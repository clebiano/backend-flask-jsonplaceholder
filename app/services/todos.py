import requests


class TodoService:
    def get_n_todos(self, size: int):
        response = {"items": []}

        try:
            todo_list = requests.get('https://jsonplaceholder.typicode.com/todos').json()[:size]
        except:
            raise Exception()

        for todo in todo_list:
            response["items"].append(
                {
                    "id": todo["id"],
                    "title": todo["title"]
                }
            )

        return response
