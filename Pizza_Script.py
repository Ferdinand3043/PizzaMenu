print("\nwelcome ~" "\n\nThis is version 1 of my pizzeria order program.....enjoy! :)")

input("\nPress Enter to continue...")

start = input("\nWe have a varity of menu options. Would you like to see a preview of the menu?" + str("\n\nEnter yes or no : "))



if start == "yes" or start == 'Yes' or start == 'YES':
        print("\nMenu Items:")
        food = ['\nPizza', 'Mozzarella sticks', 'Mozzarella Bites ', 'Zucchini Fries ', 'Classic Caesar Salad ', 'etc....']
        for item in food:
            print(item)
            continue
if start == "no" or start == 'No' or start == 'NO':
    print('\nOkay!')
    
            

order = (input('\nCan you please provide all the items you would like to order today: '))
print('\n\tOrder Details:')
print(order)

order_confirm = input('\nIs everything looking good for your order? '+ ('\n\nEnter Yes or No: '))

while True:
    order_list = []
    if order_confirm == "no" or order_confirm == 'No' or order_confirm == 'NO':
        addtional = input('\nWhat else would you like added? ')
        print('\n\tOrder Details:')
        print('add', addtional)
        Last_chance = input('\nAnything else?' + ('\n\nEnter Yes or No: '))
        if Last_chance ==  "no" or order_confirm == 'No' or order_confirm == 'NO':
                print('\nGreat!')    
                break
        else: 
            continue
    else:
        print('\nGreat!')    
        break


print('\n\tPlease enter card details as instructed')

card = input('\nWhat is the card number?: ')
date = input('\nWhat is the month/year?: ')
security = input('\nWhat is the 3 digit code on the back?: ')

print("\nThank you for the information. So we have ->" + "\n\nCard Number: " + card + "\nDate: " + date + "\nSecurity Code: " + security)

details = input('\n\tIs this information accurate? ')

while True: 
    if details == 'no' or details == 'No' or details == 'NO':
        print('\n\tPlease re-enter details!')
        card = input('\nWhat is the card number?: ')
        date = input('\nWhat is the month/year?: ')
        security = input('\nWhat is the 3 digit code on the back?: ')
        confirm = input('\n\tIs this information accurate? ')
        if confirm == 'yes' or confirm == 'Yes' or confirm == 'YES':
            break
        else:
            continue
    if details == 'yes' or details == 'Yes' or details == 'YES':
        break

print("\nPlease fill out address details:")

street = input('\nWhat is the street? ')
city = input('\nWhat is the city?: ')
state = input('\nWhat is the state?: ')
zip = input('\nWhat is the zip code?: ')

print("\nThank you for the information. So we have ->" + "\n\nStreet: " + street + "\nCity: " + city + "\nState: " + state + "\nZip: " + zip)

while True: # last infinate loop 
    delivery = input('\n\tIs this the best address? ')
    if delivery == 'No' or delivery == 'no' or delivery == 'NO':
        print('\n\tPlease re-enter details!')
        street = input('\nWhat is the street? ')
        city = input('\nWhat is the city?: ')
        state = input('\nWhat is the state?: ')
        zip = input('\nWhat is the zip code?: ')
        continue
    if delivery == 'Yes' or delivery == 'yes' or delivery == 'YES':
        break

Farewell = print('\nThank you for stopping by and testing my program out.' + '\n\tSee you around! :)')
print(Farewell)


