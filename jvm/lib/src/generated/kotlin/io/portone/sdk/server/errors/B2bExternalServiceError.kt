package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 외부 서비스에서 에러가 발생한 경우 */
@Serializable
@SerialName("B2B_EXTERNAL_SERVICE")
internal data class B2bExternalServiceError(
  override val message: String? = null,
) : GetB2bBusinessInfosError.Recognized


