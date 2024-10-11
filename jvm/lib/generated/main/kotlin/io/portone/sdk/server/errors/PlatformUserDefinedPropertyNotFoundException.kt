package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.PlatformUserDefinedPropertyNotFoundError
import java.lang.Exception


/** 사용자 정의 속성이 존재 하지 않는 경우 */
public class PlatformUserDefinedPropertyNotFoundException(
  cause: PlatformUserDefinedPropertyNotFoundError
) : Exception(cause.message) {
}
