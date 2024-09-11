import json

def d_menu():
    print("1. Reset update notification")
    var = input("Input your choice: ")

    if var == '1':
        reset_update_notif()
        print("Settings were updated. In the next time when you will run this app, it will show update notification again.")

def reset_update_notif():
    with open ('app.json', 'r') as file:
        data = json.load(file)
        data['update_installed'] = True

    with open ('app.json', 'w') as file:
        json.dump(data, file, indent=4)
