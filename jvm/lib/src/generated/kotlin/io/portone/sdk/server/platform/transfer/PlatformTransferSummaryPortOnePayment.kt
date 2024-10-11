package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.PaymentMethodType
import io.portone.sdk.server.platform.transfer.PlatformTransferSummaryPayment
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PORT_ONE")
public data class PlatformTransferSummaryPortOnePayment(
  val id: String,
  val orderName: String,
  val currency: Currency,
  val methodType: PaymentMethodType? = null,
): PlatformTransferSummaryPayment
