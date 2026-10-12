# 1. List of friends' names and list of tuples with name and length
friends_names = ["Rahul", "Priya", "Aditya", "Divya", "Karthik"]
name_length_tuples = [(name, len(name)) for name in friends_names]

print("Friends and their name lengths:")
print(name_length_tuples)

# 2. Expense Tracking and Comparison
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses for each
total_your_expenses = sum(your_expenses.values())
total_partner_expenses = sum(partner_expenses.values())

print(f"\nYour Total Expenses: {total_your_expenses}")
print(f"Partner's Total Expenses: {total_partner_expenses}")

# Determine who spent more money overall
if total_your_expenses > total_partner_expenses:
    print("You spent more money overall.")
elif total_partner_expenses > total_your_expenses:
    print("Your partner spent more money overall.")
else:
    print("Both of you spent the same amount overall.")

# Find the expense category with the significant difference
max_difference = -1
significant_category = ""

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_difference:
        max_difference = diff
        significant_category = category

print(f"\nCategory with the largest spending difference: {significant_category} (Difference: {max_difference})")