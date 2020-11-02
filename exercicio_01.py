#!/usr/bin/env python3

"""
    Declare uma lista contendo as notas de 10 alunos
    Declare uma lista contendo os nomes dos 10 alunos
    Mostre a média das notas da turma
    Mostre a maior nota e o nome do respectivo aluno
    Monte uma lista com alunos aprovados e outras com alunos reprovados (critério para aprovação nota maior ou igual a 7)
"""

approved = list()
failed = list()    

def get_grades():
    return [9, 10, 5, 6, 9, 9, 10, 5, 6, 9]

def get_students():
    return ["A", "B", "C", "D", "E", "F", "G", "H", "I", "G"]

def isApproved(grade):
    if (grade >= 7):
        return True
    return False

def add_approved(stutent):
    approved.append(stutent)

def add_failed(stutent):
    failed.append(stutent)

def processes_grades():
    count = 0
    grades = get_grades()
    students = get_students()
    for n in grades:
        stutent = dict()
        
        stutent['name'] = students[count]
        stutent['grade'] = grades[count]
        
        if isApproved(grades[count]):
            add_approved(stutent)
            count += 1
            continue
        
        add_failed(stutent)
        count += 1

def show_approved():
    print("Approved:")
    for student in approved:
        print("\tName:", student['name'])
        print("\tGrade:", student['grade'], "\n")

def show_failed():
    print("Failed:")
    for student in failed:
        print("\tName:", student['name'])
        print("\tGrade:", student['grade'], "\n")

if __name__ == '__main__':
    processes_grades()
    show_approved()
    show_failed()