def print_list(lst):
    return lst


def append_list(lst, item):
    lst.append(item)
    return lst


def remove_list(lst, item):
    if item not in lst:
        return f"'{item}' not found in list"
    lst.remove(item)
    return lst


def extend_list(lst, new_items):
    lst.extend(new_items)
    return lst


def insert_list(lst, index, item):
    lst.insert(index, item)
    return lst


def pop_list(lst):
    if not lst:
        return "List is empty"
    lst.pop()
    return lst


def sort_list(lst):
    lst.sort()
    return lst


def reverse_list(lst):
    lst.reverse()
    return lst


def count_list(lst, item):
    return lst.count(item)


def index_list(lst, item):
    if item not in lst:
        return f"'{item}' not found"
    return lst.index(item)


def copy_list(lst):
    return lst.copy()


def clear_list(lst):
    lst.clear()
    return lst


default_list = ["start", "stop", "pause"]
print(default_list)
print(append_list(default_list, "reset"))
print(remove_list(default_list, "start"))
print(extend_list(default_list, ["run", "walk"]))
print(insert_list(default_list, 2, "jump"))

