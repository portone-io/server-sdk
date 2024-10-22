package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.AttachB2bTaxInvoiceFileError
import io.portone.sdk.server.errors.DeleteB2bTaxInvoiceAttachmentError
import io.portone.sdk.server.errors.UpdateB2bTaxInvoiceDraftError
import io.portone.sdk.server.errors.requestB2bTaxInvoiceError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서가 임시저장 상태가 아닌 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_NOT_DRAFTED_STATUS")
@ConsistentCopyVisibility
public data class B2bTaxInvoiceNotDraftedStatusError internal constructor(
  override val message: String? = null,
): AttachB2bTaxInvoiceFileError,
  DeleteB2bTaxInvoiceAttachmentError,
  UpdateB2bTaxInvoiceDraftError,
  requestB2bTaxInvoiceError
