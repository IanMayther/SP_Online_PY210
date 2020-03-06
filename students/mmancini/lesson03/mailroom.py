#!/usr/bin/env python3


db_donors = [("Jane Smith", [25, 50]),
             ("Tom Adams", [100]),
             ("Helen Smalls", [10,20,30]),
             ("Ming Chan", [50]),
             ("Mary Jones", [5, 10, 15])]

####################################


def menu_donation_amount():
    msg = ""
    msg += "Please enter a donation amount::\n"
    msg += ".....>>"

    # donation_amount_entry = input(msg)
    donation_amount_entry = 55      # ***MMM

    return donation_amount_entry


def show_donors():
    print(f"List of Donors:")
    for donor in db_donors:
        # print(f"diag spin donors, donor ==> ", donor[0])
        print(f" ", donor[0])


def process_new_donor(name):
    print(f"process a new donor ==> ", name)
    amount_ary = []

    amount = menu_donation_amount()
    amount_ary.append(amount)

    db_donors.append((name,amount_ary))
    #donor_donations.append((user_action_TY, [donation]))

    print(f"***MMM diag , donations >=> ", db_donors)


def process_existing_donor(name):
    print(f"process existing donor ==> ", name)

    donor_names_lst = [x[0] for x in db_donors]
    x = donor_names_lst.index(name)

    amount = menu_donation_amount()
    #for d in db_donors:
    #    d[1].append(3)
    db_donors[x][1].append(amount)
    print(f"existing donor {name} donated {amount}")
    #print(db_donors)

    print(x)

def process_donor(in_name):

    donor_names_lst = [x[0] for x in db_donors]

    if in_name in donor_names_lst:
        process_existing_donor(in_name)
    else:
        process_new_donor(in_name)

    ix = -1
    for donor in db_donors:
        #print(f"diag spin donors, donor ==> ", donor[0])
        i=1

        #if donors[0] == user_action_TY:
        #        donors[1].append(donation)

        i = 1


def send_thankyou():
    msg = ""
    msg += "Please enter donor name or 'list' for list of donors:\n"
    msg += ".....>>"

    entry = ""
    need_entry = True
    while need_entry:
        # entry = input(msg)

        entry = 'Phil Mason'
        # entry = 'Tom Adams'
        #entry = 'list'
        print(f"user entered ==> ", entry)

        if entry.lower() == 'list':
            show_donors()
        else:
            # have a donor name
            need_entry = False

        break   # ***MMM test only

    process_donor(entry)


def main_menu():
    msg = ""
    msg += "Please enter option from below:\n"
    msg += " S: Send thank you note\n"
    msg += " C: Create report\n"
    msg += " Q: Quit\n"
    msg += ".....>>"

    # entry = input(msg)

    entry = 'S'
    print(f"user entered ==> ", entry)

    if entry == 'S':
        send_thankyou()

    """
    if user_action == 'S'
        create_a_report()
    elif user_action == '3':
        quit()
    else:
        print('Invalid input. Please choose 1, 2 or 3.')


    """
    return entry

###################################


def mailroom():
    print("mailroom begin")

    # exit()

    is_done = False
    while True:
        operation = main_menu()

        if operation == 'Q':
            is_done = True

        is_done = True  # ***MMM

        if is_done:
            break

    print("mailroom end")


###################################


# main, test funcs

if __name__ == "__main__":
    mailroom()

