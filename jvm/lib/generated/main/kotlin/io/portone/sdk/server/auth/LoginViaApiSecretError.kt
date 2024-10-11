package io.portone.sdk.server.auth

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface LoginViaApiSecretError {
  val message: String?
}
