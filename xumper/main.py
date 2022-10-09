import os

from xumper.utils import search_ver, increment_ver


def extract_version(file_path: str) -> str:

    with open(file_path, "r") as file:
        content = file.read()
        found = search_ver(content)

    return found


def main():
    files_list = os.environ["FILES_LIST"]

    for file_path in files_list.split(','):
        file_path = file_path.strip()
        old_version = extract_version(file_path)
        new_version = increment_ver(old_version)

        print(f"{old_version} -> {new_version}")


if __name__ == "__main__":
    main()
