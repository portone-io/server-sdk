package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 지원 되지 않는 통화를 선택한 경우 */
@Serializable
@SerialName("PLATFORM_CURRENCY_NOT_SUPPORTED")
internal data class PlatformCurrencyNotSupportedError(
  override val message: String? = null,
) : CreatePlatformOrderTransferError.Recognized, CreatePlatformPartnerError.Recognized, CreatePlatformPartnersError.Recognized
