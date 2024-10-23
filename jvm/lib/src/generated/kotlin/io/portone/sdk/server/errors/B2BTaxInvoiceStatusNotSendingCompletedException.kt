package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2BTaxInvoiceStatusNotSendingCompletedError
import java.lang.Exception


/** 원본 세금계산서가 전송완료 상태가 아닌 경우 */
public class B2BTaxInvoiceStatusNotSendingCompletedException(
  cause: B2BTaxInvoiceStatusNotSendingCompletedError
) : Exception(cause.message) {
}
