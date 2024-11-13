package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformTransferSummaryPayment {
  public data object Unrecognized : PlatformTransferSummaryPayment
}
