task_list = []
tasks_dict = {key: "In process" for key in task_list}
fool_task_list = list(tasks_dict.items())
x = 1


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


while x:
    to_do = input('Hi! If you want to open previous task list, press 1. \n'
              'If you want to add a new task, press 2. \n'
              'If you want to delete the task, press 3. \n'
              'If you want to edit the task, press 4. \n'
              'If you want to mark the task as completed, press 5. \n'
              'If you want to highlight all tasks, press 6. \n'
              'If you want to save this task list, press 7. \n'
              'For exit enter any other number -- ')
    if to_do == '1':
        for i in range(len(fool_task_list)):
            print((i + 1), fool_task_list[i][1], fool_task_list[i][0],  sep=' ')
        a = input('If you want to open task list from file, press 1')
        if a == '1':
            fin = open('tasks.txt', 'r')
            print(fin.readlines())
        continue

    elif to_do == '2':
        while to_do:
            new_task = input('Enter a new task - ')
            tasks_dict = adding(tasks_dict, new_task)
            task_list = list(tasks_dict.keys())
            fool_task_list = list(tasks_dict.items())
            break
        continue

    elif to_do == '3':
        for i in range(len(task_list)):
            print(i + 1, task_list[i], sep=' ')
        del_task = int(input('What task do you want to delete? Enter a number - ')) - 1
        del tasks_dict[task_list[del_task]]
        task_list = list(tasks_dict.keys())
        fool_task_list = list(tasks_dict.items())
        for i in range(len(task_list)):
            print((i + 1), task_list[i], sep=' ')
        continue

    elif to_do == '4':
        for i in range(len(task_list)):
            print(i + 1, task_list[i], sep=' ')
        edit_task = int(input('What task do you want to edit? Enter a number - ')) - 1
        edited_task = input('Enter a new text - ')
        unedited_task = task_list[edit_task]
        unedited_task_status = tasks_dict[unedited_task]
        tasks_dict = editing(tasks_dict, unedited_task_status, unedited_task, edited_task)
        task_list = list(tasks_dict.keys())
        fool_task_list = list(tasks_dict.items())
        continue

    elif to_do == '5':
         for i in range(len(fool_task_list)):
            print((i + 1), fool_task_list[i][1], fool_task_list[i][0],  sep=' ')
         numb_task_for_status_changing = int(input('What task do you want to mark as completed? Enter a number - ')) - 1
         task_for_status_changing = task_list[numb_task_for_status_changing]
         tasks_dict[task_for_status_changing] = 'Done'
         task_list = list(tasks_dict.keys())
         fool_task_list = list(tasks_dict.items())
         continue

    elif to_do == '6':
        multiple = input('If you want to delete all tasks, press 1. \n'
                         'If you want to mark all tasks as completed, press 2. \n'
                         'If you want to mark all tasks as uncompleted, press 3. - ')
        if multiple == '1':
            tasks_dict = dict()
            task_list = list(tasks_dict.keys())
            fool_task_list = list(tasks_dict.items())
        elif multiple == '2':
            for i in tasks_dict:
                tasks_dict[i] = "Done"
            task_list = list(tasks_dict.keys())
            fool_task_list = list(tasks_dict.items())
        elif multiple == '3':
            for i in tasks_dict:
                tasks_dict[i] = "In process"
            task_list = list(tasks_dict.keys())
            fool_task_list = list(tasks_dict.items())
        continue

    elif to_do == '7':
        fout = open('tasks.txt', 'w')
        fout.write(tasks_dict)
        fout.write(task_list)
        fout.write(fool_task_list)

        print('Now in file:', )
        for line in fout:
            print(fout.readlines())
    break

fin.close()
fout.close()
