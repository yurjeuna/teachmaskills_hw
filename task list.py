import json
import os

class Tasks:
    def __init__(self, task):
        self.task = task
        self.task_status = "In process"

class Options:
    task_list = []

    @staticmethod
    def print_periodic_task_list():
        for i in range(len(Options.task_list)):
            print((i + 1), Options.task_list[i][0], Options.task_list[i][1], sep=' ')

    def success_dec(func):
        def wrapper(*args, **kwargs):
            while True:
                result = func(*args, **kwargs)
                Options.print_periodic_task_list()
                answer = input('Shall we repeat? (y/n) ')
                if answer.lower() not in ('y', 'yes'):
                    break
                continue
            return result
        return wrapper

    @staticmethod
    def print_periodic_task_list():
        for i in range(len(Options.task_list)):
            print((i + 1), Options.task_list[i][0], Options.task_list[i][1], sep=' ')

    @staticmethod
    @success_dec
    def print_add():
        Options.task_list.append(Tasks(input('Enter a new task - ')))
        return Options.task_list

    def valid_number(number):
        return number.isdigit() and 0 < int(number) <= len(Options.task_list)

    @staticmethod
    @success_dec
    def print_delete():
        while True:
            Options.print_periodic_task_list()
            del_task = input('What task do you want to delete? Enter a number - ')
            if not Options.valid_number(del_task):
                print('Non valid task number! ')
                Options.print_periodic_task_list()
                continue
            del_task = int(del_task) - 1
            del [Options.task_list[del_task]]
            break
        return Options.task_list

    def editing(cons_task_status, old_task, new_task):
        Options.task_list[new_task] = cons_task_status
        del Options.task_list[old_task]
        return Options.task_list

    @staticmethod
    @success_dec
    def print_edit():
        while True:
            Options.print_periodic_task_list()
            edit_task = input('What task do you want to edit? Enter a number - ')
            if not Options.valid_number(edit_task):
                print('Non valid task number!')
                continue
            edit_task = int(edit_task) - 1
            edited_task = input('Enter a new text - ')
            unedited_task = Options.task_list[edit_task]
            unedited_task_status = Options.task_list[edit_task][1]
            Options.editing(unedited_task_status, unedited_task, edited_task)
            break
        return Options.task_list

    @staticmethod
    @success_dec
    def print_mark():
        while True:
            Options.print_periodic_task_list()
            numb_task_for_status_changing = input('What task do you want to mark as completed? Enter a number - ')
            if not Options.valid_number(numb_task_for_status_changing):
                print('Non valid task number!')
                continue
            numb_task_for_status_changing = int(numb_task_for_status_changing) - 1
            task_for_status_changing = Options.task_list[numb_task_for_status_changing]
            Options.task_list[task_for_status_changing][1] = 'Done'
            break
        return Options.task_list

    @staticmethod
    @success_dec
    def print_highlight_all():
        while True:
            multiple = input('If you want to delete all tasks, press 1. \n'
                             'If you want to mark all tasks as completed, press 2. \n'
                             'If you want to mark all tasks as uncompleted, press 3. - ')
            if multiple == '1':
                Options.task_list = []
            elif multiple == '2':
                for i in range(len(Options.task_list)):
                    Options.task_list[i][1] = "Done"
                Options.print_periodic_task_list()
            elif multiple == '3':
                for i in range(len(Options.task_list)):
                    Options.task_list[i][1] = "In process"
                Options.print_periodic_task_list()
            else:
                break
            break
        return Options.task_list

    @staticmethod
    def print_show_completed():
        list_done = list(filter(lambda x: Options.task_list[x][1] == "Done", Options.task_list))
        for i in list_done:
            if i in Options.task_list:
                print((Options.task_list(i) + 1), i, 'Done',  sep=' ')
        return True

    @staticmethod
    def print_show_uncompleted():
        list_undone = list(filter(lambda x: Options.task_list[x][1] == "In process", Options.task_list))
        for i in list_undone:
            if i in Options.task_list:
                print((Options.task_list(i) + 1), i, 'In process',  sep=' ')
        return True

    @staticmethod
    def print_search():
        while True:
            search = input('What should we look for? ')
            for i in Options.task_list:
                if i.find(search) != -1:
                    print((Options.task_list.index(i) + 1), i, Options.task_list[i][1])
        return True

    @staticmethod
    def print_task_list():
        Options.print_periodic_task_list()
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
                data_list = Options.task_list
                print('Saved in file:')
                for i in data_list:
                    print((data_list.index(i) + 1), i, data[i])
            b = input('If you want to transfer task list from file for new operations, press 1')
            if b == '1':
                Options.task_list = dict(data)
                Options.print_periodic_task_list()
        return True

    @staticmethod
    def print_save():
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
                    json.dump(Options.task_list, task_file)
                os.rename('somefile.json', (file_name + '.json'))
                print('Saved:')
                Options.print_periodic_task_list()
                break
            elif file_choice == '2':
                file_numb = int(input("In what file you want to save your task list? Enter a number"))
                with open(file_lis[file_numb - 1], 'w') as task_file:
                    json.dump(Options.task_list, task_file)
                print('Saved:')
                Options.print_periodic_task_list()
                break
            else:
                continue
        return True

    @staticmethod
    def exit_from():
        exit()

def main():

    menu_dict = {
        '2': (Options.print_add, 'add a new task'),
        '3': (Options.print_delete, 'delete a task'),
        '4': (Options.print_edit, 'edit a task'),
        '5': (Options.print_mark, 'mark a task as completed'),
        '6': (Options.print_highlight_all, 'highlight all tasks'),
        '7': (Options.print_show_completed, 'show only completed tasks'),
        '8': (Options.print_show_uncompleted, 'show only uncompleted tasks'),
        '9': (Options.print_search, 'search by text'),
        '10': (Options.print_save, 'save this task list'),
        '0': (Options.exit_from, 'exit')
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
