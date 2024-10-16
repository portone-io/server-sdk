package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import io.portone.sdk.server.platform.transfer.PlatformPortOnePaymentCancelAmountType
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산 취소 요청 금액이 포트원 결제 취소 내역의 취소 금액을 초과한 경우 */
@Serializable
@SerialName("PLATFORM_SETTLEMENT_CANCEL_AMOUNT_EXCEEDED_PORT_ONE_CANCEL")
@ConsistentCopyVisibility
public data class PlatformSettlementCancelAmountExceededPortOneCancelError internal constructor(
  val registeredSettlementCancelAmount: Long,
  val requestSettlementCancelAmount: Long,
  val portOneCancelAmount: Long,
  val amountType: PlatformPortOnePaymentCancelAmountType,
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError
