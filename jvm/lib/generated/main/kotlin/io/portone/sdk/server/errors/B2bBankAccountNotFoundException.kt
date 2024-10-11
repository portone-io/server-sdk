package io.portone.sdk.server.errors

import io.portone.sdk.server.b2b.B2bBankAccountNotFoundError
import java.lang.Exception


/** 계좌가 존재하지 않는 경우 */
public class B2bBankAccountNotFoundException(
  cause: B2bBankAccountNotFoundError
) : Exception(cause.message) {
}
