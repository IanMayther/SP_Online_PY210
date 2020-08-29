#!/usr/bin/env python3

#DELIVERABLES
'''
Use dicts where appropriate.
See if you can use a dict to switch between the user’s selections.
See if you can use a dict to switch between the users selections. see Using a Dictionary to switch for what this means.
Convert your main donor data structure to be a dict. - Complete
Try to use a dict and the .format() method to produce the letter as one big template, rather than building up a big string that produces the letter in parts.
'''

#Donors
donors = {"Morgan Stanely": [0.01, 20.00],
            "Cornelius Vanderbilt": [800, 15, 10.00],
            "John D. Rockefeller": [7000, 150.00, 25],
            "Stephen Girard": [60000],
            "Andrew Carnegie": [0.04, 999.99]}

#Single Thank You
def receiver():
    #Determine Previous Donor
    new_vs_ex = input("New Donor [Y/N]? ")

    if new_vs_ex.lower() == "y":
        name = new_donor()
    elif new_vs_ex.lower() == "quit":
        name = "quit"
    else:
        i = 1
        temp_list = []
        for key in sorted(donors):
            print(f"[{i}] - {key}")
            i += 1
            temp_list.append(key)

        donor_name = input("Who gave the donation [#]? ")

        if donor_name.lower() == "quit":
            name = "quit"

        name = temp_list[int(donor_name)-1]

    don_val = 0

    for k, v in donors.items():
        if k == name:
            don_val = sum(v)
    
    print("\n" + email(name, don_val))

    return name


#New Donor
def new_donor():
    name_of_new = input("What is the New Donor's Name: ")
    if name_of_new not in donors:
        dol_val = gift()
        donors[name_of_new] = [dol_val]
    return name_of_new


#Donor Verification
def ver_don(giver):
    exist = False
    for i in range(len(donors)):
        if giver == donors[i][0]:
            exist = True
        else:
            exist = False
    return exist

#Get Value of Donation
def gift():
    while True:
        try:
            value = float(input("What is the value of the donation: "))
            break      
        except ValueError:
            print("Not a valid donation value")
    return value


#Print Email
def email(to_donor, gift_amount):
    name = to_donor
    donation = gift_amount
    body = f"""Greetings {name}\n
\n
Thank you so much for your generous contribution to our charity.\n
It is donors like you who make our work of building schools for ants' possible.\n
With your gift of ${donation}, means (10) or (20) more schools can be built to help the ants learn to read.\n
\n
Sincerely,\n
Derek Zoolander\n
Founder and C.E.O. of Derek Zoolander Charity for Ants Who Can't Read Good (DZCAWCRG)"""
    return body


#Create Report
def print_report(my_List = []):
    #Header
    print("{0:<25s}|{1:^15s}|{2:^15s}|{3:>12s}".format("Donor Name", "Total Given", "# of Gifts","Avg. Gift"))
    print("-" * 72)
    #Table Data
    for i in range(len(my_List)):
        #Process Data
        #Donor
        col = my_List[i][1]
        #Sum Total 
        total = sum(col)
        #Gift Count  
        No_Gifts = len(my_List[i][1])
        #Calc Average
        Ave_Gift = total / No_Gifts
        #Print Table
        print("{0:<25s}${1:>14.2f}{2:>17d}  ${3:>11.2f}".format(my_List[i][0],total, No_Gifts, Ave_Gift, end =''))    
    return

#Send Letter
def send_letter():
    print("Sending Letter")
    pass

def quit():
    print("Quitting, Thank you.")
    return "quit"

#Main Menu Options
def main_menu(prompt, dict_choice):
    while True:
        choice = input(prompt)
        if dict_choice[choice]() == "quit":
            break

choice_menu = ("Choose an Action:\n"
            "\n"
            "1 - Send Thank You to Single Donor.\n"
            "2 - Create Report.\n"
            "3 - Send Letters to ALL Donor.\n"
            "4 - Quit.\n")

main_selections = {"1" : receiver,
                    "2" : print_report,
                    "3" : send_letter,
                    "4" : quit,
                    }
    

#Main Exicutable
if __name__ == '__main__':
    main_menu(choice_menu, main_selections)
'''
        directive = input("What would you like to do; [1]Send Thank you, [2]Create Report, [3]Quit: ")
        if directive == "1" or directive == "2" or directive == "3":
            if directive == "1":
                #Launch Send Thank you
                grat = input("Who would you like to send a Thank You to? Enter 'list' for a list of previous donors.  ")
                #Quit Code
                if grat.lower() == "quit":
                    continue
                recipient = receiver(grat)
                if recipient.lower() == "quit":
                    continue
                ver_don(recipient)
                contr = gift()
                if contr == "quit":
                    continue
                if not ver_don:
                    new_donor = [recipient[:-1], (contr)]
                    #donors1.append(new_donor)
                    print(email(new_donor[0][0],new_donor[0][1]))
                else:
                    for i in range(len(donors)):
                        if recipient == donors[i][0]:
                            donors[i][1].append(contr)
                            print(donors)
                    print(email(recipient, contr))
            elif directive == "2":
                #Launch Create Report
                print("Create Report")
                print_report(donors1)
            elif directive == "3":
                #Quit
                print("Quitter")
                real_response = True
        else:
            print("Please select one of the options above")
'''