package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderTransferError
import io.portone.sdk.server.errors.CreatePlatformPartnerError
import io.portone.sdk.server.errors.CreatePlatformPartnersError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 지원 되지 않는 통화를 선택한 경우 */
@Serializable
@SerialName("PLATFORM_CURRENCY_NOT_SUPPORTED")
public data class PlatformCurrencyNotSupportedError(
  val message: String? = null,
): CreatePlatformOrderTransferError,
  CreatePlatformPartnerError,
  CreatePlatformPartnersError
