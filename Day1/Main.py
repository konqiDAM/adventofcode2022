print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
lastSum: int = 0
calories_sum: int = []
for calories in contents:
    if calories != "":
        lastSum += int(calories)
    else:
        calories_sum.append(int(lastSum))
        lastSum = 0
calories_sum.sort()
#print(caloriesSum[-3:])
totalSum = 0
for cal in calories_sum[-3:]:
    totalSum += cal
print(calories_sum[-1])
print(totalSum)
