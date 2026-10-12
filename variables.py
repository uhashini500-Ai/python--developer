pi = 22 / 7

print("Value of pi:", pi)
print("Data type of pi:", type(pi))

print("\nUsing 'for' as a variable name:")

try:
    exec("for = 4")
except SyntaxError:
    print("SyntaxError: 'for' is a reserved keyword.")

for_value = 4
print("Correct variable value:", for_value)

principal = 10000
rate = 5
time = 3

simple_interest = (principal * rate * time) / 100

print("\nPrincipal:", principal)
print("Rate:", rate)
print("Time:", time, "years")
print("Simple Interest:", simple_interest)