package io.portone.sdk.server.identityverification

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 요청된 본인인증 건이 존재하지 않는 경우 */
@Serializable
@SerialName("IDENTITY_VERIFICATION_NOT_FOUND")
public data class IdentityVerificationNotFoundError(
  override val message: String? = null,
): ConfirmIdentityVerificationError,
  ): GetIdentityVerificationError,
    ): ResendIdentityVerificationError,
      ): SendIdentityVerificationError,
