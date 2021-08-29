#
# Copyright (C) 2021 Noverde Tecnologia e Pagamentos S/A
# Copyright (C) 2021 Everaldo Canuto <everaldo.canuto@gmail.com>
#
# Use of this source code is governed by an MIT-style license that can be
# found in the LICENSE file or at https://opensource.org/licenses/MIT.
#
from getpass import getpass

from columba import gdrive
from columba import profiles


def configure(profile=None, access_key=None, secret_key=None, region="us-east-1"):
    gdrive.mount()

    if not profile:
        profile = input("Enter the AWS profile name: ")

    if not access_key:
        access_key = getpass("Enter the AWS access key: ")

    if not secret_key:
        secret_key = getpass("Enter the AWS secret key: ")

    profiles.save(
        profile,
        {
            "AWS_ACCESS_KEY_ID": access_key,
            "AWS_SECRET_ACCESS_KEY": secret_key,
            "AWS_DEFAULT_REGION": region,
        },
    )
