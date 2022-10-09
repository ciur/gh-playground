import os

from banger.utils import (
    search_ver,
    increment_ver,
    replace_ver
)

from banger import git


def get_file_content(file_path: str) -> str:

    with open(file_path, "r") as file:
        content = file.read()

    return content


def set_file_content(file_path: str, content: str) -> None:

    with open(file_path, "w") as file:
        file.write(content)


def main():
    files_list = os.environ["FILES_LIST"]

    old_version = ""
    new_version = ""

    for file_path in files_list.split(','):
        file_path = file_path.strip()
        content = get_file_content(file_path)
        old_version = search_ver(content)
        new_version = increment_ver(old_version)
        print(f"{old_version} -> {new_version}")

        new_content = replace_ver(content, str(new_version))
        set_file_content(file_path, new_content)

    git.add([file_path.strip() for file_path in files_list.split(',')])
    git.commit(f"Bump version {old_version} to {new_version}")


if __name__ == "__main__":
    main()
