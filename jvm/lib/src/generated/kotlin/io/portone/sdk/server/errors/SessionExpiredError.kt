package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 세션이 만료된 경우 */
@Serializable
@SerialName("SESSION_EXPIRED")
internal data class SessionExpiredError(
  override val message: String? = null,
) : GetPaymentSessionError.Recognized


