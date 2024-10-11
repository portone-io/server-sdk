package io.portone.sdk.server.identityverification

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 본인인증 건이 이미 인증 완료된 상태인 경우 */
@Serializable
@SerialName("IDENTITY_VERIFICATION_ALREADY_VERIFIED")
public data class IdentityVerificationAlreadyVerifiedError(
  override val message: String? = null,
): ConfirmIdentityVerificationError,
  ): ResendIdentityVerificationError,
    ): SendIdentityVerificationError,
