package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformNotSupportedBankError
import java.lang.Exception


/** 지원하지 않는 은행인 경우 */
public class PlatformNotSupportedBankException(
  cause: PlatformNotSupportedBankError
) : Exception(cause.message) {
}
