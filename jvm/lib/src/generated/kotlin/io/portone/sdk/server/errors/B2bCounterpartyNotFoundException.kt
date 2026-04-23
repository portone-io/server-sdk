package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyNotFoundError
import java.lang.Exception
import kotlin.String


/** 거래처가 존재하지 않는 경우 */
public class B2bCounterpartyNotFoundException internal constructor(
  cause: B2bCounterpartyNotFoundError
) : PortOneException(cause.message), DeleteB2bCounterpartyException, DraftB2bTaxInvoiceException, GetB2bCounterpartyCertificateException, GetB2bCounterpartyCertificateRegistrationUrlException, GetB2bCounterpartyException, IssueB2bTaxInvoiceImmediatelyException, RequestB2bTaxInvoiceReverseIssuanceException, UpdateB2bCounterpartyException, UpdateB2bTaxInvoiceDraftException, ValidateB2bCounterpartyCertificateException {
  public val counterpartyId: String? = cause.counterpartyId
}
