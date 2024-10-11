package io.portone.sdk.server.errors

import io.portone.sdk.server.identityverification.IdentityVerificationNotSentError
import java.lang.Exception


/** 본인인증 건이 API로 요청된 상태가 아닌 경우 */
public class IdentityVerificationNotSentException(
  cause: IdentityVerificationNotSentError
) : Exception(cause.message) {
}
