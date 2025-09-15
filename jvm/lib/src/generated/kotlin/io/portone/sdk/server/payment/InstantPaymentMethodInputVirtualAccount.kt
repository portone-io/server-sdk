package io.portone.sdk.server.payment

import io.portone.sdk.server.common.Bank
import io.portone.sdk.server.payment.InstantPaymentMethodInputVirtualAccountCashReceiptInfo
import io.portone.sdk.server.payment.InstantPaymentMethodInputVirtualAccountExpiry
import io.portone.sdk.server.payment.InstantPaymentMethodInputVirtualAccountOption
import kotlin.String
import kotlinx.serialization.Serializable

/** 가상계좌 수단 정보 입력 정보 */
@Serializable
public data class InstantPaymentMethodInputVirtualAccount(
  /** 은행 */
  val bank: Bank,
  /** 입금 만료 기한 */
  val expiry: InstantPaymentMethodInputVirtualAccountExpiry,
  /** 가상계좌 유형 */
  val option: InstantPaymentMethodInputVirtualAccountOption,
  /** 현금영수증 정보 */
  val cashReceipt: InstantPaymentMethodInputVirtualAccountCashReceiptInfo? = null,
  /** 예금주명 */
  val remitteeName: String? = null,
)


