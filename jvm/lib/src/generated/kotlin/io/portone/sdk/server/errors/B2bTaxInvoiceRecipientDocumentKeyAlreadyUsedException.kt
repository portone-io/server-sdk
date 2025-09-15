package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError
import java.lang.Exception


/** 세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우 */
public class B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedException internal constructor(
  cause: B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError
) : PortOneException(cause.message), DraftB2bTaxInvoiceException, IssueB2bTaxInvoiceImmediatelyException, RequestB2bTaxInvoiceReverseIssuanceException, UpdateB2bTaxInvoiceDraftException {
}
