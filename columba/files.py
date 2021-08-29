#
# Copyright (C) 2021 Noverde Tecnologia e Pagamentos S/A
# Copyright (C) 2021 Everaldo Canuto <everaldo.canuto@gmail.com>
#
# Use of this source code is governed by an MIT-style license that can be
# found in the LICENSE file or at https://opensource.org/licenses/MIT.
#
from google.colab import files


def upload():
    result = files.upload()
    if result:
        return list(result.keys())[0]
