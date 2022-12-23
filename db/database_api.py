import sqlite3


def fetch_data(path, query, args):
    """ get data by query """
    connection = __get_connection(path)
    cursor = connection.cursor()
    cursor.execute(query, args)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def insert_data(path, query, args):
    """ Add data to the database """
    connection = __get_connection(path)
    connection.execute(query, args)
    connection.commit()
    connection.close()


def __get_connection(path: str):
    connection = sqlite3.connect(
        path)
    return connection