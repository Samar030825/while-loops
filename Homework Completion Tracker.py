total_homework = 4
original_count = total_homework
print(f"You have {original_count} homework to complete today!\n")

completed_count = 0
task_num = 1

while task_num <= total_homework:

    if task_num == 1:
        next_task = "Math Worksheet"
    elif task_num == 2:
        next_task = "Science Learning"
    elif task_num == 3:
        next_task = "English Writing"
    else:
        next_task = "Coding Practice"

    answer = (f"Have you finished {next_task}? (Yes/No) ")

    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("Great job! homework task completed")
    else:
        print("Okay , finish it and check again")

    print("Homework remaining : " , total_homework - completed_count)
    print()

print("====ALL HOMEWORK COMPLETED===")
print("GREAT WORK COMPLETING ALL THE HOMEWORK")


print(Now 
