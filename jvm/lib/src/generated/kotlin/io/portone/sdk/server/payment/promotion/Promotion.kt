package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 프로모션 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface Promotion {
  public data object Unrecognized : Promotion
}
