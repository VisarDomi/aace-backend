from werkzeug.exceptions import Conflict, NotFound, Unauthorized, BadRequest


class JSONException(Exception):
    status_code = NotFound.code
    message = ""

    def __init__(self, message=None, status_code=None):
        Exception.__init__(self)
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return {
            "error": {
                "code": self.status_code,
                "message": self.message,
                "type": str(self.__class__.__name__),
            }
        }


class InvalidContentType(JSONException):
    pass


class InvalidPermissions(JSONException):
    status_code = Unauthorized.code


class InvalidAPIRequest(JSONException):
    pass


class DatabaseError(JSONException):
    pass


class RecordNotFound(DatabaseError):

    pass


class RecordAlreadyExists(DatabaseError):
    status_code = Conflict.code


class MissingArguments(Exception):
    status_code = BadRequest.code


class CannotChangeOthersProfile(InvalidPermissions):
    pass


class CannotDeleteOthersProfile(InvalidPermissions):
    pass


class YouAreNotAdmin(InvalidPermissions):
    pass


class CannotChangeFirstAdminProperties(InvalidPermissions):
    pass


class CannotDeleteFirstAdmin(InvalidPermissions):
    pass


class ThereIsAlreadyAGroupByThatName(RecordAlreadyExists):
    pass


class UserIsAlreadyPartOfGroup(RecordAlreadyExists):
    pass


class NoUserByThatID(RecordNotFound):
    pass


class OrganizationGroupIsAlreadyPartOfGroup(RecordAlreadyExists):
    pass


class NoOrganizationGroupByThatID(RecordNotFound):
    pass


class NoPostByThatID(RecordNotFound):
    pass


class InvalidURL(InvalidAPIRequest):
    pass


class TypeErrorFlusk(InvalidAPIRequest):
    status_code = BadRequest.code
    pass


class CannotPostOnOthersProfile(InvalidPermissions):
    pass


class CannotDeleteOthersPost(InvalidPermissions):
    pass


class CannotNotificationOnOthersProfile(InvalidPermissions):
    pass


class CannotMessageOnOthersProfile(InvalidPermissions):
    pass


class CannotEventOnOthersProfile(InvalidPermissions):
    pass


class CannotCommentOnOthersProfile(InvalidPermissions):
    pass


class PostIsAlreadyPartOfEvent(RecordAlreadyExists):
    pass


class CannotDeleteOthersExperience(InvalidPermissions):
    pass


class CannotDeleteOthersEducation(InvalidPermissions):
    pass


class CannotDeleteOthersSkill(InvalidPermissions):
    pass


class CannotDeleteOthersMedia(InvalidPermissions):
    pass


class CannotGetOthersMedia(InvalidPermissions):
    pass
