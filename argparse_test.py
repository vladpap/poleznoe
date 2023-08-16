import argparse


def main():
	parser = argparse.ArgumentParser(
		description='Описание что делает программа')
	parser.add_argument('name', help='Ваше имя')
	parser.add_argument('-l', '--last_name', help='Ваша фамилия')
	parser.add_argument('-a', '--age', help='Возраст', type=int)
	parser.add_argument('-s', '--show_age', action='store_true',
                    help='True or False, show age')
	parser.parse_args()

	args = parser.parse_args()
	print(args.name, args.last_name, args.age if args.show_age else "")



if __name__ == "__main__":
	main()
