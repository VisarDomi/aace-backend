from . import backend


def create_user(user_data):
    """Create user.
    :param user_data: user information
    :type user_data: dict
    :returns: serialized user object
    :rtype: dict
    """
    user = backend.create_user(user_data)

    return user.to_dict()


def get_user_by_id(user_id):
    """Get User by id.
    :param user_id: id of the user to be retrived
    :type user_id: integer
    :returns: serialized User object
    :rtype: dict
    """
    user = backend.get_user_by_id(user_id)

    return user.to_dict()


def get_all_users():
    """Get all Users.
    :returns: serialized User objects
    :rtype: list
    """
    users = backend.get_all_users()
    return [
        user.to_dict() for user in users
    ]


def update_user(user_data, user_id):
    """Update User.
    :param user_data: User information
    :type user_data: dict
    :param user_id: id of the User to be updated
    :type user_id: integer
    :returns: serialized User object
    :rtype: dict
    """
    user = backend.update_user(user_data, user_id)

    return user.to_dict()


def delete_user(user_id):
    """Delete User.
    :param user_id: id of the User to be deleted
    :type user_id: integer
    """
    backend.delete_user(user_id)
