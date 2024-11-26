package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.IdentityVerificationNotFoundError
import java.lang.Exception


/** 요청된 본인인증 건이 존재하지 않는 경우 */
public class IdentityVerificationNotFoundException internal constructor(
  cause: IdentityVerificationNotFoundError
) : PortOneException(cause.message), ConfirmIdentityVerificationException, GetIdentityVerificationException, ResendIdentityVerificationException, SendIdentityVerificationException {
}
