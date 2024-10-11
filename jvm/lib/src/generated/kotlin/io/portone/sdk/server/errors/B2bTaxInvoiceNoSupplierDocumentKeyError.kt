package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.RefuseB2bTaxInvoiceRequestError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서에 공급자 문서 번호가 기입되지 않은 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_NO_SUPPLIER_DOCUMENT_KEY")
public data class B2bTaxInvoiceNoSupplierDocumentKeyError(
  val message: String? = null,
): RefuseB2bTaxInvoiceRequestError
