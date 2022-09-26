#!/bin/bash
#
# Copyright (C) 2016 The CyanogenMod Project
# Copyright (C) 2017-2020 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

function blob_fixup() {
    case "${1}" in
    odm/etc/init/wlchgmonitor.rc)
        sed -i '/disabled/d' "${2}"
        sed -i '/seclabel u:r:wlchgmonitor:s0/d' "${2}"
        ;;
    esac
}

# If we're being sourced by the common script that we called,
# stop right here. No need to go down the rabbit hole.
if [ "${BASH_SOURCE[0]}" != "${0}" ]; then
    return
fi

set -e

export DEVICE=instantnoodlep
export DEVICE_COMMON=sm8250-common
export VENDOR=oneplus

"./../../${VENDOR}/${DEVICE_COMMON}/extract-files.sh" "$@"
