#윤년
import sys
input = sys.stdin.readline
year = int(input())

year_yoon = 0
if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
    year_yoon =1

print(year_yoon)