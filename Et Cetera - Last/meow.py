import argparse

parser = argparse.ArgumentParser(description="Meow from cat")
parser.add_argument("-n", default=1,
                    help="Help for meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("Meow!")