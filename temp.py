poll4 = Poll(name="ngjyra", description="lala", body="afdl")
option9 = Option(body="bardhe")
option10 = Option(body="zi")
option11 = Option(body="lejla")
poll4.save()
option9.save()
option10.save()
option11.save()

option9.poll = poll4
option10.poll = poll4
option11.poll = poll4

poll4.save()

user3 = User.query.all()[2]

option9.users.append(user3)
option9.save()
option10.users.append(user3)
option10.save()

