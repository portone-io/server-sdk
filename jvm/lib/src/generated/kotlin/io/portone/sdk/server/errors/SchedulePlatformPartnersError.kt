package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface SchedulePlatformPartnersError {
  public sealed interface Recognized : SchedulePlatformPartnersError {
    public val message: String?
  }
  public data object Unrecognized : SchedulePlatformPartnersError
}
