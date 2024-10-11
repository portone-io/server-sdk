package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCannotSpecifyTransferError
import java.lang.Exception


/** 정산 건 식별에 실패한 경우 */
public class PlatformCannotSpecifyTransferException(
  cause: PlatformCannotSpecifyTransferError
) : Exception(cause.message) {
}
