package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.policy.PlatformCannotArchiveScheduledContractError
import java.lang.Exception


/** 예약된 업데이트가 있는 계약을 보관하려고 하는 경우 */
public class PlatformCannotArchiveScheduledContractException(
  cause: PlatformCannotArchiveScheduledContractError
) : Exception(cause.message) {
}
