import argparse
from ulrich_the_guardian.generate_password import generate

def get_parser(h):
	parser = argparse.ArgumentParser(add_help=h)
	subparser = parser.add_subparsers(dest='command')
	init_database = subparser.add_parser('init', help="Init the database.")
	generate_password = subparser.add_parser('generate', help='Generate a random password.')
	add_password = subparser.add_parser('add_password', help='Add a passowrd.')
	list_password = subparser.add_parser('list', help='List password.')
	show_password = subparser.add_parser('show', help='Show password.')
	remove_password = subparser.add_parser('remove', help='Remove password.')
	return parser

if (__name__=="__main__"):
	p = get_parser(h=True)
	args = p.parse_args()
	if args.command == 'init':
		print("INIT")
	elif args.command == 'generate':
		print("GENERATE")
		generate()
	elif args.command == 'add_password':
		print("ADD_PASSWORD")
	elif args.command == 'list':
		print("LIST")
	elif args.command == 'show':
		print("SHOW")
	elif args.command == 'remove':
		print("REMOVE")
