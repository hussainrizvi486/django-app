from django.db import connection


def exceute_sql_query(query: str, serialized=True):
    with connection.cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
        columns = cursor.description        
        columns = [col[0] for col in columns]
        rows = [dict(zip(columns, row)) for row in res]

        print(rows)
        return rows
