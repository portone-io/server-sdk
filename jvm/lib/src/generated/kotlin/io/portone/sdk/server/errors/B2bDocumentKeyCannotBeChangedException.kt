package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bDocumentKeyCannotBeChangedError
import java.lang.Exception


/** 문서번호 수정이 요청된 경우 */
public class B2bDocumentKeyCannotBeChangedException internal constructor(
  cause: B2bDocumentKeyCannotBeChangedError
) : PortOneException(cause.message), UpdateB2bTaxInvoiceDraftException {
}
