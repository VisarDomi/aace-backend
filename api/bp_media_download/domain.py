from . import backend


def download_communication(media_communication_id):
    return backend.download_communication(media_communication_id)


def download_event(media_event_id):
    return backend.download_event(media_event_id)


def download_poll(media_poll_id):
    return backend.download_poll(media_poll_id)


def download_comment(media_comment_id):
    return backend.download_comment(media_comment_id)
