/*
 * SPDX-FileCopyrightText: 2025 The LineageOS Project
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include "TouchscreenGesture.h"

namespace aidl::vendor::lineage::touch {

const int TouchscreenGesture::kSupportedGestures = makeBitField(
        kGestureUpVee, kGestureLeftVee, kGestureRightVee, kGestureCircle, kGestureDoubleSwipe,
        kGestureUpToDown, kGestureM, kGestureW, kGestureSingleTap, kGestureS);

}  // namespace aidl::vendor::lineage::touch
