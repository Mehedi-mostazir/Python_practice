row1 = [1,1,1]
row2 = [1,1,1]
row3 = [1,1,1]

list = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Enter the position where you want to hide your money: ")

row = (int(position[0])-1)
coloum = (int(position[1])-1)

list[row][coloum] = "x"

print(f"{row1}\n{row2}\n{row3}")