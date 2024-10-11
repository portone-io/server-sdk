package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.PaymentMethodType
import io.portone.sdk.server.platform.transfer.PlatformTransferSummaryPayment
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("EXTERNAL")
public data class PlatformTransferSummaryExternalPayment(
  val id: String,
  val currency: Currency,
  val orderName: String? = null,
  val methodType: PaymentMethodType? = null,
): PlatformTransferSummaryPayment
