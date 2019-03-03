from . import backend


def download_education(media_education_id):
    return backend.download_education(media_education_id)


def download_experience(media_experience_id):
    return backend.download_experience(media_experience_id)


def download_skill(media_skill_id):
    return backend.download_skill(media_skill_id)
