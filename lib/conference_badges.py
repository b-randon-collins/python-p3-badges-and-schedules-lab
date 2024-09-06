def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    rooms = range(1, 9)
    assignments = []
    room_index = 1

    for name in names:
        assignment = f"Hello, {name}! You'll be assigned to room {room_index}!"
        assignments.append(assignment)
        room_index += 1
    

    
    return assignments

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    
    output = "\n".join(badges) + "\n"
    for assignment in room_assignments:
        output += assignment + "\n"
    
    return output

def printer(names):
    badges = batch_badge_creator(names)
    assignments = assign_rooms(names)
    
    combined_messages = badges + assignments
    
    for message in combined_messages:
        print(message)