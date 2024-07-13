#!/usr/bin/python
def main():
    # user input, if else
    if input("Choose data type, (grouped/ungrouped) (default = ungrouped) : ") == "ungrouped":
        while True:
            x = input("x = ")
            # xvalue = [integer for number.sequence in x, ignore ","]
            xvalue = [int(num) for num in x.split(",")]

            n = len(xvalue)
            sumx = sum(xvalue)

            b = print(f"n = {n}")
            a = print(f"Σx = {sumx}")
            xmean = float(sumx) / n
            print(f"mean = {xmean}")
            

    else:
        print("ungrouped data")

if __name__ == "__main__":
    main()
