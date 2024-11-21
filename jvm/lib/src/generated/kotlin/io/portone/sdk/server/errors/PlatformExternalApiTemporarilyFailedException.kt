package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformExternalApiTemporarilyFailedError
import java.lang.Exception


/** 외부 api의 일시적인 오류 */
public class PlatformExternalApiTemporarilyFailedException internal constructor(
  cause: PlatformExternalApiTemporarilyFailedError
) : PortOneException(cause.message), GetPlatformAccountHolderException {
}
