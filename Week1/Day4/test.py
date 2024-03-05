magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def make_great():
    global magician_names
    magician_names = [f"{name} the Great" for name in magician_names]

make_great()