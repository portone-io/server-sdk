package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CancelCashReceiptError
import io.portone.sdk.server.errors.GetCashReceiptError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 현금영수증이 존재하지 않는 경우 */
@Serializable
@SerialName("CASH_RECEIPT_NOT_FOUND")
@ConsistentCopyVisibility
public data class CashReceiptNotFoundError internal constructor(
  override val message: String? = null,
): CancelCashReceiptError,
  GetCashReceiptError
