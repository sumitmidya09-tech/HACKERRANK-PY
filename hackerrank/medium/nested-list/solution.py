if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    second = sorted(set(score for name, score in students))[1]

    names = [name for name, score in students if score == second]

    for name in sorted(names):
        print(name)
