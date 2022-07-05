students=open("St_students.txt")
all_students=[stud.rstrip("\n") for stud in students]
print(all_students)
failed = open("St_failed.txt")
failed_stud = [fail.rstrip("\n") for fail in failed]
print(failed_stud)

passed = open("St_passed.txt", "w")
passed_students = set(all_students) - set(failed_stud)  # here we use set because set does not store duplicates
print(passed_students)
for st in passed_students:
    st += "\n"
    passed.write(st)

fp = open("St_passed.txt", "a")
name = "surej"
fp.write(name)
