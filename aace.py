import os

from werkzeug.contrib.fixers import ProxyFix

from api import create_app

from api.common.database import db_session, drop_db
from api.common.models import (
    User,
    Experience,
    Education,
    Accomplishment,
    Media,
    Group,
    Event,
    Post,
    Comment,
    Message,
    MessageRecipient,
    MessageGroup,
    Notification,
)

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        "db_session": db_session,
        "drop_db": drop_db,
        "User": User,
        "Experience": Experience,
        "Education": Education,
        "Accomplishment": Accomplishment,
        "Media": Media,
        "Group": Group,
        "Event": Event,
        "Post": Post,
        "Comment": Comment,
        "Message": Message,
        "MessageRecipient": MessageRecipient,
        "MessageGroup": MessageGroup,
        "Notification": Notification,
    }


def run():
    # debug = os.environ.get('APP_DEBUG', True)
    host = os.environ.get("APP_HOST", "0.0.0.0")
    port = int(os.environ.get("APP_PORT", 8000))

    # app.run(debug=debug, host=host, port=port)
    app.run(host=host, port=port)


wsgi = ProxyFix(app.wsgi_app)


if __name__ == "__main__":
    run()
