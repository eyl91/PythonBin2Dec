import argparse
import re


def chooseConversionType(args):
    num = args.number

    if re.search(r"[a-zA-Z$&+,:;=?@#|\'<>\-^*()%!]", num):
        print("Your number needs to be decimal or binary.")
    else:
        charNum = set(num)

        if args.output_type.lower() == "decimal" and (
            charNum == {"1", "0"} or charNum == {"0"} or charNum == {"1"}
        ):
            print("Converting from binary to decimal.", convertBinToDec(num), sep="\n")

        else:
            print("Converting from decimal to binary.", convertDecToBin(num), sep="\n")


def convertDecToBin(num):
    binary = int(float(num))
    return bin(binary).replace("0b", "")


def convertBinToDec(num):
    return int(num, 2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "output_type", help="Binary or Decimal", type=str, choices=["binary", "decimal"]
    )
    parser.add_argument("number", help="Decimal Number", type=str)
    args = parser.parse_args()

    chooseConversionType(args)


if __name__ == "__main__":
    main()

