package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetPlatformAccountHolderError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 외부 api의 일시적인 오류 */
@Serializable
@SerialName("PLATFORM_EXTERNAL_API_TEMPORARILY_FAILED")
public data class PlatformExternalApiTemporarilyFailedError(
  override val message: String? = null,
): GetPlatformAccountHolderError
