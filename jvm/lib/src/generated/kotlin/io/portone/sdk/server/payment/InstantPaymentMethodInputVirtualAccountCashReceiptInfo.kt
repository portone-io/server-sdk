package io.portone.sdk.server.payment

import io.portone.sdk.server.common.CashReceiptInputType
import kotlin.String
import kotlinx.serialization.Serializable

/** 가상계좌 결제 시 현금영수증 정보 */
@Serializable
public data class InstantPaymentMethodInputVirtualAccountCashReceiptInfo(
  /** 현금영수증 유형 */
  val type: CashReceiptInputType,
  /** 사용자 식별 번호 */
  val customerIdentityNumber: String,
)
