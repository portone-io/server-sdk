package io.portone.sdk.server.errors

import io.portone.sdk.server.b2b.B2bExternalServiceError
import java.lang.Exception


/** 외부 서비스에서 에러가 발생한 경우 */
public class B2bExternalServiceException(
  cause: B2bExternalServiceError
) : Exception(cause.message) {
}
