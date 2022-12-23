import db.database_api as db


__database_path = 'db/database.db'


def get_quote():
    query = """
        SELECT * FROM quote
        ORDER BY RANDOM()
        LIMIT 1
        """
    args = ()
    data = db.fetch_data(__database_path, query, args)
    return data


def add_quote(quote) -> None:
    args = (quote['author'], quote['quote'])
    query = ("insert into quote(auteur, quote) "
             "values(?, ?)")
    db.insert_data(__database_path, query, args)
