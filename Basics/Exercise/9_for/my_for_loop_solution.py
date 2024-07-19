result = [
    "heads",
    "tails",
    "tails",
    "heads",
    "tails",
    "heads",
    "heads",
    "tails",
    "tails",
    "tails",
]

count = 0
for toss in result:
    if toss == "heads":
        count += 1

print("The heads count is:", count)

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in int_list:
    if num % 2 != 0:
        print(num * num)

expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January", "February", "March", "April", "May"]

expense = int(input("Enter an expense amount: "))
month = -1
for i in range(len(expense_list)):
    if expense == expense_list[i]:
        month = i
        break

if month != -1:
    print(f"You spent {expense} in {month_list[month]}")
else:
    print(f"You didn't spend {expense} in any month")

for mile in range(5):
    print(f"You ran {mile + 1} miles")
    tired = input("Are you tired? ").lower()
    if tired == "yes":
        print(
            "You didn't finish the race but you still ran",
            mile + 1,
            "miles. Well done!",
        )
        break
else:
    print("Congratulations! You finished the race.")

for i in range(1, 6):
    star = ""
    for j in range(i):
        star += "*"
    print(star)
