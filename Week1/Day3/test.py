users = ["Mickey","Minnie","Donald","Ariel","Pluto"]


# 5th result
disney_users_A = {user: index for index, user in enumerate(users) if user.lower().startswith(('m', 'p'))}
print(disney_users_A)