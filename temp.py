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


test1_dict = {
    "email": "test1@aace.al",
    "password": "password"
}
test1 = create_user(test1_dict)
test1.save()

test2_dict = {
    "email": "test2@aace.al",
    "password": "password"
}
test2 = create_user(test2_dict)
test2.save()

test3_dict = {
    "email": "test3@aace.al",
    "password": "password"
}
test3 = create_user(test3_dict)
test3.save()

############################
# communications

communication1_dict = {
    "name": "communication1 name",
    "description": "communication1 description",
    "body": "communication1 body"
}
communication1 = OfficialCommunication(**communication1_dict)
communication1.author = User.query.filter(User.id == 1).one()
communication1.save()

communication2_dict = {
    "name": "communication2 name",
    "description": "communication2 description",
    "body": "communication2 body"
}
communication2 = OfficialCommunication(**communication2_dict)
communication2.author = User.query.filter(User.id == 1).one()
communication2.save()


###############################
# accept users as members add them to organizationgroup 'anetaret'

user_ids = {
    "ids": [2, 3, 4]
}

admin_payload = {
    "application_status": "accepted",
    "comment_from_administrator": "",
    "accepted_date": "2019-03-18"
}

for user_id in user_ids["ids"]:
    user = User.query.filter(User.id == user_id).one()

    # accept users
    user.update(**admin_payload)
    user.save()

    # add them to organizationgroup 'anetaret'
    organizationgroups = OrganizationGroup.query.all()
    anetaret = organizationgroups[0]
    user_in_a_group = None
    for organizationgroup in organizationgroups:
        if user == organizationgroup.users.filter(User.id == user_id).one_or_none():
            user_in_a_group = user
    if user is not user_in_a_group:
        organizationgroup = anetaret
        organizationgroup.users.append(user)
        organizationgroup.save()


######################################################
# add organizationgroup 'anetaret' to communication 1 and 2

communication_list = [communication1, communication2]
anetaret = organizationgroups[0]
organizationgroups = OrganizationGroup.query.all()
organizationgroup = anetaret
for officialcommunication in communication_list:
    og_in_oc_one_or_none = officialcommunication.organizationgroups.filter(
        OrganizationGroup.id == organizationgroup.id
    ).one_or_none()
    if organizationgroup is not og_in_oc_one_or_none:
        # add organizationgroup only it is not part of that officialcommunication
        officialcommunication.organizationgroups.append(organizationgroup)
        officialcommunication.save()
    else:
        print(f"{organizationgroup} is already part of {officialcommunication}")


#################################
# add comments to communication 1

comment1_dict = {
    "body": "comment1 body"
}
comment2_dict = {
    "body": "comment2 body"
}
comments = [comment1_dict, comment2_dict]
author_id = 2
officialcommunication = communication1
for comment in comments:
    comment1 = OfficialComment(**comment)
    comment1.officialcommunication = OfficialCommunication.query.filter(OfficialCommunication.id == officialcommunication.id).one()
    comment1.author = User.query.filter(User.id == author_id).one()
    comment1.save()

comment3_dict = {
    "body": "comment3 body"
}
comment4_dict = {
    "body": "comment4 body"
}
comments = [comment3_dict, comment4_dict]
author_id = 3
officialcommunication = communication2
for comment in comments:
    comment1 = OfficialComment(**comment)
    comment1.officialcommunication = OfficialCommunication.query.filter(OfficialCommunication.id == officialcommunication.id).one()
    comment1.author = User.query.filter(User.id == author_id).one()
    comment1.save()



db_session.commit()
