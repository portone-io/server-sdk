package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyNtsNotConnectedError
import java.lang.Exception
import kotlin.String


/** 국세청에 연동되어 있지 않은 경우 */
public class B2bCounterpartyNtsNotConnectedException internal constructor(
  cause: B2bCounterpartyNtsNotConnectedError
) : PortOneException(cause.message), DraftB2bTaxInvoiceException, GetB2bCounterpartyCertificateException, GetB2bCounterpartyCertificateRegistrationUrlException, IssueB2bTaxInvoiceImmediatelyException, RequestB2bTaxInvoiceReverseIssuanceException, UpdateB2bTaxInvoiceDraftException, ValidateB2bCounterpartyCertificateException {
  public val brn: String? = cause.brn
  public val counterpartyId: String? = cause.counterpartyId
}
