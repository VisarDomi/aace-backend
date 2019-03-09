from . import backend


def download_officialcommunication(media_officialcommunication_id):
    return backend.download_officialcommunication(media_officialcommunication_id)


def download_officialcomment(media_officialcomment_id):
    return backend.download_officialcomment(media_officialcomment_id)
