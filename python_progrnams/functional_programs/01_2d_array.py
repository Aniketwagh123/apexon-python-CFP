def get_2d_array_input(rows: int, columns: int):
    matrix = []
    
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(int(input()))
        matrix.append(row)
    return matrix

def print_2d_array(matrix):    
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end=" ")
        print()


if __name__ == "__main__":
    rows: int = int(input("Enter the number of rows: "))
    columns: int = int(input("Enter the number of columns: "))

    matrix = get_2d_array_input(rows=rows, columns=columns)
    print_2d_array(matrix)
