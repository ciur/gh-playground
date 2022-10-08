import os
from packaging.version import Version


def increment_ver(version: str) -> Version:
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
    cur_ver = os.environ["CURRENT_VERSION"]
    version = increment_ver(cur_ver)

    print(version)


if __name__ == "__main__":
    main()
