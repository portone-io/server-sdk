package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.PlatformPaymentMethod
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 가상계좌 */
@Serializable
@SerialName("VIRTUAL_ACCOUNT")
public data object PlatformPaymentMethodVirtualAccount: PlatformPaymentMethod