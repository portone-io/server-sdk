package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 외부 api의 일시적인 오류 */
@Serializable
@SerialName("PLATFORM_EXTERNAL_API_TEMPORARILY_FAILED")
@ConsistentCopyVisibility
public data class PlatformExternalApiTemporarilyFailedError internal constructor(
  val message: String? = null,
) : GetPlatformAccountHolderError
