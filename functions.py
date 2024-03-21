FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Writes todos list into a text file.
    Default: 'todos.txt'.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
    print("Todos updated on disk.")


if __name__ == '__main__':
    print('hello from functions')
