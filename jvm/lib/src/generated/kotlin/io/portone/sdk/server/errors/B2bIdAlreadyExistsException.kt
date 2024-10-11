package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bIdAlreadyExistsError
import java.lang.Exception


/** ID가 이미 사용중인 경우 */
public class B2bIdAlreadyExistsException(
  cause: B2bIdAlreadyExistsError
) : Exception(cause.message) {
}
