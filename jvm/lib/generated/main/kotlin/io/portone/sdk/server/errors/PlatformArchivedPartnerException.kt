package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.PlatformArchivedPartnerError
import java.lang.Exception


/** 보관된 파트너를 업데이트하려고 하는 경우 */
public class PlatformArchivedPartnerException(
  cause: PlatformArchivedPartnerError
) : Exception(cause.message) {
}
