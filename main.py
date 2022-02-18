import argparse

def get_parser(h):
	parser = argparse.ArgumentParser(add_help=h)
#	group = parser.add_mutually_exclusive_group()
#	group.add_argument("-v", "--verbose", action="store_true")
#	group.add_argument("-q", "--quiet", action="store_true")
	parser.add_argument("x", help="the base")
	parser.add_argument("y", help="the exponent")
#	parser.add_argument("-v", help="the exponent")
	return parser

if (__name__=="__main__"):
	p = get_parser(h=True)
	args = p.parse_args()
