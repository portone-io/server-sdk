package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** B2B 기능이 활성화되지 않은 경우 */
@Serializable
@SerialName("B2B_NOT_ENABLED")
internal data class B2bNotEnabledError(
  override val message: String? = null,
) : GetB2bBusinessInfosError.Recognized


