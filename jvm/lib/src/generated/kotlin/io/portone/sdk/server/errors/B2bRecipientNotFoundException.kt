package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bRecipientNotFoundError
import java.lang.Exception


/** 공급받는자가 존재하지 않은 경우 */
public class B2bRecipientNotFoundException internal constructor(
  cause: B2bRecipientNotFoundError
) : PortOneException(cause.message), DraftB2bTaxInvoiceException, IssueB2bTaxInvoiceImmediatelyException, RequestB2bTaxInvoiceReverseIssuanceException, UpdateB2bTaxInvoiceDraftException {
}
