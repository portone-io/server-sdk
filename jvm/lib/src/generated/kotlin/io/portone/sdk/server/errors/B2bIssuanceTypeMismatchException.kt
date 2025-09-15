package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bIssuanceTypeMismatchError
import java.lang.Exception


/** 세금계산서 발행 유형이 올바르지 않은 경우 */
public class B2bIssuanceTypeMismatchException internal constructor(
  cause: B2bIssuanceTypeMismatchError
) : PortOneException(cause.message), DraftB2bTaxInvoiceException, IssueB2bTaxInvoiceImmediatelyException, RequestB2bTaxInvoiceReverseIssuanceException, UpdateB2bTaxInvoiceDraftException, requestB2bTaxInvoiceException {
}
