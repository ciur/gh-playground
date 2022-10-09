import os
from tempfile import NamedTemporaryFile

from banger import cmd as command


class Git:

    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run

    def add(self, file_list):
        for file_path in file_list:
            command.run(f"git add {file_path}", dry_run=self.dry_run)

    def push(self) -> command.Command:
        return command.run("git push", dry_run=self.dry_run)

    def commit(self, message: str, args: str = "") -> command.Command :
        f = NamedTemporaryFile("wb", delete=False)
        f.write(message.encode("utf-8"))
        f.close()
        c = command.run(f"git commit {args} -F {f.name}", dry_run=self.dry_run)
        os.unlink(f.name)
        return c
