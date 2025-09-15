package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.BillingKeyAlreadyIssuedError
import java.lang.Exception


public class BillingKeyAlreadyIssuedException internal constructor(
  cause: BillingKeyAlreadyIssuedError
) : PortOneException(cause.message), ConfirmBillingKeyException, ConfirmBillingKeyIssueAndPayException {
}
