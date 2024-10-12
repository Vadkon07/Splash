import json
import os
import psutil
import sys
import time
import multiprocessing

def d_menu():
    print("1. Reset update notification")
    print("2. Resources Monitor")
    var = input("Input your choice: ")

    if var == '1':
        reset_update_notif()
        print("Settings were updated. In the next time when you will run this app, it will show update notification again.")

    if var == '2':
        resources_monitor()

def reset_update_notif():
    with open ('app.json', 'r') as file:
        data = json.load(file)
        data['update_installed'] = True

    with open ('app.json', 'w') as file:
        json.dump(data, file, indent=4)

def resources_monitor():
    print("Welcome to the Resources Monitor! Choose one of these tools:\n")
    print("1. RAM monitor")
    print("2. CPU monitor\n")
    tool_choice = input("Input number of tool: ")

    if tool_choice == '1':
        safe = int(input("Safe mode ON (1) or OFF (0) ?: "))
        refresh_time = float(input("Refresh time in seconds ('0' to live refresh)?: "))
        allocate_memory(safe, refresh_time)

    if tool_choice == '2':
        refresh_time = float(input("Refresh time in seconds ('0' to live refresh)?: "))
        stress_cpu()

def allocate_memory(safe, refresh_time):
    i = 1

    while i == 1:
        total, available, used, free, percent = ram_info()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Total RAM: {total / (1024 * 1024):.2f} MB")
        print(f"Available RAM: {available / (1024 * 1024):.2f} MB")
        print(f"Used RAM: {used / (1024 * 1024):.2f} MB")
        print(f"Free RAM: {free / (1024 * 1024):.2f} MB")
        print(f"Percentage of RAM used: {percent}%")
        safe_mode(safe, percent)
        refresh_time
        time.sleep(refresh_time)

def safe_mode(safe, percent):
    if safe == 1:
        print("Safe mode status: ON")
        if percent >= 90.0:
            print("Usage of RAM is more than 90%, emergency shutdown!")
            os._exit(1)
    else:
        print("! Safe mode status: OFF !")

def ram_info():
    ram = psutil.virtual_memory()

    total_ram = ram.total
    available_ram = ram.available
    used_ram = ram.used
    free_ram = ram.free
    percent_used = ram.percent

    return total_ram, available_ram, used_ram, free_ram, percent_used

def cpu_stress():
    while True:
        start_time = time.time()
        while (time.time() - start_time) < (percentage / 100.0):
            pass
        time.sleep((100 - percentage) / 100.0)

def monitor_cpu():
    while True:
        usage = psutil.cpu_percent(interval=1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Current CPU usage: {usage}%")
        if os.name == 'posix':  # Linux/Unix
            temp = os.popen("sensors | grep 'Package id 0:' | awk '{print $4}'").read().strip()
            print(f"CPU Temperature: {temp} (probably doesn't work)") #FIX IT

def stress_cpu():
    processes = []
    monitor = multiprocessing.Process(target=monitor_cpu)
    monitor.start()

    time.sleep(999)

    for p in processes:
        p.terminate()
        p.join()  # Ensure the process has finished

    monitor.terminate()
    monitor.join()

if __name__ == "__main__":
    main()
