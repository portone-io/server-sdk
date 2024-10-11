package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bTaxInvoiceNotRegisteredStatusError
import java.lang.Exception


/** 세금계산서가 임시저장 상태가 아닌 경우 */
public class B2bTaxInvoiceNotRegisteredStatusException(
  cause: B2bTaxInvoiceNotRegisteredStatusError
) : Exception(cause.message) {
}
