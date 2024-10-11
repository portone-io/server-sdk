package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bTaxInvoiceNoSupplierDocumentKeyError
import java.lang.Exception


/** 세금계산서에 공급자 문서 번호가 기입되지 않은 경우 */
public class B2bTaxInvoiceNoSupplierDocumentKeyException(
  cause: B2bTaxInvoiceNoSupplierDocumentKeyError
) : Exception(cause.message) {
}
