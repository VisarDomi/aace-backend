from ..common.models import User


def search_users(search_user_data):
    print("search_user_data: ",search_user_data)
    fname = search_user_data["fname"]
    lname = search_user_data["lname"]
    looking_for_fname = '%{0}%'.format(fname)
    looking_for_lname = '%{0}%'.format(lname)
    users = User.query.filter(
        User.first_name.ilike(looking_for_fname)
        & User.last_name.ilike(looking_for_lname)
    ).all()
    # users=[]

    return users
