def najstarsi(inp: dict):
    return list(max(inp.items(), key=lambda x: x[1]))

def teraz(inp: dict):
    ret = []
    for pair in inp.items():
        if pair[1] >= 65:
            ret.append(pair[0])
    return ret

def on(inp: dict, n: int):
    ret = []
    for pair in inp.items():
        if pair[1] + n == 65:
            ret.append(pair[0])
    return ret

with open("ucitelia.txt", "r") as f:
    lines = f.readlines()
    ucitelia = {};
    for line in lines:
        a = line.split(" ")
        ucitelia[a[0]] = int(a[1])

    print(f"najstarsi {najstarsi(ucitelia)}")
    print(f"teraz {teraz(ucitelia)}")
    print(f"on {on(ucitelia, 20)}")

