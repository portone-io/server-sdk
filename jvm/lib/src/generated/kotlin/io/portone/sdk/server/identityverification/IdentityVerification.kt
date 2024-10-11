package io.portone.sdk.server.identityverification

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 본인인증 내역 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface IdentityVerification {
}
