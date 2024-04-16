import sys

from colorama import Fore
from pathlib import Path


def print_dir(dir_path: Path, level: int):
    print(f'{Fore.YELLOW}{'\t' * level}{dir_path.name}')

    for item in dir_path.iterdir():
        if item.is_dir():
            print_dir(item, level + 1)
        else:
            print(f'{Fore.GREEN}{'\t' * (level + 1)}{item.name}')


def print_list_directories(path):
    dir_path = Path(path)

    if not dir_path.exists():
        print('This path is not exist!')
        return

    if not dir_path.is_dir():
        print('This path is nor directory!')

    print_dir(dir_path, 0)


def main():
    if len(sys.argv) < 2:
        print('The path to the directory is not specified')

    print_list_directories(sys.argv[1])


if __name__ == "__main__":
    main()
