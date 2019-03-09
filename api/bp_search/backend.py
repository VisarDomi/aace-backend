from ..common.models import User
from ..common.exceptions import NotFound


def search_users(search_user_data):
    print("search_user_data: ", search_user_data)
    try:
        fname = search_user_data["fname"]
        lname = search_user_data["lname"]
    except KeyError:
        msg = f"The keys fname and lname are not found."
        raise NotFound(message=msg)
    looking_for_fname = "%{0}%".format(fname)
    looking_for_lname = "%{0}%".format(lname)
    users = User.query.filter(
        User.first_name.ilike(looking_for_fname)
        & User.last_name.ilike(looking_for_lname)
    ).all()
    # users=[]

    return users
