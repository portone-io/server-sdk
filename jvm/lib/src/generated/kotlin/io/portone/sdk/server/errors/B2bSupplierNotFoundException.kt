package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bSupplierNotFoundError
import java.lang.Exception
import kotlin.String


/** 공급자가 존재하지 않은 경우 */
public class B2bSupplierNotFoundException internal constructor(
  cause: B2bSupplierNotFoundError
) : PortOneException(cause.message), DraftB2bTaxInvoiceException, IssueB2bTaxInvoiceImmediatelyException, RequestB2bTaxInvoiceReverseIssuanceException, UpdateB2bTaxInvoiceDraftException {
  public val brn: String? = cause.brn
  public val counterpartyId: String? = cause.counterpartyId
}
