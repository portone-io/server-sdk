package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.PlatformDiscountSharePolicyNotFoundError
import java.lang.Exception


public class PlatformDiscountSharePolicyNotFoundException(
  cause: PlatformDiscountSharePolicyNotFoundError
) : Exception(cause.message) {
}