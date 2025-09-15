package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 공급자가 존재하지 않은 경우 */
@Serializable
@SerialName("B2B_SUPPLIER_NOT_FOUND")
internal data class B2bSupplierNotFoundError(
  override val message: String? = null,
) : DraftB2bTaxInvoiceError.Recognized, IssueB2bTaxInvoiceImmediatelyError.Recognized, RequestB2bTaxInvoiceReverseIssuanceError.Recognized, UpdateB2bTaxInvoiceDraftError.Recognized


