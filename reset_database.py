from api.common.models import User, Group, Post, Media
from api.common.database import db_session

# from api.common.database import drop_db


visar = User(email="visar3")
erdal = User(email="erdal4")
group1 = Group(body="civil5")
visar.groups.append(group1)
group2 = Group(body="elektrik6")
visar.groups.append(group2)
erdal.groups.append(group2)
db_session.add(group1)
db_session.add(group2)
db_session.add(visar)
db_session.add(erdal)
db_session.commit()


user_data = {"email": "erdal@forcewing.com", "password": "password"}
User.query.filter(User.email == user_data["email"]).one_or_none()
user_data2 = {"email": "erdal2@forcewing.com", "password": "password"}
User.query.filter(User.email == user_data2["email"]).one_or_none()
user = User.new_from_dict(user_data, error_on_extra_keys=False, drop_extra_keys=True)
user.set_password(user_data["password"])


User.query.filter(User.email != "visar@forcewing.com").filter(
    User.email != "erdal@forcewing.com"
).all()

user = User.query.filter(User.email == "visar@forcewing.com").one()
user.experiences.filter_by(id=1).one()

posts = Post.query.filter(Post.user_id == '1').all()
medias = Media.query.filter(Media.experience_id == '1').all()
