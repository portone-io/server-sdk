package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.InformationMismatchError
import java.lang.Exception


/** 정보가 일치하지 않는 경우 */
public class InformationMismatchException internal constructor(
  cause: InformationMismatchError
) : PortOneException(cause.message), ConfirmBillingKeyException, ConfirmBillingKeyIssueAndPayException, ConfirmPaymentException {
}
