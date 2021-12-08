#
# Copyright (C) 2021 Noverde Tecnologia e Pagamentos S/A
# Copyright (C) 2021 Everaldo Canuto <everaldo.canuto@gmail.com>
#
# Use of this source code is governed by an MIT-style license that can be
# found in the LICENSE file or at https://opensource.org/licenses/MIT.
#
import os
import shlex

from columba import gdrive


BASE_PATH = f"{gdrive.BASE_PATH}/My Drive/.profiles"


class ProfileNotFound(Exception):
    pass


def load(profile: str = "default"):
    gdrive.mount()

    filename = f"{BASE_PATH}/{profile}"

    try:
        stream = open(filename, "r")
        buffer = stream.readlines()
        stream.close()
    except Exception:
        raise ProfileNotFound(
            f"Please check if profile '{profile}' "
            "exists or create a new profile with 'aws.configure()'."
        )

    for line in buffer:
        tokens = list(shlex.shlex(line, posix=True, punctuation_chars="="))
        if len(tokens) < 2:
            continue
        if tokens[0] == "export" and tokens[2] == "=":
            tokens.pop(0)

        os.environ[tokens[0]] = tokens[2] if len(tokens) > 2 else ""

    print(f"Profile loaded from '{filename}'")


def save(profile="default", vars={}):
    gdrive.mount()

    filename = f"{BASE_PATH}/{profile}"
    dirname = os.path.dirname(filename)

    os.makedirs(dirname, exist_ok=True)

    with open(filename, "w") as file:
        for key, value in vars.items():
            file.write(f'{key}="{value}"\n')

    print(f"Profile saved at '{filename}'")
