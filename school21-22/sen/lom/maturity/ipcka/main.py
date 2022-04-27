def check(line: str) -> bool:
    split = line.split(".")
    if len(split) != 4:
        return False
    mask = []
    for c in split:
        if c.isnumeric():
            if 0 <= int(c) <= 255:
                mask.append(True)
                continue
        mask.append(False)

    return all(mask)

def main() -> None:
    with open("ips.txt", "r") as fp:
        good = []
        for line in fp.readlines():
            if check(line.strip()):
                good.append(line)
        fp.close()
        with open("out", "w+") as fp:
            fp.writelines(good)

if __name__ == "__main__":
    main()
