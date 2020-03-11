import sys


def load_from_storage():
    with open('ideas_list.txt', 'r') as storage:
        return storage.readlines()


draft = load_from_storage()


def ask():
    idea = input('What is your new idea? ')
    idea = f'{idea}\n'
    draft.append(idea)
    return draft


def draft_printout():
    item_no = 0
    for item in draft:
        item_no += 1
        print(f'{item_no}. {item}')


def save_to_storage():
    with open('ideas_list.txt', 'w') as storage:
        for item in draft:
            storage.write(item)


def delete_item():
    try:
        item_index = int(sys.argv[2]) - 1
        if int(sys.argv[2]) > len(sys.argv) or int(sys.argv[2]) < 0:
            print('The index number you have entered is invalid!')
        else:
            del draft[item_index]
            draft_printout()
            return item_index
    except (IndexError, ValueError):
        print('Specify a number after --delete')


while 1 == 1:
    try:
        if sys.argv[1] == '--list':
            draft_printout()
            break
        elif sys.argv[1] == '--delete':
            delete_item()
            save_to_storage()
            break
    except IndexError:
        ask()
        draft_printout()
        save_to_storage()
