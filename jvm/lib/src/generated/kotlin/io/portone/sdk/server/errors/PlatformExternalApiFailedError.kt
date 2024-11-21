package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 외부 api 오류 */
@Serializable
@SerialName("PLATFORM_EXTERNAL_API_FAILED")
internal data class PlatformExternalApiFailedError(
  override val message: String? = null,
) : GetPlatformAccountHolderError.Recognized
