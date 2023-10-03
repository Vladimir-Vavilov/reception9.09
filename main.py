from pprint import pprint


def op_file():
    with open('reception.txt', 'rt') as f:
        cook_book = {}
        for line in f:
            eat_name = line.strip()
            ingredient_name = int(f.readline())
            meas = []
        for i in range(ingredient_name):
            mea = f.readline()
            ingredient, quantity, measure = mea.split(' | ')
            meas.append({
                'ingredient_name': ingredient,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[eat_name] = meas
    pprint(cook_book)


def my_cook_book():
    with open('reception.txt', encoding='utf-8') as file:
        cook_book = {}
        for txt in file.read().split('\n\n'):
            name, _, *args = txt.split('\n')
            tmp = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = tmp
    return cook_book


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюдо: ').split(', ')
    dishes = [dish.capitalize() for dish in dishes]

    shop_list = get_shop_list_by_dishes(dishes, person_count)

    return shop_list


def update_shoplist(my_cook_book, ingrigient_name, measure):
    if ingrigient_name in my_cook_book:
        my_cook_book[ingrigient_name].append(measure)
    else:
        new_key = 2 * ingrigient_name
        if new_key in my_cook_book:
            my_cook_book[new_key].append(measure)
        else:
            my_cook_book[new_key] = [measure]



def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    my_cookbook = my_cook_book()
    for dish in dishes:
        if dish not in my_cookbook:
            print(f"Блюдо '{dish}' не найдено в книге рецептов.")
            continue
        for ingredient in my_cookbook[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            if ingredient_name in shop_list:
                shop_list[ingredient_name] += quantity
            else:
                shop_list[ingredient_name] = quantity
    return shop_list


pprint(create_shop_list())

print(get_shop_list_by_dishes(["Омлет", "Омлет"],2))
person_count = 2
dishes = ['Омлет', 'Омлет']