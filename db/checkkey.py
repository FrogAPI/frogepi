from hashlib import sha256
import logging
import db.database_api as db
from flask import request


__path__ = "db/key.db"

SALT = "johnhadawildcatnamedgeorgesreeeeeeeee312"


def validkey(key) -> bool:
    clef_salt = str(key) + SALT
    hashedkey = sha256(clef_salt.encode('utf-8')).hexdigest()
    return __is_hash_in_db(hashedkey)


def __is_hash_in_db(hashing):
    try:
        resreq: str = __search_db(hashing)
        return resreq != ""
    except Exception as err:
        string = __build_record_message(err)
        logging.warning(string)
        return False


def __search_db(hashing):
    query = """
            SELECT * FROM apikey
            WHERE hashing = ?
            """
    args = (hashing, )
    return db.fetch_data(__path__, query, args)[0]


def __build_record_message(err):
    s = "BAD API KEY - - "
    s += str(err)
    return s
