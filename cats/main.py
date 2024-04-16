def get_cats_info(path):
    cats = []

    try:
        with open(path, 'r') as file:
            lines = [el.strip() for el in file.readlines()]
    except FileNotFoundError:
        print('File is not found')

    for line in lines:
        id, name, age = line.split(',')
        cats.append({ 'id': id, 'name': name, 'age': age })

    return cats


print(get_cats_info('./data.txt'))
