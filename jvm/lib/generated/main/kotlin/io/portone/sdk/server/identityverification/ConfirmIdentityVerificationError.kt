package io.portone.sdk.server.identityverification

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface ConfirmIdentityVerificationError {
  val message: String?
}
