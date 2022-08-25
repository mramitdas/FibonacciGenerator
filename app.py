def fabonacci(n):
    if n <= 0:
        print("Enter Positive No")
    else:
        f = [0, 1]
        for i in range(2, n + 1):
            f.append(f[i - 1] + f[i - 2])
        return f


if __name__ == "__main__":
    print(fabonacci(int(input())))
