import os
from tempfile import NamedTemporaryFile

from banger import cmd as command


def add(file_list):
    for file_path in file_list:
        command.run(f"git add {file_path}")


def push() -> command.Command:
    return command.run("git push")


def commit(message: str, args: str = "") -> command.Command:
    f = NamedTemporaryFile("wb", delete=False)
    f.write(message.encode("utf-8"))

    f.close()
    c = command.run(f"git commit {args} -F {f.name}")
    os.unlink(f.name)
    return c
