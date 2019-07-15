from flask import request

from ..common.validation import schema
from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("/communication/<communication_id>", methods=["POST"])
@schema("create_communication_comment.json")
@token_auth.login_required
def create_communication_comment(communication_id):
    return domain.create_communication_comment(request.json, communication_id)


@bp.route("/<comment_id>/communication/<communication_id>", methods=["GET"])
@token_auth.login_required
def get_communication_comment(communication_id, comment_id):

    return domain.get_communication_comment(communication_id, comment_id)


@bp.route("/all/communication/<communication_id>", methods=["GET"])
@token_auth.login_required
def get_communication_comments(communication_id):

    return domain.get_communication_comments(communication_id)


# order is route, schema, auth
@bp.route("/<comment_id>/communication/<communication_id>", methods=["PUT"])
@schema("/update_communication_comment.json")
@token_auth.login_required
def update_communication_comment(communication_id, comment_id):

    return domain.update_communication_comment(
        request.json, communication_id, comment_id
    )


@bp.route("/<comment_id>/communication/<communication_id>", methods=["DELETE"])
@token_auth.login_required
def delete_communication_comment(communication_id, comment_id):
    domain.delete_communication_comment(communication_id, comment_id)

    return {"message": "Comment with `id: %s` has been deleted." % comment_id}


@bp.route("/event/<event_id>", methods=["POST"])
@schema("create_event_comment.json")
@token_auth.login_required
def create_event_comment(event_id):
    return domain.create_event_comment(request.json, event_id)


@bp.route("/<comment_id>/event/<event_id>", methods=["GET"])
@token_auth.login_required
def get_event_comment(event_id, comment_id):

    return domain.get_event_comment(event_id, comment_id)


@bp.route("/all/event/<event_id>", methods=["GET"])
@token_auth.login_required
def get_event_comments(event_id):

    return domain.get_event_comments(event_id)


# order is route, schema, auth
@bp.route("/<comment_id>/event/<event_id>", methods=["PUT"])
@schema("/update_event_comment.json")
@token_auth.login_required
def update_event_comment(event_id, comment_id):

    return domain.update_event_comment(request.json, event_id, comment_id)


@bp.route("/<comment_id>/event/<event_id>", methods=["DELETE"])
@token_auth.login_required
def delete_event_comment(event_id, comment_id):
    domain.delete_event_comment(event_id, comment_id)

    return {"message": "Comment with `id: %s` has been deleted." % comment_id}


@bp.route("/poll/<poll_id>", methods=["POST"])
@schema("create_poll_comment.json")
@token_auth.login_required
def create_poll_comment(poll_id):
    return domain.create_poll_comment(request.json, poll_id)


@bp.route("/<comment_id>/poll/<poll_id>", methods=["GET"])
@token_auth.login_required
def get_poll_comment(poll_id, comment_id):

    return domain.get_poll_comment(poll_id, comment_id)


@bp.route("/all/poll/<poll_id>", methods=["GET"])
@token_auth.login_required
def get_poll_comments(poll_id):

    return domain.get_poll_comments(poll_id)


# order is route, schema, auth
@bp.route("/<comment_id>/poll/<poll_id>", methods=["PUT"])
@schema("/update_poll_comment.json")
@token_auth.login_required
def update_poll_comment(poll_id, comment_id):

    return domain.update_poll_comment(request.json, poll_id, comment_id)


@bp.route("/<comment_id>/poll/<poll_id>", methods=["DELETE"])
@token_auth.login_required
def delete_poll_comment(poll_id, comment_id):
    domain.delete_poll_comment(poll_id, comment_id)

    return {"message": "Comment with `id: %s` has been deleted." % comment_id}
