import subprocess
from typing import NamedTuple


class Command(NamedTuple):
    out: str
    err: str
    stdout: bytes
    stderr: bytes
    return_code: int


def _try_decode(bytes_: bytes) -> str:
    return bytes_.decode("utf-8")


def run(cmd: str) -> Command:
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    return_code = process.returncode
    return Command(
        _try_decode(stdout),
        _try_decode(stderr),
        stdout,
        stderr,
        return_code,
    )
