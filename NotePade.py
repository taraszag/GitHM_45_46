# Нашел только одну ошибку, если не было записи тогда выкидывало с программы, решил ее через Try, Except.
import note_functions as nf

db = []
print("Hello this is NotePade")

while True:
    command = str(input(f"Create user[cu]\n"
                        f"Create note [cn]\nRead Users [ru]\nRead Notes [rn]\nUpdate Note[un]"
                        f"\nDelete note [dn]\nPrint command:  "))
    # Create user
    if command == 'cu':
        name = input("Enter yor name : ")
        password = input('Enter your password: ')
        nf.create_user(db, name, password)
    # Create note
    elif command == 'cn':
        name = input('Enter your name: ')
        note = input("Enter your notes:")
        nf.create_user_note(db, name, note)
    # Read Users
    elif command == 'ru':
        nf.read_users(db)
    # Read Notes
    elif command == 'rn':
        name = input('Enter user name:')
        password = input('Enter password: ')
        try:
            nf.read_user_notes(db, name,password, {note})
        except:
            print('No notes found. Create note!')


    # Update Note
    elif command == 'un':
        name = input('Enter your name: ')
        password = input("Enter your password:")
        new_note = input("Enter new note :")
        old_note = input("Enter old note :")
        nf.update_user_note(db, name, old_note, new_note, password)
    #  Delete
    elif command == 'dn':
        name = input('Enter your name: ')
        password = input('Enter your password: ')
        del_note = input('Enter note to delete: ')
        nf.del_notes(db, name, del_note, password)

    e = str(input("Enter anykey to continue or Enter to exit: "))
    if not (e):
        break
