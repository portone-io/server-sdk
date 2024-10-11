package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformPartnerNotFoundError
import java.lang.Exception


public class PlatformPartnerNotFoundException(
  cause: PlatformPartnerNotFoundError
) : Exception(cause.message) {
}
