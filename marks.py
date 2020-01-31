print("The Mark Calculator Made by SnowLeoo")

"""

"""

num_marks = int(input("How much Marks do you have?"))
i = 0
total_marks = 0


for i in range(num_marks):
    current_mark = int(input("What is the next mark?"))
    total_marks = total_marks + current_mark
    print(total_marks)

end_marks = total_marks / num_marks

round(end_marks, 1)

print("Your average Mark is " + str(end_marks))