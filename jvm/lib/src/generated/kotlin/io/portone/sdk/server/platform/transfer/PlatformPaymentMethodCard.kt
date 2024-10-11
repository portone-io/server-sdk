package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.PlatformPaymentMethod
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 카드 */
@Serializable
@SerialName("CARD")
public data object PlatformPaymentMethodCard: PlatformPaymentMethod
