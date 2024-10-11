package io.portone.sdk.server.errors

import io.portone.sdk.server.identityverification.IdentityVerificationNotFoundError
import java.lang.Exception


/** 요청된 본인인증 건이 존재하지 않는 경우 */
public class IdentityVerificationNotFoundException(
  cause: IdentityVerificationNotFoundError
) : Exception(cause.message) {
}
