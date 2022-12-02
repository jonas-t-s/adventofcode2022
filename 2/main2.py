import os

file = "input"
readedlines = []
with open(file) as f:
    for line in f.readlines():
        readedlines.append((line[0],line[-2]))
sol = []
for line in readedlines:
    match line[0]:
        case "A": #Rock
            match line[1]:
                case "X": #loose
                    sol.append((line[0], "Z"))
                case "Y": #draw
                    sol.append((line[0], "X"))
                case "Z": #win
                    sol.append((line[0], "Y"))
        case "B": # Paper
            match line[1]:
                case "X": #loose
                    sol.append((line[0], "X"))
                case "Y": #draw
                    sol.append((line[0], "Y"))
                case "Z": #win
                    sol.append((line[0], "Z"))
        case "C": # Scissors
            match line[1]:
                case "X": #loose
                    sol.append((line[0], "Y"))
                case "Y": #draw
                    sol.append((line[0], "Z"))
                case "Z": #win
                    sol.append((line[0], "X"))
readedlines = sol
score = 0
for line in readedlines:
    match line[0]:
        case "A": # Rock
            match line[1]:
                case "Y": # Paper
                    score += 8
                case "X": # Rock
                    score += 1+3
                case "Z": #Scissors
                    score += 3
        case "B": # Paper
            match line[1]:
                case "Y": # Paper
                    score += 3+ 2
                case "X": # Rock
                    score += 1+0
                case "Z": #Scissors
                    score += 3+6
        case "C":  # Scissors
            match line[1]:
                case "Y":  # Paper
                    score += 2
                case "X":  # Rock
                    score += 1 + 6
                case "Z":  # Scissors
                    score += 3 + 3
print(score)