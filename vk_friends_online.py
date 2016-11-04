import vk

APP_ID = 5708591


def get_user_login():
	login = input('Введите логин\n')
	return login 

def get_user_password():
	password = input('Введите пароль\n')
	return password


def get_online_friends(login, password):
	session = vk.AuthSession(app_id=APP_ID, user_login=login, user_password=password, scope='friends')
	api = vk.API(session)
	dict_of_id = api.friends.getOnline(order = 'hints')
	dict_of_name = api.users.get(user_ids=dict_of_id)
	return dict_of_name 	


def output_friends_to_console(friends_online):
	print ('Список ваших друзей онлайн')
	for user in friends_online:
		print ('{} {}'.format(user['last_name'],user['first_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
