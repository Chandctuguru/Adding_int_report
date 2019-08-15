# [ ] create, call and test the adding_report() function
# then PASTE THIS CODE into edX
def adding_report(report):
    print(" Input an integer to add to the total or \"Q\" to quit")
    item_all = "Items"
    total_sum = 0
    while True:
        user_input = input("Enter an integer or \"Q\":")
        if user_input.isdigit()==True:
            if report.upper()=='A':
                item_all = item_all + "\n" + user_input
                total_sum = int(user_input) + total_sum
            else:
                total_sum = int(user_input) + total_sum
        elif user_input.upper().startswith('Q'):
            if report.upper()=='A':
                print()
                print(item_all)
                print()
                print("Total\n"+str(total_sum))
            else:
                print()
                print("Total\n"+str(total_sum))
            break
        else:
            print(user_input,"is invalid input")
print(" Report Types include All Items (\"A\") or Total Only (\"T\")")
while True:
    report_input = input("Choose Report Type (\"A\" or \"T\"): ")
    if report_input.upper() == 'A':
        print()
        adding_report(report_input)
        break
    elif report_input.upper() == 'T':
        print()
        adding_report(report_input)
        break
    else:
        print(report_input," is invalid input")
