
# String Formating

template = "Dear {} , You are awesome, take this ${} bag."

a = "John"
a1 = 10000

b ="Robert"
b1 = 11000

c = "kim"
c1 = 500

s1 = template.format(a,a1)

print(s1)

print(f"Dear {c},you are awesome, you won ${c1} bag")