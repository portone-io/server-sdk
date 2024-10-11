package io.portone.sdk.server.errors

import io.portone.sdk.server.b2b.B2bMemberCompanyNotFoundError
import java.lang.Exception


/** 연동 사업자가 존재하지 않는 경우 */
public class B2bMemberCompanyNotFoundException(
  cause: B2bMemberCompanyNotFoundError
) : Exception(cause.message) {
}
