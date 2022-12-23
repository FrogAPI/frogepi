# script python pour set up les bases de données

import sqlite3

try:
    connection = sqlite3.connect('db/database.db')
    cursor = connection.cursor()
    cursor.execute(
        """
        create table quote(
        id integer primary key,
        auteur varchar(50),
        quote varchar(500),
        UNIQUE (auteur) ON CONFLICT IGNORE
        );
        """

    )
    connection.commit()

    cursor.close()
    connection.close()
except:
    print("déjà set up")


try:
    connection1 = sqlite3.connect('db/key.db')
    cursor1 = connection1.cursor()
    cursor1.execute(
        """
        create table apikey(
        id integer primary key,
        hashing varchar(64),
        UNIQUE (hashing) ON CONFLICT IGNORE
        );
        """
    )
    connection1.commit()

    cursor1.close()
    connection1.close()
except:
    print("déjà set up")