import string
if __name__ == '__main__':
    alphabet = list(string.ascii_uppercase)
    students = [[input(), float(input())] for _ in range(int(input()))]
    scores = [student[1] for student in students]
    lowest = min(scores)
    students = [student for student in students if student[1] != lowest]
    scores = [student[1] for student in students]
    second_lowest = min(scores)
    students = [student[0] for student in students if student[1] == second_lowest]
    for student in sorted(students):
        print(student)
