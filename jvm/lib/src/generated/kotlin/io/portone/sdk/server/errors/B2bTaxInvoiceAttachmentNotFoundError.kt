package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.DeleteB2bTaxInvoiceAttachmentError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서의 첨부파일을 찾을 수 없는 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_ATTACHMENT_NOT_FOUND")
@ConsistentCopyVisibility
public data class B2bTaxInvoiceAttachmentNotFoundError internal constructor(
  override val message: String? = null,
): DeleteB2bTaxInvoiceAttachmentError
