package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bExternalServiceError
import java.lang.Exception


/** 외부 서비스에서 에러가 발생한 경우 */
public class B2bExternalServiceException internal constructor(
  cause: B2bExternalServiceError
) : PortOneException(cause.message), GetB2bBusinessInfosException {
}
