package io.portone.sdk.server.platform.accounttransfer

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface GetPlatformAccountTransfersError {
  val message: String?
}
