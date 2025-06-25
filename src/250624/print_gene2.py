import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--num1", required=True)
parser.add_argument("--num2", default=2)

args = parser.parse_args()
print(int(args.num1) + int(args.num2))
