package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산 요청 공급대가가 포트원 결제 내역의 공급대가를 초과한 경우 */
@Serializable
@SerialName("PLATFORM_SETTLEMENT_SUPPLY_WITH_VAT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT")
@ConsistentCopyVisibility
public data class PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError internal constructor(
  val registeredSettlementSupplyWithVatAmount: Long,
  val requestSettlementSupplyWithVatAmount: Long,
  val portOneSupplyWithVatAmount: Long,
  val message: String? = null,
) : CreatePlatformOrderTransferError
