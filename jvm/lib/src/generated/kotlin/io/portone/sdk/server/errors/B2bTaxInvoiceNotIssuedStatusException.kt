package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bTaxInvoiceNotIssuedStatusError
import java.lang.Exception


/** 세금계산서가 발행된(ISSUED) 상태가 아닌 경우 */
public class B2bTaxInvoiceNotIssuedStatusException internal constructor(
  cause: B2bTaxInvoiceNotIssuedStatusError
) : PortOneException(cause.message), CancelB2bTaxInvoiceIssuanceException, SendToNtsB2bTaxInvoiceException {
}
