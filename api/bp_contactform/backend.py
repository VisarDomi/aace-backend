from ..models.items import ContactForm
from ..helper_functions.get_by_id import (
    get_contactform_by_id,
)
from ..helper_functions.decorators import admin_required


def create_contactform(contactform_data):
    contactform = ContactForm(**contactform_data)
    contactform.save()

    return contactform


@admin_required
def get_contactforms():
    contactforms = ContactForm.query.all()

    return contactforms


@admin_required
def delete_contactform(contactform_id):
    contactform = get_contactform_by_id(contactform_id)
    contactform.delete()
