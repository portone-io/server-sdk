package io.portone.sdk.server.errors

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface GetPlatformAdditionalFeePolicyScheduleError {
  public data object Unrecognized : GetPlatformAdditionalFeePolicyScheduleError
}
