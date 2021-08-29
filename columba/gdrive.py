#
# Copyright (C) 2021 Noverde Tecnologia e Pagamentos S/A
# Copyright (C) 2021 Everaldo Canuto <everaldo.canuto@gmail.com>
#
# Use of this source code is governed by an MIT-style license that can be
# found in the LICENSE file or at https://opensource.org/licenses/MIT.
#
import os
import warnings

warnings.simplefilter(action="ignore", category=UserWarning)

from google.colab import drive

BASE_PATH = "/content/drive"


def mount(remount=False):
    if remount or not os.path.isdir(BASE_PATH):
        drive.mount(BASE_PATH, force_remount=True)
