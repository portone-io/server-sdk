package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCompanyNotFoundError
import java.lang.Exception


/** 사업자 정보를 찾을 수 없는 경우 */
public class PlatformCompanyNotFoundException internal constructor(
  cause: PlatformCompanyNotFoundError
) : PortOneException(cause.message), GetPlatformCompanyStateException {
}
