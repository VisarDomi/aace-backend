from . import backend
from ..helper_functions.get_by_id import get_contactform_by_id
from ..helper_functions.decorators import admin_required


def create_contactform(contactform_data):
    contactform = backend.create_contactform(contactform_data)
    contactform_dict = contactform.to_dict()

    return contactform_dict


def get_contactforms():
    contactforms = backend.get_contactforms()
    contactforms_list = []
    for contactform in contactforms:
        contactform_dict = contactform.to_dict()
        contactforms_list += [contactform_dict]

    return contactforms_list


@admin_required
def get_contactform(contactform_id):
    contactform = get_contactform_by_id(contactform_id)
    contactform_dict = contactform.to_dict()

    return contactform_dict


def delete_contactform(contactform_id):
    backend.delete_contactform(contactform_id)
