package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCompanyNotFoundError
import java.lang.Exception


/** 사업자가 존재하지 않는 경우 */
public class B2bCompanyNotFoundException(
  cause: B2bCompanyNotFoundError
) : Exception(cause.message) {
}
