package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bOriginalTaxInvoiceNotFoundError
import java.lang.Exception


/** 원본 세금계산서가 존재하지 않은 경우 */
public class B2bOriginalTaxInvoiceNotFoundException internal constructor(
  cause: B2bOriginalTaxInvoiceNotFoundError
) : PortOneException(cause.message), DraftB2bTaxInvoiceException, IssueB2bTaxInvoiceImmediatelyException, RequestB2bTaxInvoiceReverseIssuanceException, UpdateB2bTaxInvoiceDraftException, requestB2bTaxInvoiceException {
}
