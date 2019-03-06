from flask import request

from ..common.validation import schema
from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_organizationgroup.json")
@token_auth.login_required
def create_organizationgroup():
    return domain.create_organizationgroup(request.json)


@bp.route("/<organizationgroup_id>", methods=["GET"])
def get_organizationgroup(organizationgroup_id):

    return domain.get_organizationgroup_by_id(organizationgroup_id)


@bp.route("/all", methods=["GET"])
def get_organizationgroups():

    return domain.get_all_organizationgroups()


# order is route, schema, auth
@bp.route("/<organizationgroup_id>", methods=["PUT"])
@schema("/update_organizationgroup.json")
@token_auth.login_required
def update_organizationgroup(organizationgroup_id):

    return domain.update_organizationgroup(request.json, organizationgroup_id)


@bp.route("/<organizationgroup_id>", methods=["DELETE"])
@token_auth.login_required
def delete_organizationgroup(organizationgroup_id):
    domain.delete_organizationgroup(organizationgroup_id)

    return {
        "message": "OrganizationGroup with `id: %s` has been deleted."
        % organizationgroup_id
    }
