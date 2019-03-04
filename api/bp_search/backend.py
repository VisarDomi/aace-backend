from ..common.models import User


def search_users(search_user_data):
    print("search_user_data['fname'] :", search_user_data["fname"])
    fname = search_user_data["fname"]
    lname = search_user_data["lname"]
    users = User.query.filter(
        User.first_name.contains(fname) & User.last_name.contains(lname)
    ).all()

    return users
