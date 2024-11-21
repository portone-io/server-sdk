package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CashReceiptNotFoundError
import java.lang.Exception


/** 현금영수증이 존재하지 않는 경우 */
public class CashReceiptNotFoundException internal constructor(
  cause: CashReceiptNotFoundError
) : PortOneException(cause.message), CancelCashReceiptException, GetCashReceiptException {
}
