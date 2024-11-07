package io.portone.sdk.server.identityverification

import kotlinx.serialization.Serializable

/** 본인인증 방식 */
@Serializable
public enum class IdentityVerificationMethod {
  Sms,
  App,
}
