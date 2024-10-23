package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError
import java.lang.Exception


/** 세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우 */
public class B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedException(
  cause: B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError
) : Exception(cause.message) {
}
