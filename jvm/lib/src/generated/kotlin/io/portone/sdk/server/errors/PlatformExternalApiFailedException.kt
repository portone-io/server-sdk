package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformExternalApiFailedError
import java.lang.Exception


/** 외부 api 오류 */
public class PlatformExternalApiFailedException internal constructor(
  cause: PlatformExternalApiFailedError
) : PortOneException(cause.message), GetPlatformAccountHolderException, GetPlatformCompanyStateException {
}
