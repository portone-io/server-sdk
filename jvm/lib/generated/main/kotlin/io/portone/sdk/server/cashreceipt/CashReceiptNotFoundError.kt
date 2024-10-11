package io.portone.sdk.server.cashreceipt

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 현금영수증이 존재하지 않는 경우 */
@Serializable
@SerialName("CASH_RECEIPT_NOT_FOUND")
public data class CashReceiptNotFoundError(
  override val message: String? = null,
): CancelCashReceiptError,
  ): GetCashReceiptError,