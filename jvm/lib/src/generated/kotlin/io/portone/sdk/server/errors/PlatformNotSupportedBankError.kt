package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 지원하지 않는 은행인 경우 */
@Serializable
@SerialName("PLATFORM_NOT_SUPPORTED_BANK")
internal data class PlatformNotSupportedBankError(
  override val message: String? = null,
) : GetPlatformAccountHolderError.Recognized
