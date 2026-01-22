package io.portone.sdk.server.reconciliation

import io.portone.sdk.server.reconciliation.SimplifiedPaymentMethodType
import kotlinx.serialization.Serializable

@Serializable
public data class PaymentReconciliationVatReportItem(
  /** 결제수단 */
  val paymentMethod: SimplifiedPaymentMethodType,
  /** 공급가액 */
  val supplyAmount: Long,
  /** 부가세 금액 */
  val vatAmount: Long,
  /** 면세 금액 */
  val taxFreeAmount: Long,
  /** 총 금액 */
  val totalAmount: Long,
)


