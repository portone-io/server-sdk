package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.DraftB2bTaxInvoiceError
import io.portone.sdk.server.errors.RequestB2bTaxInvoiceReverseIssuanceError
import io.portone.sdk.server.errors.UpdateB2bTaxInvoiceDraftError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서에 공급자 문서 번호가 이미 사용 중인 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_SUPPLIER_DOCUMENT_KEY_ALREADY_USED")
@ConsistentCopyVisibility
public data class B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError internal constructor(
  override val message: String? = null,
): DraftB2bTaxInvoiceError,
  RequestB2bTaxInvoiceReverseIssuanceError,
  UpdateB2bTaxInvoiceDraftError
