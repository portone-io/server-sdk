package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bTaxInvoiceNonDeletableStatusError
import java.lang.Exception


/**
 * 세금계산서가 삭제 가능한 상태가 아닌 경우
 *
 * 삭제 가능한 상태는 `DRAFTED`, `ISSUE_REFUSED`, `REQUEST_CANCELLED_BY_RECIPIENT`, `ISSUE_CANCELLED_BY_SUPPLIER`, `SENDING_FAILED` 입니다.
 */
public class B2bTaxInvoiceNonDeletableStatusException internal constructor(
  cause: B2bTaxInvoiceNonDeletableStatusError
) : PortOneException(cause.message), DeleteB2bTaxInvoiceException {
}
