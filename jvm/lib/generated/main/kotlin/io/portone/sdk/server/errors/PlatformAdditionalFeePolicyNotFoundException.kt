package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.PlatformAdditionalFeePolicyNotFoundError
import java.lang.Exception


public class PlatformAdditionalFeePolicyNotFoundException(
  cause: PlatformAdditionalFeePolicyNotFoundError
) : Exception(cause.message) {
}
