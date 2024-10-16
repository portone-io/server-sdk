package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.IssueCashReceiptError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 현금영수증이 이미 발급된 경우 */
@Serializable
@SerialName("CASH_RECEIPT_ALREADY_ISSUED")
@ConsistentCopyVisibility
public data class CashReceiptAlreadyIssuedError internal constructor(
  override val message: String? = null,
): IssueCashReceiptError
