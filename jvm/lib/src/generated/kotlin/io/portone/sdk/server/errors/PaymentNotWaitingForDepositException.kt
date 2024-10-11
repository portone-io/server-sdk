package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PaymentNotWaitingForDepositError
import java.lang.Exception


/** 결제 건이 입금 대기 상태가 아닌 경우 */
public class PaymentNotWaitingForDepositException(
  cause: PaymentNotWaitingForDepositError
) : Exception(cause.message) {
}
