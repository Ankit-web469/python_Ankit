#pass or fail
sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))

total_marks = sub1 + sub2 + sub3
percentage = (total_marks / 300) * 100


if sub1 < 33 or sub2 < 33 or sub3 < 33:
    print("Result: Fail (Scored less than 33% in a subject)")
elif percentage < 40:
    print(f"Result: Fail (Overall percentage is {percentage:.2f}%, less than 40%)")
else:
    print(f"Result: Pass (Overall percentage is {percentage:.2f}%)")
