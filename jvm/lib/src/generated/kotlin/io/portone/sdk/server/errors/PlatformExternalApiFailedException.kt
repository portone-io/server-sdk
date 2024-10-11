package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformExternalApiFailedError
import java.lang.Exception


/** 외부 api 오류 */
public class PlatformExternalApiFailedException(
  cause: PlatformExternalApiFailedError
) : Exception(cause.message) {
}
