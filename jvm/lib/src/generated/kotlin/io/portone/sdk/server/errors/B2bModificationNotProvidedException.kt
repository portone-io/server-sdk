package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bModificationNotProvidedError
import java.lang.Exception


/** 세금계산서 수정 입력 정보를 찾을 수 없는 경우 */
public class B2bModificationNotProvidedException internal constructor(
  cause: B2bModificationNotProvidedError
) : PortOneException(cause.message), DraftB2bTaxInvoiceException, IssueB2bTaxInvoiceImmediatelyException, RequestB2bTaxInvoiceReverseIssuanceException, UpdateB2bTaxInvoiceDraftException, requestB2bTaxInvoiceException {
}
