def search_in_matrix(mat, x):
    return any(x in row for row in mat)


n, m = map(int, input("Enter number of rows and columns: ").split())
mat = [list(map(int, input(f"Enter row {i+1}: ").split())) for i in range(n)]


x = int(input("Enter the element to search: "))


print("true" if search_in_matrix(mat, x) else "false")
