package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.AttachB2bTaxInvoiceFileError
import io.portone.sdk.server.errors.CancelB2bTaxInvoiceRequestError
import io.portone.sdk.server.errors.DeleteB2bTaxInvoiceAttachmentError
import io.portone.sdk.server.errors.DeleteB2bTaxInvoiceError
import io.portone.sdk.server.errors.GetB2bTaxInvoiceAttachmentsError
import io.portone.sdk.server.errors.GetB2bTaxInvoiceError
import io.portone.sdk.server.errors.GetB2bTaxInvoicePdfDownloadUrlError
import io.portone.sdk.server.errors.GetB2bTaxInvoicePopupUrlError
import io.portone.sdk.server.errors.GetB2bTaxInvoicePrintUrlError
import io.portone.sdk.server.errors.IssueB2bTaxInvoiceError
import io.portone.sdk.server.errors.RefuseB2bTaxInvoiceRequestError
import io.portone.sdk.server.errors.requestB2bTaxInvoiceError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서가 존재하지 않은 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_NOT_FOUND")
@ConsistentCopyVisibility
public data class B2bTaxInvoiceNotFoundError internal constructor(
  val message: String? = null,
): AttachB2bTaxInvoiceFileError,
  CancelB2bTaxInvoiceRequestError,
  DeleteB2bTaxInvoiceAttachmentError,
  DeleteB2bTaxInvoiceError,
  GetB2bTaxInvoiceAttachmentsError,
  GetB2bTaxInvoiceError,
  GetB2bTaxInvoicePdfDownloadUrlError,
  GetB2bTaxInvoicePopupUrlError,
  GetB2bTaxInvoicePrintUrlError,
  IssueB2bTaxInvoiceError,
  RefuseB2bTaxInvoiceRequestError,
  requestB2bTaxInvoiceError
