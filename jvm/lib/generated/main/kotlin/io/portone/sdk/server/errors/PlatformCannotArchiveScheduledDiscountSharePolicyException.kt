package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.policy.PlatformCannotArchiveScheduledDiscountSharePolicyError
import java.lang.Exception


/** 예약된 업데이트가 있는 할인 분담 정책을 보관하려고 하는 경우 */
public class PlatformCannotArchiveScheduledDiscountSharePolicyException(
  cause: PlatformCannotArchiveScheduledDiscountSharePolicyError
) : Exception(cause.message) {
}
