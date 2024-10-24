package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformAdditionalFeePolicyAlreadyExistsError
import java.lang.Exception


public class PlatformAdditionalFeePolicyAlreadyExistsException(
  cause: PlatformAdditionalFeePolicyAlreadyExistsError
) : Exception(cause.message) {
}