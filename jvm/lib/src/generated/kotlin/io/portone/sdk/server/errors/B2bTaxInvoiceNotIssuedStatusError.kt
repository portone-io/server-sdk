package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CancelB2bTaxInvoiceIssuanceError
import io.portone.sdk.server.errors.SendToNtsB2bTaxInvoiceError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서가 발행된(ISSUED) 상태가 아닌 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_NOT_ISSUED_STATUS")
@ConsistentCopyVisibility
public data class B2bTaxInvoiceNotIssuedStatusError internal constructor(
  override val message: String? = null,
): CancelB2bTaxInvoiceIssuanceError,
  SendToNtsB2bTaxInvoiceError
