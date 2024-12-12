import sys

def createSquareMatrix(s):
    n = [[0 for _ in range(s)] for _ in range(s)]
    return n

def txtToList(file):
    m = []
    with open(file, 'r') as file:
        for l in file:
            nums = list(map(int, l.split()))
            m.append(nums)
    return m

def listToMatrix(list, matrix, option):
    # preenche a matriz para representar um grafo não-direcionado
    if option == "1":
        for i in list[1:]:
            temp = i
            matrix[temp[0]-1][temp[1]-1] = temp[2]
            matrix[temp[1]-1][temp[0]-1] = temp[2]
    #preenche a matriz para representar um grafo direcionado
    if option == "2":
        for i in list[1:]:
            temp = i
            matrix[temp[0]-1][temp[1]-1] = temp[2]

def main():
    if len(sys.argv) == 3 and (sys.argv[2] == "1" or sys.argv[2] == "2"):
        values = txtToList(sys.argv[1])
        size = values[0]
        size = size[0]
        matrix = createSquareMatrix(size)
        listToMatrix(values, matrix, sys.argv[2])
        
        for i in matrix:
            print(i)
    else:
        print("\ninsufficient or invalid arguments\n")
        print("correct example: algoritmo test.g 1\n")
        exit(0)
if __name__ == "__main__": 
    main()