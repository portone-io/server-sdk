package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCannotArchiveScheduledAdditionalFeePolicyError
import java.lang.Exception


/** 예약된 업데이트가 있는 추가 수수료 정책을 보관하려고 하는 경우 */
public class PlatformCannotArchiveScheduledAdditionalFeePolicyException(
  cause: PlatformCannotArchiveScheduledAdditionalFeePolicyError
) : Exception(cause.message) {
}
