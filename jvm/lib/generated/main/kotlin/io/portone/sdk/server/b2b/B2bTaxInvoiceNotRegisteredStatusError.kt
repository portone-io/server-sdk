package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서가 임시저장 상태가 아닌 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_NOT_REGISTERED_STATUS")
public data class B2bTaxInvoiceNotRegisteredStatusError(
  override val message: String? = null,
): AttachB2bTaxInvoiceFileError,
  ): DeleteB2bTaxInvoiceAttachmentError,
    ): requestB2bTaxInvoiceError,
