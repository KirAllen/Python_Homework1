# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
quater = int(input())
if quater == 1:
    print("X > 0 and y > 0")
elif quater == 2:
    print("X < 0 and y > 0")
elif quater == 3:
    print("x < 0 and y < 0")
elif quater == 4:
    print("x > 0 and y < 0")
else:
    print("ERROR")