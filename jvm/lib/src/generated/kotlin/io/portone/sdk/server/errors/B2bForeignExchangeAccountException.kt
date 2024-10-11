package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bForeignExchangeAccountError
import java.lang.Exception


/** 계좌 정보 조회가 불가능한 외화 계좌인 경우 */
public class B2bForeignExchangeAccountException(
  cause: B2bForeignExchangeAccountError
) : Exception(cause.message) {
}
