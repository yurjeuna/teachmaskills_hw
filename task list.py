import json
import os
task_list = []
tasks_dict = {key: "In process" for key in task_list}
fool_task_list = list(tasks_dict.items())

def editing(dictionary, task_status, old_task, new_task):
    dictionary[new_task] = task_status
    del dictionary[old_task]
    return dictionary

def adding(dictionary, task):
    dictionary2 = dict()
    dictionary2[task] = "In process"
    dictionary.update(dictionary2)
    return dictionary

def deleting(number):
    del tasks_dict[task_list[number]]
    return True

def success_dec(func):
    def wrapper(*args, **kwargs):
        while True:
            result = func(*args, **kwargs)
            print_periodic_fool_task_list()
            answer = input('Shall we repeat? (y/n) ')
            if answer.lower() not in ('y', 'yes'):
                break
            continue
        return result
    return wrapper

@success_dec
def print_add():
    new_task = input('Enter a new task - ')
    global tasks_dict
    tasks_dict = adding(tasks_dict, new_task)
    renew()
    return tasks_dict, task_list, fool_task_list

def print_periodic_task_list():
    for i in range(len(task_list)):
        print(i + 1, task_list[i], sep=' ')
    pass

def print_periodic_fool_task_list():
    for i in range(len(fool_task_list)):
        print((i + 1), fool_task_list[i][0], fool_task_list[i][1], sep=' ')
    pass

def valid_number(number, my_list):
    return number.isdigit() and 0 < int(number) <= len(my_list)

def renew():
    global tasks_dict, task_list, fool_task_list
    task_list = list(tasks_dict.keys())
    fool_task_list = list(tasks_dict.items())
    return task_list, fool_task_list

@success_dec
def print_delete():
    while True:
        print_periodic_task_list()
        del_task = input('What task do you want to delete? Enter a number - ')
        if not valid_number(del_task, task_list):
            print('Non valid task number! ')
            print_periodic_task_list()
            continue
        del_task = int(del_task) - 1
        deleting(del_task)
        renew()
        break
    return tasks_dict, task_list, fool_task_list

@success_dec
def print_edit():
    while True:
        global tasks_dict
        print_periodic_task_list()
        edit_task = input('What task do you want to edit? Enter a number - ')
        if not valid_number(edit_task, task_list):
            print('Non valid task number!')
            continue
        edit_task = int(edit_task) - 1
        edited_task = input('Enter a new text - ')
        unedited_task = task_list[edit_task]
        unedited_task_status = tasks_dict[unedited_task]
        tasks_dict = editing(tasks_dict, unedited_task_status, unedited_task, edited_task)
        renew()
        break
    return tasks_dict, task_list, fool_task_list

@success_dec
def print_mark():
    while True:
        print_periodic_fool_task_list()
        numb_task_for_status_changing = input('What task do you want to mark as completed? Enter a number - ')
        if not valid_number(numb_task_for_status_changing):
            print('Non valid task number!')
            continue
        numb_task_for_status_changing = int(numb_task_for_status_changing) - 1
        task_for_status_changing = task_list[numb_task_for_status_changing]
        tasks_dict[task_for_status_changing] = 'Done'
        renew()
        break
    return tasks_dict, task_list, fool_task_list

@success_dec
def print_highlight_all():
    while True:
        multiple = input('If you want to delete all tasks, press 1. \n'
                         'If you want to mark all tasks as completed, press 2. \n'
                         'If you want to mark all tasks as uncompleted, press 3. - ')
        if multiple == '1':
            my_dict = dict()
            renew()
        elif multiple == '2':
            for i in tasks_dict:
                tasks_dict[i] = "Done"
            renew()
            print_periodic_fool_task_list()
        elif multiple == '3':
            for i in tasks_dict:
                tasks_dict[i] = "In process"
            renew()
            print_periodic_fool_task_list()
        else:
            break
        break
    return tasks_dict, task_list, fool_task_list

def print_show_completed():
    list_done = list(filter(lambda x: tasks_dict[x] == "Done", tasks_dict.keys()))
    for i in list_done:
        if i in tasks_dict.keys():
            print((task_list.index(i) + 1), i, 'Done',  sep=' ')
    return True

def print_show_uncompleted():
    list_undone = list(filter(lambda x: tasks_dict[x] == "In process", tasks_dict.keys()))
    for i in list_undone:
        if i in tasks_dict.keys():
            print((task_list.index(i) + 1), i, 'In process',  sep=' ')
    return True

def print_search():
    while True:
        search = input('What should we look for? ')
        for i in task_list:
            if i.find(search) != -1:
                print((task_list.index(i) + 1), i, tasks_dict[i])
    return True

def print_task_list():
    print_periodic_fool_task_list()
    a = input('If you want to open task list from file, press 1')
    if a == '1':
        os.getcwd()
        try:
            os.chdir("task_folder")
        except FileNotFoundError:
            os.mkdir("task_folder")
        file_lis = os.listdir()
        if len(file_lis) == 0:
            print('No saved files')
        else:
            print("Saved files:")
            for i in range(len(file_lis)):
                print(i + 1, file_lis[i], sep=' ')
            file_numb = int(input("What file you want to open? Enter a number"))
            with open(file_lis[file_numb - 1], 'r') as task_file:
                data = json.load(task_file)
            data_list = list(data.keys())
            print('Saved in file:')
            for i in data_list:
                print((data_list.index(i) + 1), i, data[i])
        b = input('If you want to transfer task list from file for new operations, press 1')
        if b == '1':
            global tasks_dict
            tasks_dict = dict(data)
            renew()
            print_periodic_fool_task_list()
    return True

def print_save():
    renew()
    os.getcwd()
    try:
        os.chdir("task_folder")
    except FileNotFoundError:
        os.mkdir("task_folder")
    file_lis = os.listdir()
    print("Saved files:")
    for i in range(len(file_lis)):
        print(i + 1, file_lis[i], sep=' ')
    while True:
        file_choice = input("1 - save to a new file \n2 - save to existing file")
        if file_choice == '1':
            file_name = input("In what file you want to save your task list?")
            with open('somefile.json', 'w') as task_file:
                json.dump(tasks_dict, task_file)
            os.rename('somefile.json', (file_name + '.json'))
            print('Saved:')
            print_periodic_fool_task_list()
            break
        elif file_choice == '2':
            file_numb = int(input("In what file you want to save your task list? Enter a number"))
            with open(file_lis[file_numb - 1], 'w') as task_file:
                json.dump(tasks_dict, task_file)
            print('Saved:')
            print_periodic_fool_task_list()
            break
        else:
            continue
    return True

def exit_from():
    exit()

def main():

    menu_dict = {
        '1': (print_task_list,'open (previous) task list'),
        '2': (print_add, 'add a new task'),
        '3': (print_delete, 'delete a task'),
        '4': (print_edit, 'edit a task'),
        '5': (print_mark, 'mark a task as completed'),
        '6': (print_highlight_all, 'highlight all tasks'),
        '7': (print_show_completed, 'show only completed tasks'),
        '8': (print_show_uncompleted, 'show only uncompleted tasks'),
        '9': (print_search, 'search by text'),
        '10': (print_save, 'save this task list'),
        '0': (exit_from, 'exit')
    }

    while True:
        for i in menu_dict:
            print(i, menu_dict[i][1], sep=' ', end='\n')
        menu_numb = input('Choose, what should we do? ')
        if menu_numb not in menu_dict.keys():
            print("Incorrect. Try again")
            continue
        menu_dict[menu_numb][0]()
    return True

main()
