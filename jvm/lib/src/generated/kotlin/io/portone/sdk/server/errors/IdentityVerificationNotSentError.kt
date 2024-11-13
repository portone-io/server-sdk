package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 본인인증 건이 API로 요청된 상태가 아닌 경우 */
@Serializable
@SerialName("IDENTITY_VERIFICATION_NOT_SENT")
@ConsistentCopyVisibility
public data class IdentityVerificationNotSentError internal constructor(
  val message: String? = null,
) : ConfirmIdentityVerificationError, ResendIdentityVerificationError
