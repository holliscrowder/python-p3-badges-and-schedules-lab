def badge_maker(name):
    # print(f"Hello, my name is {name}.")
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    i = 0
    badge_list = []
    while i < len(names):
        badge_list.append(badge_maker(names[i]))
        i += 1
    # print(badge_list)
    return badge_list


def assign_rooms(names):
    i = 0
    room_list = []
    while i < len(names):
        room_list.append(f"Hello, {names[i]}! You'll be assigned to room {i+1}!")
        i += 1
    # print(room_list)
    return room_list


def printer(names):
    i = 0
    while i < len(names):
        print(batch_badge_creator(names)[i])
        i += 1
    j = 0
    while j < len(names):
        print(assign_rooms(names)[j])
        j += 1
    return None


printer(["Arel", "Carol"])
