package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bTaxInvoiceAttachmentNotFoundError
import java.lang.Exception


/** 세금계산서의 첨부파일을 찾을 수 없는 경우 */
public class B2bTaxInvoiceAttachmentNotFoundException internal constructor(
  cause: B2bTaxInvoiceAttachmentNotFoundError
) : PortOneException(cause.message), DeleteB2bTaxInvoiceAttachmentException {
}
