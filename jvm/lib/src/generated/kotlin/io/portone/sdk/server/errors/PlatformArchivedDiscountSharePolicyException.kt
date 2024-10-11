package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformArchivedDiscountSharePolicyError
import java.lang.Exception


/** 보관된 할인 분담 정책을 업데이트하려고 하는 경우 */
public class PlatformArchivedDiscountSharePolicyException(
  cause: PlatformArchivedDiscountSharePolicyError
) : Exception(cause.message) {
}
