package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.PlatformPaymentMethod
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 계좌이체 */
@Serializable
@SerialName("TRANSFER")
public data object PlatformPaymentMethodTransfer: PlatformPaymentMethod