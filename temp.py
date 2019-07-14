###################
# users


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

####################
# organizationgroups

anetaret_dict = {
    "name": "anetaret",
    "description": "anetaret e shoqates"
}
presidenti_dict = {
    "name": "presidenti",
    "description": "presidenti i shoqates"
}
sekretari_dict = {
    "name": "sekretari",
    "description": "sekretari i shoqates"
}
koordinatori_dict = {
    "name": "koordinatori",
    "description": "koordinatori i shoqates"
}
kryesia_dict = {
    "name": "kryesia",
    "description": "kryesia e shoqates"
}
bordi_dict = {
    "name": "bordi",
    "description": "bordi i shoqates"
}
anetaret = OrganizationGroup(**anetaret_dict)
anetaret.save()
presidenti = OrganizationGroup(**presidenti_dict)
presidenti.save()
sekretari = OrganizationGroup(**sekretari_dict)
sekretari.save()
koordinatori = OrganizationGroup(**koordinatori_dict)
koordinatori.save()
kryesia = OrganizationGroup(**kryesia_dict)
kryesia.save()
bordi = OrganizationGroup(**bordi_dict)
bordi.save()

db_session.commit()
