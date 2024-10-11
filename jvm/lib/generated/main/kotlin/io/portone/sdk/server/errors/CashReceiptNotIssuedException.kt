package io.portone.sdk.server.errors

import io.portone.sdk.server.cashreceipt.CashReceiptNotIssuedError
import java.lang.Exception


/** 현금영수증이 발급되지 않은 경우 */
public class CashReceiptNotIssuedException(
  cause: CashReceiptNotIssuedError
) : Exception(cause.message) {
}
