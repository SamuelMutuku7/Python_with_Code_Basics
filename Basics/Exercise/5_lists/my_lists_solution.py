expenses = [2200, 2350, 2600, 2130, 2190]

feb_diff = expenses[1] - expenses[0]
print(f"In Feb, I spent an extra amount of {feb_diff} over Jan")

q1_expenses = expenses[0] + expenses[1] + expenses[2]
print(f"Total expense in Q1: {q1_expenses}")

for i in range(len(expenses)):
    if expenses[i] == 2000:
        print(f"2000 was spent in month {i+1}")
        break
    else:
        print("2000 was not spent in any month")
        break

expenses.append(1980)
print(expenses)

expenses[3] = expenses[3] - 200
print(expenses)
