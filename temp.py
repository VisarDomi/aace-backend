###################
#users
test1_dict = {
    "email": "test1@aace.al",
    "password": "password"
}
test1_instance = User(**test1_dict)
test1_instance.save()

test2_dict = {
    "email": "test2@aace.al",
    "password": "password"
}
test2_instance = User(**test2_dict)
test2_instance.save()

test3_dict = {
    "email": "test3@aace.al",
    "password": "password"
}
test3_instance = User(**test3_dict)
test3_instance.save()

############################
#communications
communication1_dict = {
    "name": "communication1 name",
    "description": "communication1 description",
    "body": "communication1 body"
}
communication1_instance = OfficialCommunication(**communication1_dict)
communication1_instance.author = User.query.filter(User.id == 1).one()
communication1_instance.save()

communication2_dict = {
    "name": "communication2 name",
    "description": "communication2 description",
    "body": "communication2 body"
}
communication2_instance = OfficialCommunication(**communication2_dict)
communication2_instance.author = User.query.filter(User.id == 1).one()
communication2_instance.save()










#################################
#comments
# comment1_dict = {
#     "body": "comment1 body"
# }
# comment1_instance = OfficialComment(**comment1_dict)
# comment1_instance.author = User.query.filter(User.id == 2).one()
# comment1_instance.save()

