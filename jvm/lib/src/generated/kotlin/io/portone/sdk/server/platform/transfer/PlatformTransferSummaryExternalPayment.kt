package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.PaymentMethodType
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("EXTERNAL")
public data class PlatformTransferSummaryExternalPayment(
  override val id: String,
  override val orderName: String? = null,
  override val currency: Currency,
  override val methodType: PaymentMethodType? = null,
) : PlatformTransferSummaryPayment.Recognized


