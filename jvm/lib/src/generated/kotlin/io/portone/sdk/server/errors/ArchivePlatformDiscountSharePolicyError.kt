package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface ArchivePlatformDiscountSharePolicyError {
  public sealed interface Recognized : ArchivePlatformDiscountSharePolicyError {
    public val message: String?
  }
  public data object Unrecognized : ArchivePlatformDiscountSharePolicyError
}
