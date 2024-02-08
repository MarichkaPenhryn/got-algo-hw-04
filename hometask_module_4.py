#------------------------------------------------------------------------------
#----------------------- TASK 1 -----------------------------------------------
#------------------------------------------------------------------------------

from pathlib import Path

def total_salary(path):
    # відкриваємо дві копії
    fh, fh1 = open(path, 'r'), open(path, 'r')
    # створюємо список, total для суми і прапорець n для підрахунку кількості стрічок
    lst_salary = list()
    n = 0
    total = 0

    while True:
        # читаємо стрічки по одній
        line = fh.readline()
        if not line:
            # в останньому рядку, виникає проблема того, що в його кінці немає переносу, тому ми видалили одну цифру
            # щоб не проходтити список купу разів, ми просто віднімкмо від тоталу останнє число і додамо проавильне
            # для цього ми створили копію спочатку і зараз просто візьмемо з неї останній елемент і вже тоді вийдемо з циклу
            # (не дуже елегантно)
            total -= lst_salary[n-1]
            total += int(fh1.readlines()[n-1].split(',')[1])
            break
        # рахуємо людей, в total  додаємо зп кожного без урахування переносу на новий рядок в кінці кожного рядка
        n += 1
        total += int(line.split(',')[1][:-1])
        # складаємо список зп
        lst_salary.append(int(line.split(',')[1][:-1]))

    # ? Наскільки округлити
    average = round(total / n, 2)
    fh.close()
    fh1.close()
    return total, average

#для використання
#try:
#    total, average = total_salary("/Users/marichkapenhryn/salary.txt")
#    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
#except:
#    print("File not found")

#------------------------------------------------------------------------------
#----------------------- TASK 2 -----------------------------------------------
#------------------------------------------------------------------------------

from pathlib import Path

def get_cats_info(path):
    # Відкриваємо файл, створюємо список стрічок і закриваємо
    with open(path, "r") as fh:
        lines = [el.strip() for el in fh.readlines()]

    # Створюємо пустий список
    list_of_cats = list()
    # Проходимось по кожній стрічці
    for cat in lines:
        # В пустий словник записуємо значення з ключами id, name, age
        dic_of_cat = {}
        dic_of_cat["id"] = cat.split(',')[0]
        dic_of_cat["name"] = cat.split(',')[1]
        dic_of_cat["age"] = cat.split(',')[2]
        # Додаємо до списку словник
        list_of_cats.append(dic_of_cat)
    return list_of_cats

#для використання
#try:
#    cats_info = get_cats_info("/Users/marichkapenhryn/cats.txt")
#    print(cats_info)
#except:
#    print("File not found")

#------------------------------------------------------------------------------
#----------------------- TASK 4 -----------------------------------------------
#------------------------------------------------------------------------------

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Якщо контакт вже існує, то повідомляємо про це, якщо ні, додаємо,
# якщо неправильний ввід, повідомляємо про помилку
def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            return f'Contact {name} is already exist. If you want to change, choose another command'
        else:
            contacts[name] = phone
            return "Contact added."
    except:
        return 'Input error'

# ??? якщо команда 'add', але аргументи не порожні видаємо повідомлення про помилку? чи показуємо?
def show_all(args, contacts):
    try:
        a = args[0]
        return 'In case you want see all phones, print only [all]'
    except:
        return contacts

def show_phone(args, contacts):
    try:
        # якщо користувач ввів не тільки команду і ім'я, то просимо ввести правильно?
        try:
            a = args[1]
            return 'In case you want see phone number, print only [phone] and [name]'
        except:
            return contacts[args[0]]
    except:
        return 'User not found'

def change_contact(args, contacts):
    try:
        name, phone = args
        # якщо контакт не існує, то повідомляємо про це, як існує то додаємо
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return f'Contact {name} is not exist.'
    except:
        return 'Input error'


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


#------------------------------------------------------------------------------
#----------------------- TASK 3 -----------------------------------------------
#------------------------------------------------------------------------------

# без коментарів

#from colorama import Fore, Back, Style
#import pathlib

#def print_directory(dir):
#    directory = pathlib.Path(dir)
#    print(Fore.BLUE+f'{directory.parts[-1]}'.upper())
#    for path in directory.iterdir():
#        if path.is_dir():
#            print(Fore.CYAN+f' |--------> {path.parts[-1]}')
#            for i in path.iterdir():
#                i.parts
#                print(Fore.YELLOW+f' |\t\t|-------->{i.parts[-1]}')
#                if pathlib.Path.is_dir(i):
#                    for j in i.iterdir():
#                        print(f'\t\t{j.parts[-1]}')
#        else:
#            print(Fore.CYAN+f' |--------> {path.parts[-1]}')

#для використання
#try:
    #print_directory('/Users/marichkapenhryn/Desktop/picture')
#except:
    #print('This directory does not exist')
