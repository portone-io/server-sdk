package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CashReceiptNotIssuedError
import java.lang.Exception


/** 현금영수증이 발급되지 않은 경우 */
public class CashReceiptNotIssuedException internal constructor(
  cause: CashReceiptNotIssuedError
) : PortOneException(cause.message), CancelCashReceiptException {
}
