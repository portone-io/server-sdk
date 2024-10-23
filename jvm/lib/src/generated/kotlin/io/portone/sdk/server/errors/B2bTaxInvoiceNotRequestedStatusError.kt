package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CancelB2bTaxInvoiceRequestError
import io.portone.sdk.server.errors.IssueB2bTaxInvoiceError
import io.portone.sdk.server.errors.RefuseB2bTaxInvoiceRequestError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서가 역발행 대기 상태가 아닌 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_NOT_REQUESTED_STATUS")
@ConsistentCopyVisibility
public data class B2bTaxInvoiceNotRequestedStatusError internal constructor(
  override val message: String? = null,
): CancelB2bTaxInvoiceRequestError,
  IssueB2bTaxInvoiceError,
  RefuseB2bTaxInvoiceRequestError
