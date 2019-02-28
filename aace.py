import os

from werkzeug.contrib.fixers import ProxyFix

from api import create_app

from api.common.database import db_session, drop_db, init_db
from api.common.models import Education, Experience, Group, Media, Skill, User

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        "db_session": db_session,
        "drop_db": drop_db,
        "init_db": init_db,
        "Education": Education,
        "Experience": Experience,
        "Group": Group,
        "Media": Media,
        "Skill": Skill,
        "User": User,
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
