import json
data_log = {
    "users": [
        {
            "login": "ДЖЕСОН123",
            "password": "ДЖЕБРЕВНИК8445"
        },
        {
            "login": "user2",
            "password": "pass2"
        }
    ]
}
with open("res.json",'w') as f:
    json.dump(data_log, f)



def check_login(login, password, json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    for user in data['users']:
        if user['login'] == login and user['password'] == password:
            return True


LOGIN = input("Введите логин: ")
PASSWORD = input("Введите пароль: ")

if __name__ == "__main__":
    FILE = 'res.json'
    if check_login(LOGIN, PASSWORD, FILE):
        print("Доступ к ДЖЕЙСОНБИРЕ РАЗРЕШЕН")
    else:
        print("Доступ к ДЖЕЙСОНБИРЕ Запрещен")


