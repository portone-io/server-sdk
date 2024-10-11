package io.portone.sdk.server.errors

import io.portone.sdk.server.cashreceipt.CashReceiptAlreadyIssuedError
import java.lang.Exception


/** 현금영수증이 이미 발급된 경우 */
public class CashReceiptAlreadyIssuedException(
  cause: CashReceiptAlreadyIssuedError
) : Exception(cause.message) {
}
