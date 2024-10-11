package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformDiscountSharePolicyAlreadyExistsError
import java.lang.Exception


public class PlatformDiscountSharePolicyAlreadyExistsException(
  cause: PlatformDiscountSharePolicyAlreadyExistsError
) : Exception(cause.message) {
}
