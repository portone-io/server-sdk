package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bTaxInvoiceNotDraftedStatusError
import java.lang.Exception


/** 세금계산서가 임시저장 상태가 아닌 경우 */
public class B2bTaxInvoiceNotDraftedStatusException(
  cause: B2bTaxInvoiceNotDraftedStatusError
) : Exception(cause.message) {
}
