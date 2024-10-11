package io.portone.sdk.server.errors

import io.portone.sdk.server.b2b.B2bTaxInvoiceAttachmentNotFoundError
import java.lang.Exception


/** 세금계산서의 첨부파일을 찾을 수 없는 경우 */
public class B2bTaxInvoiceAttachmentNotFoundException(
  cause: B2bTaxInvoiceAttachmentNotFoundError
) : Exception(cause.message) {
}
