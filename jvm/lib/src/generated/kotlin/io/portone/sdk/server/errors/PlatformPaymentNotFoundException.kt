package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformPaymentNotFoundError
import java.lang.Exception


public class PlatformPaymentNotFoundException(
  cause: PlatformPaymentNotFoundError
) : Exception(cause.message) {
}
