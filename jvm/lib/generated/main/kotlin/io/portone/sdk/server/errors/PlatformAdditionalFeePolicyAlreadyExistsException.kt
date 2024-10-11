package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.policy.PlatformAdditionalFeePolicyAlreadyExistsError
import java.lang.Exception


public class PlatformAdditionalFeePolicyAlreadyExistsException(
  cause: PlatformAdditionalFeePolicyAlreadyExistsError
) : Exception(cause.message) {
}
