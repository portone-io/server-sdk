package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.IdentityVerificationAlreadyVerifiedError
import java.lang.Exception


/** 본인인증 건이 이미 인증 완료된 상태인 경우 */
public class IdentityVerificationAlreadyVerifiedException(
  cause: IdentityVerificationAlreadyVerifiedError
) : Exception(cause.message) {
}
