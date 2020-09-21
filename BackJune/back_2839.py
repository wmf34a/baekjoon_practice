sugar_kg = int(input())
total_cnt = 0

while True:
    if sugar_kg % 5 == 0:
        total_cnt += sugar_kg//5
        break
    elif sugar_kg <= 0:
        total_cnt = -1
        break
    sugar_kg -= 3
    total_cnt +=1

print(total_cnt)

