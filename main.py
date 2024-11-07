import time
import os

def show_num(plastic_list, metal_list, otherwaste_list):
    print("Show the number of waste (1:plastic, 2:metal, 3:other):", end="")
    option = int(input())
    if (option == 1):
        print(len(plastic_list))
    elif (option == 2):
        print(len(metal_list))
    elif (option == 3):
        print(len(otherwaste_list))

def sorting(waiting_list, plastic_list, metal_list, otherwaste_list):
    count = 0
    while (count < len(waiting_list)):
        if (waiting_list[count] == "plastic"):  # BY AI recognition camera
            plastic_list.append(waiting_list[count])
        elif (waiting_list[count] == "metal"):  # BY AI recognition camera
            metal_list.append(waiting_list[count])
        else:                                   # BY AI recognition camera
            otherwaste_list.append(waiting_list[count])
        count += 1
    if count > 0:
        print("Sorting is done!")
    else:
        print("There is no waste in waiting list.")
    return [plastic_list, metal_list, otherwaste_list]

def add_waste():
    waiting_list = []
    plastic_list = []
    metal_list = []
    otherwaste_list = []
    system_boolean = True
    time.sleep(0.5)
    print("Different simulation of system (1:produce waste, 2:sorting, 3:show number of waste, 4:Quit):", end=" ")
    stimulation = int(input())
    if stimulation == 4:
        system_boolean = False
    while (system_boolean):
        if (stimulation == 1):
            print("Waste type (plastic,metal,other):", end=" ")
            waste_type = input()
            waiting_list.append(waste_type)
            print("Done")
        elif (stimulation == 2):
            all_list = sorting(waiting_list, plastic_list, metal_list, otherwaste_list)
            plastic_list = all_list[0]
            metal_list = all_list[1]
            otherwaste_list = all_list[2]
        elif (stimulation == 3):
            show_num(plastic_list, metal_list, otherwaste_list)
        elif (stimulation == 4):
            system_boolean = False
        print("Different simulation of system (1:produce waste, 2:sorting, 3:show number of waste, 4:Quit):", end=" ")
        stimulation = int(input())
    return [len(plastic_list),len(metal_list),len(otherwaste_list)]

def add():
    os.system('clear')
    flight_num = input("Please input the flight number: ")
    all_list = add_waste()
    plastic = all_list[0]
    metal = all_list[1]
    other = all_list[2]
    check = True
    with open('data.txt', 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if flight_num in lines[i]:
                lines[i] = f"{flight_num:^14}" + "|" + f"{plastic:^25}" + "|" + f"{metal:^23}" + "|" + f"{other:^23}|\n"
                check = False
                break
        if check == True:
            lines.append(f"{flight_num:^14}" + "|" + f"{plastic:^25}" + "|" + f"{metal:^23}" + "|" + f"{other:^23}|\n")
    with open("data.txt", 'w') as file:
        file.writelines(lines)
    file.close()
    print("Please type 'Enter' to return to menu.")
    input()
    print("We are directing you to the main menu...")
    time.sleep(1.5)
    os.system('clear')
    
def access():
    os.system('clear')
    print("1: All datum, 2: Specific flight data")
    choose = int(input("Your choice: "))
    if choose == 2:
        check = True
        flight_num = input("Please input the flight number: ")
        with open("data.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                if flight_num in line:
                    print(f"Datum of flight {flight_num} are as follow: ")
                    time.sleep(0.8)
                    print("flight_number | number of plastic waste | number of metal waste | number of other waste |")
                    print(line)
                    check = False
        file.close()
        if check == True:
            print(f"There is no flight number {flight_num}.")
    else:
        print("Datum are as follow: ")
        time.sleep(0.8)
        with open('data.txt', 'r') as file:
            print(file.read())
        file.close()
    print("Please type 'Enter' to return to menu.")
    input()
    print("We are directing you to the main menu...")
    time.sleep(1.5)
    os.system('clear')

def main():
    os.system('clear')
    time.sleep(0.5)
    print("Division of waste simulation")
    time.sleep(0.5)
    print("1: Add data, 2: Access data, 3: Quit ")
    option = int(input("Option: "))
    while (option == 1 or option == 2):
        if option == 1:
            add()
            print("1: Add data, 2: Access data, 3: Quit ")
            option = int(input("Option: "))
        elif int(option) == 2:
            access()
            print("1: Add data, 2: Access data, 3: Quit ")
            option = int(input("Option: "))
    os.system('clear')
main()

