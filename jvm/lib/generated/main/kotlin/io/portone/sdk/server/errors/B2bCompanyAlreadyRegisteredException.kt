package io.portone.sdk.server.errors

import io.portone.sdk.server.b2b.B2bCompanyAlreadyRegisteredError
import java.lang.Exception


/** 사업자가 이미 연동되어 있는 경우 */
public class B2bCompanyAlreadyRegisteredException(
  cause: B2bCompanyAlreadyRegisteredError
) : Exception(cause.message) {
}
