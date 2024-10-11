package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PaymentNotFoundError
import java.lang.Exception


/** 결제 건이 존재하지 않는 경우 */
public class PaymentNotFoundException(
  cause: PaymentNotFoundError
) : Exception(cause.message) {
}
