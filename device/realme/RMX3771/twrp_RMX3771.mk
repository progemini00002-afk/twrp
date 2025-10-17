#
# Copyright (C) 2024 The Android Open Source Project
# Copyright (C) 2024 TeamWin Recovery Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/base.mk)

# Inherit from RMX3771 device
$(call inherit-product, device/realme/RMX3771/device.mk)

# Inherit some common TWRP stuff.
$(call inherit-product, vendor/twrp/config/common.mk)

# Device identifier. This must come after all inclusions
PRODUCT_DEVICE := RMX3771
PRODUCT_NAME := twrp_RMX3771
PRODUCT_BRAND := realme
PRODUCT_MODEL := Realme 11 Pro 5G
PRODUCT_MANUFACTURER := realme

PRODUCT_GMS_CLIENTID_BASE := android-realme

PRODUCT_BUILD_PROP_OVERRIDES += \
    PRIVATE_BUILD_DESC="sys_mssi_64_cn_armv82-user 13 TP1A.220905.001 1691055955526 release-keys" \
    TARGET_DEVICE=RMX3771 \
    PRODUCT_NAME=RMX3771

BUILD_FINGERPRINT := realme/RMX3771/RMX3771:13/TP1A.220905.001/R.16f3a93-38c0-38c2:user/release-keys
