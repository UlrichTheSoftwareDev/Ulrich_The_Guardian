import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbosity", help="hey verbo", action="store_true")
args = parser.parse_args()
if args.verbosity:
	print("verbo one")



