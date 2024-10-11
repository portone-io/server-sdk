package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.BillingKeyNotIssuedError
import java.lang.Exception


public class BillingKeyNotIssuedException(
  cause: BillingKeyNotIssuedError
) : Exception(cause.message) {
}
