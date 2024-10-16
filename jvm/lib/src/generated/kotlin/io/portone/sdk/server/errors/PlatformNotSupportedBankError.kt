package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetPlatformAccountHolderError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 지원하지 않는 은행인 경우 */
@Serializable
@SerialName("PLATFORM_NOT_SUPPORTED_BANK")
@ConsistentCopyVisibility
public data class PlatformNotSupportedBankError internal constructor(
  override val message: String? = null,
): GetPlatformAccountHolderError
