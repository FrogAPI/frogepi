from datetime import datetime
from pydantic import BaseModel
from pydantic import ValidationError
import usecase
from flask import request, make_response, render_template
import logging
from db.checkkey import validkey

from antibrute import addf_verifBrute


logging.basicConfig(handlers=[logging.FileHandler(filename="./records.log",
                                                  encoding='UTF-8', mode='a+')],
                    format="%(asctime)s: %(message)s")

""" END POINTS """

def get_doc():
    return render_template("doc.html")


def hello():
    return 'Archy is best discord bot ever!'


def get_quote():
    """ endpoint for fecthing a random quote """

    want_wens = request.args.get('wantwens')
    if __isMercredi() and want_wens == "true":
        resp_body = {'author': "Archy",
                     'quote': "It is wednesday, my dudes!"}
        resp_code = 200
        return __http_response(resp_body, resp_code)
    return __get_quote()


def add_quote():
    """ endpoint for insert quote in database """

    api_key = request.args.get('key')
    if not validkey(api_key):
        addf_verifBrute()
        return __http_response(
            {"message": "You Wish! YOU INSOLENT FOOL! Wrong! Who even are you?"},
            403
        )

    payload = request.json

    if not __valid(payload):
        return __http_response(
            {"message": "How dare you! YOU INSOLENT FOOL!"},
            400
        )

    return __add_quote(payload)


""" PRIVATES """


class __Quote(BaseModel):
    quote: str
    author: str


def __add_quote(payload):
    try:
        usecase.add_quote(payload)
    except Exception as err:
        logging.error(err)
        return __http_response(
            {"message": "We fucked up !"},
            500
        )

    return __http_response(
        {"message": "Successfully added !"},
        201
    )


def __get_quote():
    """ endpoint for fetching random quote in database """

    try:
        quote = usecase.get_quote()[0]
        resp_body = {'author':  quote[1], 'quote': quote[2]}
        resp_code = 200
    except Exception as err:
        logging.info(err)
        resp_body = {'author': "Archy",
                     'quote': "404 - Cat not found - :frogesad:"}
        resp_code = 404

    return __http_response(resp_body, resp_code)


def __valid(payload):
    """ if payload is validate return True else False """
    try:
        # Try to create a Quote, (uses pydantic validation)
        __Quote(**payload)
        isValid = True

    except ValidationError as err:
        logging.warning(err)
        isValid = False


    return isValid


def __http_response(resp_body, resp_code):
    response = make_response(resp_body, resp_code)
    response.headers.set("Content-Type", "application/json")
    return response


def __isMercredi():
    return datetime.today().weekday() == 2
