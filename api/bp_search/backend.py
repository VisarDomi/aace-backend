from ..common.models.users import User
from ..common.exceptions import NotFound


def search_users(search_user_data):
    print("search_user_data :", search_user_data)
    first_name = None
    last_name = None
    users = []
    try:
        name = search_user_data["name"]
        print("name :", name)
    except KeyError:
        msg = f"The keys first_name and last_name are not found."
        raise NotFound(message=msg)
    accepted_members_query = User.query.filter(User.application_status == "accepted")

    if not name:
        users = accepted_members_query.all()
    names = name.split(" ")
    if len(names) == 1:
        first_name = names.pop(0)
        print("first_name :", first_name)
    elif len(names) == 2:
        first_name = names.pop(0)
        last_name = names.pop(0)

    looking_for_first_name = "%{0}%".format(first_name)
    looking_for_last_name = "%{0}%".format(last_name)
    print("looking_for_first_name :", looking_for_first_name)
    print("looking_for_last_name :", looking_for_last_name)
    if first_name and not last_name:
        fname = first_name
        lname = first_name
        looking_for_first_name = "%{0}%".format(fname)
        looking_for_last_name = "%{0}%".format(lname)
        users = accepted_members_query.filter(
            (User.first_name.ilike(looking_for_first_name))
            | (User.last_name.ilike(looking_for_last_name))
        ).all()
    elif first_name and last_name:
        looking_for_last_name = "%{0}%".format(last_name)
        users = accepted_members_query.filter(
            (User.first_name.ilike(looking_for_first_name))
            & (User.last_name.ilike(looking_for_last_name))
        ).all()

    return users
