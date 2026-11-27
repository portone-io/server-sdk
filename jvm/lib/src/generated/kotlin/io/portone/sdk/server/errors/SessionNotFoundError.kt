package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 세션이 존재하지 않는 경우 */
@Serializable
@SerialName("SESSION_NOT_FOUND")
internal data class SessionNotFoundError(
  override val message: String? = null,
) : ClosePaymentSessionError.Recognized, GetPaymentSessionError.Recognized


