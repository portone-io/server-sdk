package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bTaxInvoiceNotRequestedStatusError
import java.lang.Exception


/** 세금계산서가 역발행 대기 상태가 아닌 경우 */
public class B2bTaxInvoiceNotRequestedStatusException internal constructor(
  cause: B2bTaxInvoiceNotRequestedStatusError
) : PortOneException(cause.message), CancelB2bTaxInvoiceRequestException, IssueB2bTaxInvoiceException, RefuseB2bTaxInvoiceRequestException {
}
