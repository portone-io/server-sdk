package io.portone.sdk.server.errors

import io.portone.sdk.server.b2b.B2bFinancialSystemFailureError
import java.lang.Exception


/** 금융기관 장애 */
public class B2bFinancialSystemFailureException(
  cause: B2bFinancialSystemFailureError
) : Exception(cause.message) {
}
