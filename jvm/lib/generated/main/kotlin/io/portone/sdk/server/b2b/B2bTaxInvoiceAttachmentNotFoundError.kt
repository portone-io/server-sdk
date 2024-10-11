package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서의 첨부파일을 찾을 수 없는 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_ATTACHMENT_NOT_FOUND")
public data class B2bTaxInvoiceAttachmentNotFoundError(
  override val message: String? = null,
): DeleteB2bTaxInvoiceAttachmentError,
