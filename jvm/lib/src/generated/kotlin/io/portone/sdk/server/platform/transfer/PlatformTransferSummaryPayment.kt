package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.PaymentMethodType
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformTransferSummaryPayment {
  public val id: String
  public val currency: Currency
  public val methodType: PaymentMethodType?
}
