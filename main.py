def show_num():
    global plastic_list
    global metal_list
    global tableware_list
    global otherwaste_list
    print("Show the number of waste (1:plastic, 2:metal, 3:tableware, 4:other):",end="")
    option = int(input())
    if (option==1):      
        print(len(plastic_list))
    elif(option==2):        
        print(len(metal_list))
    elif(option==3):    
        print(len(tableware_list))
    elif(option==4):                                           
        print(len(otherwaste_list))

def sorting():
    global waiting_list
    global plastic_list
    global metal_list
    global tableware_list
    global otherwaste_list
    count=0
    while (count<len(waiting_list)):
        if (waiting_list[count]=="plastic_type"):       #BY AI recognition camera
            plastic_list.append(waiting_list[count])
        elif(waiting_list[count]=="metal_type"):        #BY AI recognition camera
            metal_list.append(waiting_list[count])
        elif(waiting_list[count]=="tableware_type"):    #BY AI recognition camera
            tableware_list.append(waiting_list[count])
        else:                                           #BY AI recognition camera
            otherwaste_list.append(waiting_list[count])
        count+=1
    if count > 0:
        print("Sorting is done!")
    else:
        print("There is no waste in waiting list.")
    waiting_list=[]

#main program
waiting_list=[]
plastic_list=[]
metal_list=[]
tableware_list=[]
otherwaste_list=[]
system_boolean=True
while (system_boolean):
    print("Different stimulation of system (1:produce waste, 2:sorting, 3:show number of waste, 4:Quit):",end=" ")
    stimulation=int(input())
    if (stimulation==1):
        print("Waste type (plastic_type,metal_type,tableware_type,other_type):",end=" ")
        waste_type=input()
        waiting_list.append(waste_type)
        print("Done")
    elif (stimulation==2):
        sorting()
    elif (stimulation==3):
        show_num() 
    elif (stimulation==4):
        system_boolean=False
    

