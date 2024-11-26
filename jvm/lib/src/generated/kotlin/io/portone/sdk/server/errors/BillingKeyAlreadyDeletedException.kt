package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.BillingKeyAlreadyDeletedError
import java.lang.Exception


/** 빌링키가 이미 삭제된 경우 */
public class BillingKeyAlreadyDeletedException internal constructor(
  cause: BillingKeyAlreadyDeletedError
) : PortOneException(cause.message), CreatePaymentScheduleException, DeleteBillingKeyException, PayWithBillingKeyException, RevokePaymentSchedulesException {
}
