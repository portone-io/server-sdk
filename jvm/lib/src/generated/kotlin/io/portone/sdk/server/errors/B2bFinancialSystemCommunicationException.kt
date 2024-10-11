package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bFinancialSystemCommunicationError
import java.lang.Exception


/** 금융기관과의 통신에 실패한 경우 */
public class B2bFinancialSystemCommunicationException(
  cause: B2bFinancialSystemCommunicationError
) : Exception(cause.message) {
}
