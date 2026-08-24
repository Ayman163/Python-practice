scores = [45, 88, 72, 91, 53, 60, 30, 95, 82]

maxv = scores[0]
avgv = 0
passed_scores = []
alll = 0
tolel = 0

for i in scores:
    if i > max:
        max = i
    alll += 1
    tolel += i
    if i >= 50:
        passed_scores.append(i)

print("The max score is", max)
avg = tolel / alll
print("The average score is", avg)
print("The passed scores are", passed_scores)

    
