# id package is 69157477

if __name__ == '__main__':
    k = int(input())
    keyboard = [[int(j) if j != '.' else None for j in input()] for _ in range(4)]

    dict_key = {}
    for row in keyboard:
        for key in row:
            if key and dict_key.get(key):
                dict_key[key] += 1
                continue
            dict_key[key] = 1

    result = 0
    for key in dict_key:
        if key and dict_key[key] <= k*2:
            result += 1
    
    print(result)
