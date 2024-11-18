package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산 요청 면세 금액이 포트원 결제 내역의 면세 금액을 초과한 경우 */
@Serializable
@SerialName("PLATFORM_SETTLEMENT_TAX_FREE_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT")
@ConsistentCopyVisibility
public data class PlatformSettlementTaxFreeAmountExceededPortOnePaymentError internal constructor(
  val registeredSettlementTaxFreeAmount: Long,
  val requestSettlementTaxFreeAmount: Long,
  val portOneTaxFreeAmount: Long,
  val message: String? = null,
) : CreatePlatformOrderTransferError
