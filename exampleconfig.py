from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 16173725
    API_HASH = "eb5276af00094ecb815e25aaf2901fcf"
    # the name to display in your alive message
    ALIVE_NAME = "MeTi"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://awvcjalw:yFCXC5vHmKVuZ8zDCvPS-fDScuw36zAG@tai.db.elephantsql.com/awvcjalw"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1AZWarzgBuwlw8yEsVVkcz5FVBnWwsCirZStAfe2jfBqpyMJYjhSVQz_NPEXf47riEOl2QCjUxyNZFieKPkXooBr2h7IX7Hsc-gVI-otAYwNGqD78MQ7dSd1ER1mXTOLUGYZ0j1TK4F3ciG90nvCSOtLK-ll6ajPMZgOl1edTpUBNlZPnTtd9jisoMs56sIQqI2MPxFgNo4uhaKPfkVRYzXHxwmCfMjkYcHhGmJr5VNa2aPw8Oz8v-3WupjQweJLyl19bix129dvZDX2LOhetpgN3kkSFINVn5XJQTn5AVOLjKVH8JmiRKz1ca_4c-5C2EWax5lTMg-4KYUUWSK0DVDfIKj-iah4="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6392494107:AAE2gp9gZXQONNWzXA4cRJB9XF6wVpfiU-Y"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1004042310398
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/arbabmahdi/catuserboT"
    # if you need badcat plugins set "True"
    BADCAT = "True"
