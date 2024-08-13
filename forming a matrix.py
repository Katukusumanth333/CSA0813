matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in matrix:
    print(row)




matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]
result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
print("Result of adding two matrices:")
for row in result:
    print(row)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in matrix:
    print(row)


decimal_num = int(input("Enter a decimal number: "))
binary_num = bin(decimal_num).replace("0b", "")
octal_num = oct(decimal_num).replace("0o", "")
print("Binary Number =", binary_num)
print("Octal Number =", octal_num)
