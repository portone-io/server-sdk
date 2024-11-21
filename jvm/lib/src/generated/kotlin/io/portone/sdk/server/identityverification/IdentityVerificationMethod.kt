package io.portone.sdk.server.identityverification

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 본인인증 방식 */
@Serializable
public sealed interface IdentityVerificationMethod {
  public val value: String
  @SerialName("SMS")
  public data object Sms : IdentityVerificationMethod {
    override val value: String = "SMS"
  }
  @SerialName("APP")
  public data object App : IdentityVerificationMethod {
    override val value: String = "APP"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : IdentityVerificationMethod
}
