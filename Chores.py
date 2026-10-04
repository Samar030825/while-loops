total_chores = 4
original_count = total_chores
print(f"You have {original_count} to finish today \n")
completed_count = 0
chore_num = 1

while chore_num <= total_chores:
    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    elif chore_num == 3: next_chore = "take out the trash"
    else: next_chore = "Finish the dishes"
    answer = input(f"Have you finished : {next_chore} ? (yes/no) ")

    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Gret job  Chore completed")
    else:
        print("OKay . Finish it and check again")
    print("chore_remaining : " , total_chores - completed_count)
    print()

print("All chores complete")
print("Great work . Finished your entire checklist today")
print("now lets safely peek at a infinity loop . . . . . . .")
test_value  = 0
safety_counter = 0
while test_value <= 0 :
    print("This  condition never changes . So this would run forever .")
    safety_counter += 1
    if safety_counter==3:
        print("Stopping here on purpose . A real loop never stop on it own")
        break
    
print("====================================================")
print("==== Chore Summary List====")
print("Chores Assigneed Today : " , original_count)
print("Chores completed : " , completed_count)
print("Chores remaining : " , total_chores - completed_count)
print("=====================================================")
