package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CashReceiptAlreadyIssuedError
import java.lang.Exception


/** 현금영수증이 이미 발급된 경우 */
public class CashReceiptAlreadyIssuedException internal constructor(
  cause: CashReceiptAlreadyIssuedError
) : PortOneException(cause.message), IssueCashReceiptException {
}
