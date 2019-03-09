from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..common.models import MediaOrganizationGroup
import os
from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import (
    get_organizationgroup_by_id,
    get_organizationgroup_media_by_id,
)


files_organizationgroup = UploadSet(
    name="organizationgroupfiles", extensions=AllExcept(SCRIPTS + EXECUTABLES)
)


@admin_required
def create_medias(media_data, organizationgroup_id):
    medias = []
    if get_organizationgroup_by_id(organizationgroup_id):
        for file in media_data:
            filename = files_organizationgroup.save(file)
            url = files_organizationgroup.url(filename)
            media = MediaOrganizationGroup(filename=filename, url=url)
            media.organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
            media.save()
            medias.append(media)

    return medias


def get_all_medias(organizationgroup_id):
    medias = MediaOrganizationGroup.query.filter(
        MediaOrganizationGroup.organizationgroup_id == int(organizationgroup_id)
    ).all()

    return medias


@admin_required
def update_media(media_data, organizationgroup_id, media_organizationgroup_id):
    medias = []
    media = MediaOrganizationGroup.query.filter(
        MediaOrganizationGroup.id == media_organizationgroup_id
    ).one_or_none()
    for file in media_data:
        if file and media:
            delete_media(organizationgroup_id, media_organizationgroup_id)
            filename = files_organizationgroup.save(file)
            url = files_organizationgroup.url(filename)
            media = MediaOrganizationGroup(filename=filename, url=url)
            media.organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
            media.save()
            medias.append(media)

    return medias


def get_file_path(file_name):
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
    FILE_TO_PATH = "static/files/organizationgroup"
    file_path = os.path.join(parent_dir, FILE_TO_PATH)
    f_path = os.path.join(file_path, file_name)

    return f_path


def is_file(file_name):
    this_file_path = get_file_path(file_name)

    return os.path.exists(this_file_path)


@admin_required
def delete_media(organizationgroup_id, media_organizationgroup_id):
    media = get_organizationgroup_media_by_id(
        organizationgroup_id, media_organizationgroup_id
    )
    file_name = files_organizationgroup.path(media.filename)
    if is_file(media.filename):
        os.remove(get_file_path(file_name))
    media.delete()
