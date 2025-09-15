package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bTaxInvoiceNoRecipientDocumentKeyError
import java.lang.Exception


/** 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우 */
public class B2bTaxInvoiceNoRecipientDocumentKeyException internal constructor(
  cause: B2bTaxInvoiceNoRecipientDocumentKeyError
) : PortOneException(cause.message), CancelB2bTaxInvoiceRequestException, requestB2bTaxInvoiceException {
}
