package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.BillingKeyNotIssuedError
import java.lang.Exception


public class BillingKeyNotIssuedException internal constructor(
  cause: BillingKeyNotIssuedError
) : PortOneException(cause.message), DeleteBillingKeyException {
}
