package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.BillingKeyNotFoundError
import java.lang.Exception


/** 빌링키가 존재하지 않는 경우 */
public class BillingKeyNotFoundException internal constructor(
  cause: BillingKeyNotFoundError
) : PortOneException(cause.message), CreatePaymentScheduleException, DeleteBillingKeyException, GetBillingKeyInfoException, PayWithBillingKeyException, RevokePaymentSchedulesException {
}
