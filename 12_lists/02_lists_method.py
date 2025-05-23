
marks = [8, 6, 10, 4, 2]

extra_marks = [35,50,60]

print(marks)

marks.append(15) # This will change original list
marks.pop()
marks.extend(extra_marks)
print(marks)