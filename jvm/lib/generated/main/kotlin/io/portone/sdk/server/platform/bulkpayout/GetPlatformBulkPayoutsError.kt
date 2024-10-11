package io.portone.sdk.server.platform.bulkpayout

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface GetPlatformBulkPayoutsError {
  val message: String?
}