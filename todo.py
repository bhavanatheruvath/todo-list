print("\n\n\t\t\tTo-Do List")
print("\nEnter A to add new To-Do.\nEnter D to delete To-Do.\nEnter U to update To-Do.\nEnter E to exit To-Do.\nEnter L to check To-Do List.")

to_do=[]
del_todo=[]

while True:
    user_input=input("\n\n\nWhat do you want to do?(A,D,U,E,L):")
    if user_input=="A":
        add=input("Enter your To-Do:")
        to_do.append(add)

    elif user_input=="D":
        dlt=input("Enter the  item you want to delete:")
        to_do.remove(dlt)
        del_todo.append(dlt)

    elif user_input=="U":
        udt=input("Enter the item you have finished:")
        index=to_do.index(udt)
        to_do[index]=udt+"✓"

    elif user_input=="L":
        print("\n+---------------+\n    To-Do\n+---------------+")
        for i in to_do:
            print('•',i) 

    elif user_input=="E":
        print("\n+--------------------+\n    Dash Board\n+--------------------+")
        for i in to_do:
            print('•',i)
        print("\n+--------------------+\n    Deleted List\n+--------------------+")
        for j in del_todo:
            print('•',j)
        break