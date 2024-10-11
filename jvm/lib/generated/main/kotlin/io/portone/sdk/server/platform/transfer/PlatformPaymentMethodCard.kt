package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 카드 */
@Serializable
@SerialName("CARD")
public data class PlatformPaymentMethodCard(
): PlatformPaymentMethod,
