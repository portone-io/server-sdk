package io.portone.sdk.server.platform.account

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 외부 api 오류 */
@Serializable
@SerialName("PLATFORM_EXTERNAL_API_FAILED")
public data class PlatformExternalApiFailedError(
  override val message: String? = null,
): GetPlatformAccountHolderError,
