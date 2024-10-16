package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ConfirmIdentityVerificationError
import io.portone.sdk.server.errors.ResendIdentityVerificationError
import io.portone.sdk.server.errors.SendIdentityVerificationError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 본인인증 건이 이미 인증 완료된 상태인 경우 */
@Serializable
@SerialName("IDENTITY_VERIFICATION_ALREADY_VERIFIED")
@ConsistentCopyVisibility
public data class IdentityVerificationAlreadyVerifiedError internal constructor(
  override val message: String? = null,
): ConfirmIdentityVerificationError,
  ResendIdentityVerificationError,
  SendIdentityVerificationError
