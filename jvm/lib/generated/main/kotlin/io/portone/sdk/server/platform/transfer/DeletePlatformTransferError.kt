package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface DeletePlatformTransferError {
  val message: String?
}
