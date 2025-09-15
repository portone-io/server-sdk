package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError
import java.lang.Exception


/** 세금계산서에 공급자 문서 번호가 이미 사용 중인 경우 */
public class B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedException internal constructor(
  cause: B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError
) : PortOneException(cause.message), DraftB2bTaxInvoiceException, IssueB2bTaxInvoiceImmediatelyException, RequestB2bTaxInvoiceReverseIssuanceException, UpdateB2bTaxInvoiceDraftException {
}
