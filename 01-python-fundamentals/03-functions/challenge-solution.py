def process_grades(*grades):
    if len(grades) == 0:
        return 0.0, 0, 0

    total = 0.0
    count = 0
    for g in grades:
        total = total + g
        count = count + 1

    average = total / count
    return average, max(grades), min(grades)

s = input('Enter grades separated by spaces (or press Enter for none): ').strip()
if s == '':
    avg, mx, mn = process_grades()
else:
    parts = s.split()
    grades = []
    for p in parts:
        try:
            val = float(p)
        except:
            print('Skipping invalid grade:', p)
            continue
        grades.append(val)

    avg, mx, mn = process_grades(*grades)

print('Average: %.2f' % avg)
print('Max:', mx)
print('Min:', mn)
