package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bTaxInvoiceNotDraftedStatusError
import java.lang.Exception


/** 세금계산서가 임시저장 완료 상태가 아닌 경우 */
public class B2bTaxInvoiceNotDraftedStatusException internal constructor(
  cause: B2bTaxInvoiceNotDraftedStatusError
) : PortOneException(cause.message), AttachB2bTaxInvoiceFileException, DeleteB2bTaxInvoiceAttachmentException, IssueB2bTaxInvoiceException, UpdateB2bTaxInvoiceDraftException, requestB2bTaxInvoiceException {
}
