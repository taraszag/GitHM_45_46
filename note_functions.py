# Create user

def create_user(data_base, name, password):
    l = list()
    l.insert(0, name)
    l.append(password)
    data_base.append(l)
    return data_base


# Create note
def create_user_note(data_base, name, note):
    for i in range(len(data_base)):
        if data_base[i][0] == name:
            data_base[i].append(note)
            return note


# Read Users
def read_users(data_base):
    print('User ID\t\tUser Name')
    for i in range(len(data_base)):
        print(f'\t{i}\t\t{data_base[i][0]}')


# Read Notes
def read_user_notes(data_base, name, password, note):
    print('User ID\t\tUser Name\t\tPassword \t\tUser Notes')
    for i in range(len(data_base)):
        if data_base[i][0] == name and data_base[i][1] == password:
            print(f'\t{i}\t\t{data_base[i][0]}\t\t{len(password) * "*"}\t\t\t\t{data_base[i][2:]}')
        # for j in range(len(data_base)):
        #     if data_base[j][1] == password:
        #         print(f'\t{j}\t\t{len(password) * "*"}\t\t\t\t{data_base[i][2:]}')
        #         return name,note

# Update Note
def update_user_note(data_base, name, old_note, new_note, password):
    print('User ID\t\tUser Name')
    for i in range(len(data_base)):
        if data_base[i][0] == name and data_base[i][1] == password:
            for j in range(1, len(data_base[i])):
                if data_base[i][j] == old_note:
                    data_base[i][j] = new_note
                    return new_note


#  Delete
def del_notes(data_base, name, del_note, password):
    for s in range(len(data_base)):
        if data_base[s][0] == name and data_base[s][1] == password:
            for i in range(len(data_base)):
                for j in range(2, len(data_base[i])):
                    if data_base[i][j] == del_note:
                        del data_base[i][j]
                        return data_base
