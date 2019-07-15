from . import backend
from ..helper_functions.get_by_id import get_poll_by_id


def create_poll(poll_data):
    poll = backend.create_poll(poll_data)
    poll_dict = poll.to_dict()

    return poll_dict


def get_polls():
    polls = backend.get_polls()
    polls_list = []
    for poll in polls:
        poll_dict = poll.to_dict()
        poll_dict["options"] = []
        for option in poll.options.all():
            option_dict = option.to_dict()
            option_dict["votes"] = option.users.count()
            poll_dict["options"].append(option_dict)
        polls_list.append(poll_dict)

    return polls_list


def get_poll(poll_id):
    poll = get_poll_by_id(poll_id)
    poll_dict = poll.to_dict()

    poll_medias = []
    poll_dict["options"] = []
    for option in poll.options.all():
        option_dict = option.to_dict()
        option_dict["votes"] = option.users.count()
        poll_dict["options"].append(option_dict)
    for poll_media in poll.medias:
        poll_medias.append(poll_media.to_dict())
    poll_dict["poll_medias"] = poll_medias

    return poll_dict


def update_poll(poll_data, poll_id):
    poll = backend.update_poll(poll_data, poll_id)
    poll_dict = poll.to_dict()

    return poll_dict


def update_poll_vote(poll_data, poll_id):
    poll = backend.update_poll_vote(poll_data, poll_id)
    poll_dict = poll.to_dict()

    return poll_dict


def delete_poll(poll_id):
    backend.delete_poll(poll_id)


def get_organizationgroups_from_poll(poll_id):
    organizationgroups = backend.get_organizationgroups_from_poll(poll_id)

    organizationgroups_list = [
        organizationgroup.to_dict() for organizationgroup in organizationgroups
    ]

    return organizationgroups_list


def add_organizationgroup_to_poll(poll_id, organizationgroup_id):
    poll = backend.add_organizationgroup_to_poll(poll_id, organizationgroup_id)
    poll_dict = poll.to_dict()

    return poll_dict


def remove_organizationgroup_from_poll(poll_id, organizationgroup_id):
    backend.remove_organizationgroup_from_poll(poll_id, organizationgroup_id)


def send_email(poll_id):
    backend.send_email(poll_id)
