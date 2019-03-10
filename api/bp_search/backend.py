from ..common.models import User
from ..common.exceptions import NotFound


def search_users(search_user_data):
    fname = None
    lname = None
    users = []
    try:
        name = search_user_data["name"]
    except KeyError:
        msg = f"The keys fname and lname are not found."
        raise NotFound(message=msg)
    accepted_members_query = User.query.filter(User.register_status == "accepted")

    if not name:
        users = accepted_members_query.all()
    names = name.split(" ")
    if len(names) == 1:
        fname = names.pop(0)
    elif len(names) == 2:
        fname = names.pop(0)
        lname = names.pop(0)

    looking_for_fname = "%{0}%".format(fname)
    if fname and not lname:
        looking_for_lname = "%{0}%".format(lname)
        users = accepted_members_query.filter(
            User.first_name.ilike(looking_for_fname)
        ).all()
    elif fname and lname:
        looking_for_lname = "%{0}%".format(lname)
        users = accepted_members_query.filter(
            User.first_name.ilike(looking_for_fname)
            & User.last_name.ilike(looking_for_lname)
        ).all()

    return users
