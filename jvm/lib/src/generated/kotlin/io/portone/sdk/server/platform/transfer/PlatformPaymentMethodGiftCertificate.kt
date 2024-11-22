package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 상품권 */
@Serializable
@SerialName("GIFT_CERTIFICATE")
public data object PlatformPaymentMethodGiftCertificate : PlatformPaymentMethod.Recognized


