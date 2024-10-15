#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'vendor/oneplus/sm8250-common',
]

blob_fixups: blob_fixups_user_type = {
    'odm/etc/init/wlchgmonitor.rc': blob_fixup()
        .regex_replace('\tdisabled\n', '')
        .regex_replace('\tseclabel u:r:wlchgmonitor:s0\n', ''),
}  # fmt: skip

module = ExtractUtilsModule(
    'instantnoodlep',
    'oneplus',
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8250-common', module.vendor
    )
    utils.run()
