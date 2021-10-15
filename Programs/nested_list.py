# Given the names and grades for each student in a class of students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == "__main__":
    students = []
    print("Enter the names and scores of students:")
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    students = sorted(students, key=lambda x: x[1])
    # print(students)
    # second_lowest_score=students[1][1]
    second_lowest_score = sorted(list(set(x[1] for x in students)))[1]
    required_data = []
    for stu in students:
        if stu[1] == second_lowest_score:
            required_data.append(stu[0])
    print("\nstudent(s) having the second lowest grade:")
    print("\n".join(sorted(required_data)))
