package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ProfileSettingsNotFoundError
import java.lang.Exception


/** 프로필 설정이 존재하지 않는 경우 */
public class ProfileSettingsNotFoundException internal constructor(
  cause: ProfileSettingsNotFoundError
) : PortOneException(cause.message), EvaluateCheckoutProfileException {
}
