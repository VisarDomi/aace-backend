#########################################################
#Admin
admin_dict = {
    "email": "admin@aace.al",
    "password": "password"
}
admin_instance = User(**admin_dict)
admin_instance.save()

#########################################################
#Groups
anetaret_dict = {
    "name": "anetaret",
    "description": "anetaret shoqates"
}
anetaret_instance = OrganizationGroup(**anetaret_dict)
anetaret_instance.save()

presidenti_dict = {
    "name": "presidenti",
    "description": "presidenti shoqates"
}
presidenti_instance = OrganizationGroup(**presidenti_dict)
presidenti_instance.save()

sekretari_dict = {
    "name": "sekretari",
    "description": "sekretari shoqates"
}
sekretari_instance = OrganizationGroup(**sekretari_dict)
sekretari_instance.save()

koordinatori_dict = {
    "name": "koordinatori",
    "description": "koordinatori shoqates"
}
koordinatori_instance = OrganizationGroup(**koordinatori_dict)
koordinatori_instance.save()

kryesia_dict = {
    "name": "kryesia",
    "description": "kryesia shoqates"
}
kryesia_instance = OrganizationGroup(**kryesia_dict)
kryesia_instance.save()

bordi_dict = {
    "name": "bordi",
    "description": "bordi shoqates"
}
bordi_instance = OrganizationGroup(**bordi_dict)
bordi_instance.save()

