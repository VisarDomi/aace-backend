from flask import g
from ..common.exceptions import (
    OrganizationGroupIsAlreadyPartOfGroup,
    NoOrganizationGroupByThatID,
    UserHasAlreadyVoted,
)
from ..models.items import Poll, OrganizationGroup, Option
from ..bp_media_poll.backend import get_medias, delete_media
from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import get_poll_by_id, get_organizationgroup_by_id
# from ..helper_functions.email import send_email_to_users


@admin_required
def create_poll(poll_data):
    options_data = poll_data.pop("options")
    poll = Poll(**poll_data)
    poll.save()
    for option_data in options_data:
        option = Option(**option_data)
        option.poll = poll
        option.save()
    poll.author = g.current_user
    poll.save()

    return poll


def get_polls():
    polls = Poll.query.all()
    allowed_polls = []
    if g.current_user.role == "admin":
        allowed_polls = polls
    else:
        for poll in polls:
            for group in poll.organizationgroups.all():
                if g.current_user in group.users.all():
                    allowed_polls.append(poll)

    return allowed_polls


@admin_required
def update_poll(poll_data, poll_id):
    poll = get_poll_by_id(poll_id)
    # needs further development
    # poll.update(**poll_data)
    # poll.save()

    return poll


def update_poll_vote(poll_data, poll_id):
    poll = get_poll_by_id(poll_id)
    user = g.current_user
    incoming_options = poll_data.pop("options")
    poll_options = poll.options.all()
    for option in poll_options:
        if user in option.users.all():

            msg = f"User with id `{user.id}` has already voted"
            f" in the poll with id `{poll.id}`"
            raise UserHasAlreadyVoted(message=msg)
    for incoming_option in incoming_options:

        for option in poll_options:
            incoming_body = incoming_option["body"]
            option_dict = option.to_dict()
            body = option_dict["body"]
            if incoming_body == body:
                option.users.append(user)
                option.save()

    return poll


@admin_required
def delete_poll(poll_id):
    for media in get_medias(poll_id):
        delete_media(media.id)
    poll = get_poll_by_id(poll_id)
    poll.delete()


# Getting, adding, removing group from poll


def get_organizationgroups_from_poll(poll_id):
    poll = get_poll_by_id(poll_id)
    organizationgroups = poll.organizationgroups.all()

    return organizationgroups


def filter_og_of_oc(poll, organizationgroup_id, OrganizationGroup):
    """Filter organizationgroups of poll"""
    is_og_in_oc = poll.organizationgroups.filter(
        OrganizationGroup.id == organizationgroup_id
    ).one_or_none()

    return is_og_in_oc


def group_in_poll_or_none(
    organizationgroup, poll, organizationgroup_id, OrganizationGroup
):
    group_or_none = organizationgroup == filter_og_of_oc(
        poll, organizationgroup_id, OrganizationGroup
    )

    return group_or_none


def is_group_in_poll(organizationgroup, poll, organizationgroup_id, OrganizationGroup):
    organizationgroup_in_a_poll = None
    if group_in_poll_or_none(
        organizationgroup, poll, organizationgroup_id, OrganizationGroup
    ):
        organizationgroup_in_a_poll = organizationgroup

    return organizationgroup_in_a_poll


@admin_required
def add_organizationgroup_to_poll(poll_id, organizationgroup_id):
    organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
    poll = get_poll_by_id(poll_id)
    organizationgroup_in_a_poll_or_none = is_group_in_poll(
        organizationgroup, poll, organizationgroup_id, OrganizationGroup
    )
    if organizationgroup is not organizationgroup_in_a_poll_or_none:
        poll = get_poll_by_id(poll_id)
        poll.organizationgroups.append(organizationgroup)
        poll.save()
    else:
        msg = "OrganizationGroup % s is already part of the poll % s." % (
            organizationgroup_id,
            poll_id,
        )
        raise OrganizationGroupIsAlreadyPartOfGroup(message=msg)

    return poll


@admin_required
def remove_organizationgroup_from_poll(poll_id, organizationgroup_id):
    poll = get_poll_by_id(poll_id)
    organizationgroup = poll.organizationgroups.filter(
        OrganizationGroup.id == organizationgroup_id
    ).one_or_none()
    if organizationgroup is not None:
        organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
        poll.organizationgroups.remove(organizationgroup)
        poll.save()
    else:
        msg = (
            f"OrganizationGroup with `id: {organizationgroup_id}` is not part "
            f"of the poll with `id {poll_id}`."
        )
        raise NoOrganizationGroupByThatID(message=msg)


@admin_required
def send_email(poll_id):
    # send_email_to_users(poll_id) doesn't work
    print("poll_id", poll_id)
