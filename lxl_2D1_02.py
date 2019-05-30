# def is_leap(year):
#     if year % 4 == 0:
#         leap = True
#         if year % 100 == 0 and year % 400 != 0:
#             leap = False
#     return leap

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap(int(input("请输入年份："))))