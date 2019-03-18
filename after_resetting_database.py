#########################################################
# Admin
def create_user(user_data):
    if user_data["email"] is None or user_data["password"] is None:
        print("Please provide an email and a password.")
    if not User.query.filter(User.email == user_data["email"]).one_or_none():
        user = User(**user_data)
        user.set_password(user_data["password"])
        user.save()
    else:
        print(f'Email `{user_data["email"]}` is already in use for another account.')
    if user.id == 1:
        user.role = "admin"
        user.save()
    user.get_token(expires_in=36_000_000)

    return user

admin_dict = {
    "email": "admin@aace.al",
    "password": "password"
}
admin = create_user(admin_dict)
admin.save()

#########################################################
# Groups

anetaret_dict = {
    "name": "anetaret",
    "description": "anetaret shoqates"
}
anetaret = OrganizationGroup(**anetaret_dict)
anetaret.save()

presidenti_dict = {
    "name": "presidenti",
    "description": "presidenti shoqates"
}
presidenti = OrganizationGroup(**presidenti_dict)
presidenti.save()

sekretari_dict = {
    "name": "sekretari",
    "description": "sekretari shoqates"
}
sekretari = OrganizationGroup(**sekretari_dict)
sekretari.save()

koordinatori_dict = {
    "name": "koordinatori",
    "description": "koordinatori shoqates"
}
koordinatori = OrganizationGroup(**koordinatori_dict)
koordinatori.save()

kryesia_dict = {
    "name": "kryesia",
    "description": "kryesia shoqates"
}
kryesia = OrganizationGroup(**kryesia_dict)
kryesia.save()

bordi_dict = {
    "name": "bordi",
    "description": "bordi shoqates"
}
bordi = OrganizationGroup(**bordi_dict)
bordi.save()

db_session.commit()
