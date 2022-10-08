import os
import re

from packaging.version import Version


def extract_version(file_path: str) -> str:

    found = None
    with open(file_path, "r") as file:
        content = file.read()
        found = re.search("version = [\"|\'](.+)[\"|\']\n", content).group(1)

    return found


def extract_version_package_json(file_path: str) -> str:
    pass



def increment_ver(version: str) -> Version:

    if not version:
        raise ValueError("Empty version")

    current = Version(version)

    if current.is_devrelease:
        number = current.dev
        number += 1
        new_ver = f"{current.base_version}.dev{number}"

        return Version(new_ver)


    if current.is_prerelease:
        letter, number = current.pre
        number += 1
        new_ver = f"{current.base_version}.{letter}{number}"

        return Version(new_ver)


    cur = current
    new_ver = f"{cur.major}.{cur.minor}.{cur.micro + 1}"


    return Version(new_ver)



def main():
    files_list = os.environ["FILES_LIST"]
    for file_path in files_list.split(','):
        file_path = file_path.strip()
        cur_ver = None

        if "pyproject.toml" in file_path:
            cur_ver = extract_version(file_path)
        elif "package.json" in file_path:
            cur_ver = extract_version_package_json(file_path)
        else:
            cur_ver = extract_version(file_path)

        version = increment_ver(cur_ver)

        print(version)


if __name__ == "__main__":
    main()
