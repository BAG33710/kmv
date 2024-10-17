people_limit = 4
people = ""

while (True):
    print("-" * 50)
    print("Введите:")
    print(" - 1, если хотите добавить пациента в очередь;")
    print(" - 2, если хотите посмотреть текущую очередь.")
    print("-" * 50)

    choice = input()

    if choice == '1':
        if len(people.split(", ")) < people_limit:
            fio = input("Введите ФИО пациента: ").strip()
            if people:
                people += f", {fio}"
            else:
                people = fio
        else:
            print(f"Текущая очередь - {people}")
            break
    elif choice == '2':
        if people:
            print(f"Текущая очередь - {people}")
        else:
            print("Очередь пустая!")
