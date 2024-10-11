package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderTransferError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산 요청 결제 금액이 포트원 결제 내역의 결제 금액을 초과한 경우 */
@Serializable
@SerialName("PLATFORM_SETTLEMENT_PAYMENT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT")
public data class PlatformSettlementPaymentAmountExceededPortOnePaymentError(
  val registeredSettlementPaymentAmount: Long,
  val requestSettlementPaymentAmount: Long,
  val portOnePaymentAmount: Long,
  val message: String? = null,
): CreatePlatformOrderTransferError
