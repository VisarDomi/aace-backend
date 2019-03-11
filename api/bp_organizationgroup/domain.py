from . import backend


def create_organizationgroup(organizationgroup_data):
    organizationgroup = backend.create_organizationgroup(organizationgroup_data)
    organizationgroup_dict = organizationgroup.to_dict()

    return organizationgroup_dict


def get_organizationgroup_by_id(organizationgroup_id):
    organizationgroup = backend.get_organizationgroup_by_id(organizationgroup_id)
    organizationgroup_dict = organizationgroup.to_dict()

    return organizationgroup_dict


def get_all_organizationgroups():
    organizationgroups = backend.get_all_organizationgroups()
    organizationgroups_list = [
        organizationgroup.to_dict() for organizationgroup in organizationgroups
    ]

    return organizationgroups_list


def update_organizationgroup(organizationgroup_data, organizationgroup_id):
    organizationgroup = backend.update_organizationgroup(
        organizationgroup_data, organizationgroup_id
    )
    organizationgroup_dict = organizationgroup.to_dict()

    return organizationgroup_dict


def delete_organizationgroup(organizationgroup_id):
    backend.delete_organizationgroup(organizationgroup_id)


def get_users_from_organizationgroup(organizationgroup_id):
    users = backend.get_users_from_organizationgroup(organizationgroup_id)
    ONLY = [
        "register_status",
        "application_date",
        "id",
        "first_name",
        "last_name",
        "profession",
        "sex",
        "summary",
        "country",
        "email",
        "phone",
        "address",
        "birthday",
        "website",
        "comment_from_administrator",
    ]
    users_list = [user.to_dict(only=ONLY) for user in users]

    return users_list


def add_user_to_organizationgroup(organizationgroup_id, user_id):
    organizationgroup = backend.add_user_to_organizationgroup(
        organizationgroup_id, user_id
    )
    organizationgroup_dict = organizationgroup.to_dict()

    return organizationgroup_dict


def remove_user_from_organizationgroup(organizationgroup_id, user_id):
    backend.remove_user_from_organizationgroup(organizationgroup_id, user_id)


def add_users_to_organizationgroup(user_data_ids, organizationgroup_id):
    organizationgroup = backend.add_users_to_organizationgroup(
        user_data_ids, organizationgroup_id
    )
    organizationgroup_dict = organizationgroup.to_dict()

    return organizationgroup_dict


def remove_users_from_organizationgroup(user_data_ids, organizationgroup_id):
    backend.remove_users_from_organizationgroup(user_data_ids, organizationgroup_id)
