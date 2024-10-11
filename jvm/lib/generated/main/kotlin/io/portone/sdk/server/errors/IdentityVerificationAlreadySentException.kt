package io.portone.sdk.server.errors

import io.portone.sdk.server.identityverification.IdentityVerificationAlreadySentError
import java.lang.Exception


/** 본인인증 건이 이미 API로 요청된 상태인 경우 */
public class IdentityVerificationAlreadySentException(
  cause: IdentityVerificationAlreadySentError
) : Exception(cause.message) {
}
