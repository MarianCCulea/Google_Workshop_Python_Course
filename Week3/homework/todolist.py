import datetime
import json

filename = "todolist.txt"


def menu():
    print("1. Adaugare task")
    print("2. Listare task-uri")
    print("3. Sortare task-uri")
    print("4. Filtrare")
    print("5. Iesire")


def sort_menu():
    print("1. Sortare ascendentă task")
    print("2. Sortare descendentă task")
    print("3. Sortare ascendentă dată")
    print("4. Sortare descendentă dată")
    print("5. Sortare ascendentă persoană responsabilă")
    print("6. Sortare descendentă persoană responsabilă")
    print("7. Sortare ascendentă categorie")
    print("8. Sortare descendentă categorie")
    print("9. Meniu Principal")


def filter_menu():
    print("1. Dupa Numele Taskului")
    print("2. Dupa Categoria Taskului")
    print("3. Dupa Responsabilul Taskului")
    print("4. Dupa data Taskului")
    print("5. Meniu Principal")


def edit_menu():
    print("1. Modifica")
    print("2. Sterge")
    print("3. Meniu Principal")


def add_method():
    categories = read_categories()
    task_name = input("Introduceți numele task-ului: ")
    while not is_valid_task(task_name):
        task_name = input("Taskul introdus este deja in lista. Specificati alt task: ")
    task_date = input("Introduceți data (YYYY-MM-DD): ")
    while not is_valid_date(task_date):
        task_date = input(
            "Data introdusă nu este validă. Introduceți data în formatul YYYY-MM-DD: "
        )
    while not is_future_date(task_date):
        task_date = input(
            "Data introdusă este în trecut. Introduceți o dată din viitor: "
        )
    task_category = input(f"Introduceți categoria ({', '.join(categories)}): ")
    while task_category not in categories:
        task_category = input(
            f"Categoria introdusă nu există. Introduceți o categorie validă ({', '.join(categories)}): "
        )
    # Fix : once task is is added category is deleted from the categories file and vice versa
    while not is_valid_category(task_category):
        task_category = input(
            f"Categoria introdusa este deja in lista. Introduceți o categorie validă ({', '.join(categories)}): "
        )
    task_person = input("Introduceti persoana responsabila: ")
    write_task(task_name, task_date, task_category, task_person)
    print("Task adăugat cu succes!")


def sort_method():
    sort_menu()
    with open("todolist.txt", "r") as f:
        tasks = [json.loads(line) for line in f]
    sortchoice = input("Alegeți o opțiune: ")
    if sortchoice == "1":
        print_tasks(sort_by_task(tasks))
    elif sortchoice == "2":
        print_tasks(reversed(sort_by_task(tasks)))
    elif sortchoice == "3":
        print_tasks(sort_by_date(tasks))
    elif sortchoice == "4":
        print_tasks(reversed(sort_by_task(tasks)))
    elif sortchoice == "5":
        print_tasks(sort_by_responsible(tasks))
    elif sortchoice == "6":
        print_tasks(reversed(sort_by_responsible(tasks)))
    elif sortchoice == "7":
        print_tasks(sort_by_category(tasks))
    elif sortchoice == "8":
        print_tasks(reversed(sort_by_category(tasks)))


def filter_method():
    filter_menu()
    with open("todolist.json", "r") as f:
        tasks = [json.loads(line) for line in f]
    for i, task in enumerate(tasks):
        task["index"] = i + 1
    filterchoice = input("Alegeți o opțiune: ")
    filterstring = input("Scrieti filtru: ")
    if filterchoice == "1":
        edit_method(filter_bytaskname(tasks, filterstring))
    elif filterchoice == "2":
        edit_method(filter_bytaskcategory(tasks, filterstring))
    elif filterchoice == "3":
        edit_method(filter_bytaskresponsible(tasks, filterstring))
    elif filterchoice == "4":
        edit_method(filter_bytaskdate(tasks, filterstring))


def edit_method(tasks):
    filter_menu()
    editchoice = input("Alegeți o opțiune: ")
    taskIndex = input("Alege indexul unui task: ")
    if editchoice == "1":
        tasks = edit_task(tasks, taskIndex)
    elif editchoice == "2":
        del tasks[taskIndex - 1]
    saveTasks(tasks)


def edit_task(tasks, taskIndex):
    categories = read_categories()
    task_name = input("Introduceți numele task-ului: ")
    while not is_valid_task(task_name):
        task_name = input("Taskul introdus este deja in lista. Specificati alt task: ")
    task_date = input("Introduceți data (YYYY-MM-DD): ")
    while not is_valid_date(task_date):
        task_date = input(
            "Data introdusă nu este validă. Introduceți data în formatul YYYY-MM-DD: "
        )
    while not is_future_date(task_date):
        task_date = input(
            "Data introdusă este în trecut. Introduceți o dată din viitor: "
        )
    task_category = input(f"Introduceți categoria ({', '.join(categories)}): ")
    while task_category not in categories:
        task_category = input(
            f"Categoria introdusă nu există. Introduceți o categorie validă ({', '.join(categories)}): "
        )
    # Fix : once task is is added category is deleted from the categories file and vice versa
    while not is_valid_category(task_category):
        task_category = input(
            f"Categoria introdusa este deja in lista. Introduceți o categorie validă ({', '.join(categories)}): "
        )
    task_person = input("Introduceti persoana responsabila: ")
    tasks[taskIndex - 1]["task"] = task_name
    tasks[taskIndex - 1]["date"] = task_date
    tasks[taskIndex - 1]["category"] = task_category
    tasks[taskIndex - 1]["responsible"] = task_person


def saveTasks(tasks):
    with open(filename, "w") as f:
        json.dump(tasks, f)


def sort_by_task(tasks):
    return sorted(tasks, key=lambda x: x["task"])


def sort_by_date(tasks):
    return sorted(tasks, key=lambda x: x["date"])


def sort_by_responsible(tasks):
    return sorted(tasks, key=lambda x: x["responsible"])


def sort_by_category(tasks):
    return sorted(tasks, key=lambda x: x["category"])


# Load the categories from the file
def read_categories():
    with open("category.txt", "r") as f:
        categories = [line.strip() for line in f]
    return categories


def is_valid_date(date_string):
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_task(task_name):
    with open(filename) as f:
        for line in f:
            task = json.loads(line.strip())
            if task["task"] == task_name:
                return False
        return True


def is_valid_category(task_category):
    with open(filename, "r") as f:
        for line in f:
            task = json.loads(line.strip())
            if task["category"] == task_category:
                return False
        return True


def is_future_date(date_string):
    date_today = datetime.datetime.now().strftime("%Y-%m-%d")
    if date_today < date_string:
        return True
    else:
        return False


def print_tasks(tasks):
    for task in tasks:
        print(
            f"{task['task']} / {task['date']} / {task['category']} / {task['responsible']}"
        )


def write_task(task_name, task_date, task_category, task_person):
    task = {
        "task": task_name,
        "date": task_date,
        "category": task_category,
        "responsible": task_person,
    }
    with open("todolist.txt", "a") as f:
        f.write(json.dumps(task) + "\n")


def filter_bytaskname(tasks, filterstring):
    filtered_tasks = filter(lambda task: task["task"] == filterstring, tasks)
    return list(filtered_tasks)


def filter_bytaskcategory(tasks, filterstring):
    filtered_tasks = filter(lambda task: task["category"] == filterstring, tasks)
    return list(filtered_tasks)


def filter_bytaskresponsible(tasks, filterstring):
    filtered_tasks = filter(lambda task: task["responsible"] == filterstring, tasks)
    return list(filtered_tasks)


def filter_bytaskdate(tasks, filterstring):
    filtered_tasks = filter(lambda task: task["date"] == filterstring, tasks)
    return list(filtered_tasks)


def main():
    while True:
        menu()
        choice = input("Alegeți o opțiune: ")
        if choice == "1":
            add_method()
        elif choice == "2":
            with open("todolist.json", "r") as f:
                tasks = [json.loads(line) for line in f]
            print_tasks(tasks)
        elif choice == "3":
            sort_method()
        elif choice == "4":
            filter_method()
        elif choice == "5":
            break


if __name__ == "__main__":
    main()
