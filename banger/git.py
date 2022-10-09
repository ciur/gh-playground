import os
from tempfile import NamedTemporaryFile

from banger import cmd


def add(file_list):
    for file_path in file_list:
        cmd.run(f"git add {file_path}")


def push() -> cmd.Command:
    return cmd.run("git push")


def commit(message: str, args: str = "") -> cmd.Command:
    f = NamedTemporaryFile("wb", delete=False)
    f.write(message.encode("utf-8"))
    f.close()
    c = cmd.run(f"git commit {args} -F {f.name}")
    os.unlink(f.name)
    return c
