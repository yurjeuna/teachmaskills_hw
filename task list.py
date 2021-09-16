import json
task_list = []
tasks_dict = {key: "In process" for key in task_list}
fool_task_list = list(tasks_dict.items())


def editing(dictionary, task_status, old_task, new_task):
    dictionary2 = dict()
    dictionary2[new_task] = task_status
    del dictionary[old_task]
    dictionary.update(dictionary2)
    return dictionary

def adding(dictionary, task):
    dictionary2 = dict()
    dictionary2[task] = "In process"
    dictionary.update(dictionary2)
    return dictionary

def deleting(number, my_list, dictionary):
    del dictionary[my_list[number]]
    return True

def actions(action):
    action = input(f'Do you want to {action} with another one? (y/n) ')
    return action in ('y', 'Y')

def print_add(my_dict, my_list, fool_list):
    while True:
        new_task = input('Enter a new task - ')
        my_dict = adding(my_dict, new_task)
        my_list, fool_list = renew(my_dict, my_list, fool_list)
        if not actions('add'):
            break
        continue
    return True

def print_periodic_task_list(k_list):
    for i in range(len(k_list)):
        print(i + 1, k_list[i], sep=' ')
    pass

def print_periodic_fool_task_list(k_list):
    for i in range(len(k_list)):
        print((i + 1), k_list[i][1], k_list[i][0],  sep=' ')
    pass

def valid_number(number, my_list):
    return number.isdigit() and 0 < int(number) <= len(my_list)

def renew(my_dict, my_list, fool_list):
    my_list = list(my_dict.keys())
    fool_list = list(my_dict.items())
    return my_list, fool_list

def print_delete(my_dict, my_list, fool_list):
    while True:
        my_list, fool_list = renew(my_dict, my_list, fool_list)
        print_periodic_task_list(my_list)
        del_task = input('What task do you want to delete? Enter a number - ')
        if not valid_number(del_task, my_list):
            print('Non valid task number! ')
            print_periodic_task_list(my_list)
            continue
        del_task = int(del_task) - 1
        deleting(del_task, my_list, my_dict)
        my_list, fool_list = renew(my_dict, my_list, fool_list)
        print_periodic_task_list(my_list)
        if not actions('delete'):
            break
        continue
    return True

def print_edit(my_dict, my_list, fool_list):
    while True:
        my_list, fool_list = renew(my_dict, my_list, fool_list)
        print_periodic_task_list(my_list)
        edit_task = input('What task do you want to edit? Enter a number - ')
        if not valid_number(edit_task, my_list):
            print('Non valid task number!')
            continue
        edit_task = int(edit_task) - 1
        edited_task = input('Enter a new text - ')
        unedited_task = my_list[edit_task]
        unedited_task_status = my_dict[unedited_task]
        my_dict = editing(my_dict, unedited_task_status, unedited_task, edited_task)
        my_list, fool_list = renew(my_dict, my_list, fool_list)
        print_periodic_task_list(my_list)
        if not actions('edit'):
            break
        continue
    return True

def print_mark(my_dict, my_list, fool_list):
    while True:
        my_list, fool_list = renew(my_dict, my_list, fool_list)
        print_periodic_fool_task_list(fool_list)
        numb_task_for_status_changing = input('What task do you want to mark as completed? Enter a number - ')
        if not valid_number(numb_task_for_status_changing, my_list):
            print('Non valid task number!')
            continue
        numb_task_for_status_changing = int(numb_task_for_status_changing) - 1
        task_for_status_changing = my_list[numb_task_for_status_changing]
        my_dict[task_for_status_changing] = 'Done'
        my_list, fool_list = renew(my_dict, my_list, fool_list)
        print_periodic_fool_task_list(fool_list)
        if not actions('mark as completed'):
            break
        continue
    return True

def print_highlight_all(my_dict, my_list, fool_list):
    while True:
        multiple = input('If you want to delete all tasks, press 1. \n'
                         'If you want to mark all tasks as completed, press 2. \n'
                         'If you want to mark all tasks as uncompleted, press 3. - ')
        if multiple == '1':
            my_dict = dict()
            my_list, fool_list = renew(my_dict, my_list, fool_list)
        elif multiple == '2':
            for i in my_dict:
                my_dict[i] = "Done"
            my_list, fool_list = renew(my_dict, my_list, fool_list)
            print_periodic_fool_task_list(fool_list)
        elif multiple == '3':
            for i in my_dict:
                my_dict[i] = "In process"
            my_list, fool_list = renew(my_dict, my_list, fool_list)
            print_periodic_fool_task_list(fool_list)
        else:
            continue
        if not actions('highlight all'):
            break
        continue
    return True

def print_show_completed(my_dict, my_list, fool_list):
    my_list, fool_list = renew(my_dict, my_list, fool_list)
    list_done = list(filter(lambda x: my_dict[x] == "Done", my_dict.keys()))
    for i in list_done:
        if i in my_dict.keys():
            print((my_list.index(i) + 1), i, 'Done',  sep=' ')
    return True

def print_show_uncompleted(my_dict, my_list, fool_list):
    my_list, fool_list = renew(my_dict, my_list, fool_list)
    list_undone = list(filter(lambda x: my_dict[x] == "In process", my_dict.keys()))
    for i in list_undone:
        if i in my_dict.keys():
            print((my_list.index(i) + 1), i, 'In process',  sep=' ')
    return True

def print_search(my_dict, my_list, fool_list):
    while True:
        my_list, fool_list = renew(my_dict, my_list, fool_list)
        search = input('What should we look for? ')
        for i in my_list:
            if i.find(search) != -1:
                print((my_list.index(i) + 1), i, my_dict[i])
        if not actions('search text'):
            break
        continue
    return True

def print_task_list(my_dict, my_list, fool_list):
    my_list, fool_list = renew(my_dict, my_list, fool_list)
    print_periodic_fool_task_list(fool_list)
    a = input('If you want to open task list from file, press 1')
    if a == '1':
        with open('data_file.json', 'r') as task_file:
            data = json.load(task_file)
            data_list = list(data.keys())
            print('Saved in file:')
            for i in data_list:
                print((data_list.index(i) + 1), i, data[i])
    b = input('If you want to transfer task list from file for new operations, press 1')
    if b == '1':
        my_dict = dict(data)
        my_list, fool_list = renew(my_dict, my_list, fool_list)
        print_periodic_fool_task_list(fool_list)
    return True


def print_save(my_dict, my_list, fool_list):
    my_list, fool_list = renew(my_dict, my_list, fool_list)
    with open('data_file.json', 'w') as task_file:
        json.dump(my_dict, task_file)
    print('Saved:')
    print_periodic_fool_task_list(fool_list)
    return True

def exit_from():
    exit()

menu = """
\nChoice menu option:\n
1 - open (previous) task list
2 - add a new task
3 - delete a task
4 - edit a task
5 - mark a task as completed
6 - highlight all tasks
7 - show only completed tasks
8 - show only uncompleted tasks
9 - search by text
10 - save this task list
0 - exit
"""

menu_dict = {
    '1': print_task_list,
    '2': print_add,
    '3': print_delete,
    '4': print_edit,
    '5': print_mark,
    '6': print_highlight_all,
    '7': print_show_completed,
    '8': print_show_uncompleted,
    '9': print_search,
    '10': print_save,
    '0': exit_from
}

while True:
    menu_numb = input(menu)
    choice = menu_dict.get(menu_numb)
    if not choice:
        print("No entered option. Try again")
        continue
    choice(tasks_dict, task_list, fool_task_list)
