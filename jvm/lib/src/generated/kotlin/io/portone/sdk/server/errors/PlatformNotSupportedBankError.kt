package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetPlatformAccountHolderError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 지원하지 않는 은행인 경우 */
@Serializable
@SerialName("PLATFORM_NOT_SUPPORTED_BANK")
public data class PlatformNotSupportedBankError(
  override val message: String? = null,
): GetPlatformAccountHolderError
