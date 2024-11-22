package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 모바일 */
@Serializable
@SerialName("MOBILE")
public data object PlatformPaymentMethodMobile : PlatformPaymentMethod.Recognized


