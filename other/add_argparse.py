import argparse

parser = argparse.ArgumentParser()
parser.add_argument('run_date')
args = parser.parse_args()

path = "root/{0}".format(args.run_date)
print("path =",path)