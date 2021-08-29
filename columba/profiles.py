#
# Copyright (C) 2021 Noverde Tecnologia e Pagamentos S/A
# Copyright (C) 2021 Everaldo Canuto <everaldo.canuto@gmail.com>
#
# Use of this source code is governed by an MIT-style license that can be
# found in the LICENSE file or at https://opensource.org/licenses/MIT.
#
import os
import shlex

from getpass import getpass

from columba import gdrive


BASE_PATH = f"{gdrive.BASE_PATH}/My Drive/.profiles"


def load(profile: str = "default"):
    gdrive.mount()

    filename = f"{BASE_PATH}/{profile}"

    try:
        stream = open(filename, "r")
        buffer = stream.readlines()
        stream.close()
    except Exception:
        return

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


def aws_configure(profile=None, access_key=None, secret_key=None, region="us-east-1"):
    if not profile:
        profile = input("Enter the AWS profile name: ")

    if not access_key:
        access_key = getpass("Enter the AWS access key: ")

    if not secret_key:
        secret_key = getpass("Enter the AWS secret key: ")

    save(
        profile,
        {
            "AWS_ACCESS_KEY_ID": access_key,
            "AWS_SECRET_ACCESS_KEY": secret_key,
            "AWS_DEFAULT_REGION": region,
        },
    )
