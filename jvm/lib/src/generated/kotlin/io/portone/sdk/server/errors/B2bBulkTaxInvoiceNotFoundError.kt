package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 일괄 세금계산서가 존재하지 않은 경우 */
@Serializable
@SerialName("B2B_BULK_TAX_INVOICE_NOT_FOUND")
internal data class B2bBulkTaxInvoiceNotFoundError(
  override val message: String? = null,
) : DeleteB2bTaxInvoiceError.Recognized, GetB2bBulkTaxInvoiceError.Recognized


