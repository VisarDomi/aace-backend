from . import backend


def download_communication(media_communication_id):
    return backend.download_communication(media_communication_id)


def download_comment(media_comment_id):
    return backend.download_comment(media_comment_id)
