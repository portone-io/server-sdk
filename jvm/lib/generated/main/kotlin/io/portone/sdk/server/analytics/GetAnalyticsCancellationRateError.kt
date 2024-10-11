package io.portone.sdk.server.analytics

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface GetAnalyticsCancellationRateError {
  val message: String?
}