package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.partner.PlatformPartnerIdAlreadyExistsError
import java.lang.Exception


public class PlatformPartnerIdAlreadyExistsException(
  cause: PlatformPartnerIdAlreadyExistsError
) : Exception(cause.message) {
}
