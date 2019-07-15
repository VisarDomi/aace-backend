import os

from werkzeug.contrib.fixers import ProxyFix

from api import create_app

from api.common.database import db_session, drop_db, init_db
from api.models.users import User
from api.models.items import (
    Education,
    Experience,
    Skill,
    Group,
    Comment,
    Option,
    Communication,
    Event,
    Poll,
    OrganizationGroup,
)
from api.models.medias import (
    MediaUser,
    MediaEducation,
    MediaExperience,
    MediaSkill,
    MediaComment,
    MediaCommunication,
    MediaEvent,
    MediaPoll,
    MediaOrganizationGroup,
)

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
        "Comment": Comment,
        "Option": Option,
        "Communication": Communication,
        "Event": Event,
        "Poll": Poll,
        "OrganizationGroup": OrganizationGroup,
        "MediaUser": MediaUser,
        "MediaEducation": MediaEducation,
        "MediaExperience": MediaExperience,
        "MediaSkill": MediaSkill,
        "MediaComment": MediaComment,
        "MediaCommunication": MediaCommunication,
        "MediaEvent": MediaEvent,
        "MediaPoll": MediaPoll,
        "MediaOrganizationGroup": MediaOrganizationGroup,
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
