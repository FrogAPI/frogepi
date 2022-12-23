# script python pour générer une api key

import string
import random
import sqlite3
from hashlib import sha256

SALT = "johnhadawildcatnamedgeorgesreeeeeeeee312"

letters = string.ascii_lowercase
clef = ''.join(random.choice(letters) for i in range(random.randint(10, 25)))

print(clef)

clef_salt = clef + SALT

res_hash = sha256(clef_salt.encode('utf-8')).hexdigest()

connection = sqlite3.connect('db/key.db')
cursor = connection.cursor()
cursor.execute(
    """
    INSERT INTO apikey (hashing) VALUES (?);
    """, (res_hash, )

)
connection.commit()

cursor.close()
connection.close()
