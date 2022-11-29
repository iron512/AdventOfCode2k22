def main():
    rows = open("input.txt").read().split("\n")
    # rows = open("input_easy.txt").read().split("\n")
    triangle = []

    for row in rows:
        triangle.append([int(el) for el in row.split(" ")])

    # starting point is the second to last row, not the last one
    start_point = len(triangle)-2
    while start_point >= 0:
        for i in range(len(triangle[start_point])):
            triangle[start_point][i] += max(triangle[start_point+1][i], triangle[start_point+1][i+1])
        start_point -= 1

    print("Result is:", triangle[0][0])


if __name__ == '__main__':
    main()
