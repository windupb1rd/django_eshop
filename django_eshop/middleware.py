from django.db import connection


class SqlViewer:
    """
    Обработчик, выводящий в консоль SQL-запрос и время выполнения запроса
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if connection.queries:
            query_to_database = connection.queries
            print(f"SQL - запрос: {query_to_database[0]['sql']}",
                  f"Время выполнения: {query_to_database[0]['time']}", sep='\n')

        return response
