package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.PlatformArchivedAdditionalFeePolicyError
import java.lang.Exception


/** 보관된 추가 수수료 정책을 업데이트하려고 하는 경우 */
public class PlatformArchivedAdditionalFeePolicyException(
  cause: PlatformArchivedAdditionalFeePolicyError
) : Exception(cause.message) {
}
