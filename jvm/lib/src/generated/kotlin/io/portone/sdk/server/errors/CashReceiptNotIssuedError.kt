package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 현금영수증이 발급되지 않은 경우 */
@Serializable
@SerialName("CASH_RECEIPT_NOT_ISSUED")
@ConsistentCopyVisibility
public data class CashReceiptNotIssuedError internal constructor(
  val message: String? = null,
) : CancelCashReceiptError
