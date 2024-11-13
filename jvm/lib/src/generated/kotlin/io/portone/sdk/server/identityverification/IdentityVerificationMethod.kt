package io.portone.sdk.server.identityverification

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 본인인증 방식 */
@Serializable
public sealed class IdentityVerificationMethod {
  @SerialName("SMS")
  public data object Sms : IdentityVerificationMethod()
  @SerialName("APP")
  public data object App : IdentityVerificationMethod()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : IdentityVerificationMethod()
}
