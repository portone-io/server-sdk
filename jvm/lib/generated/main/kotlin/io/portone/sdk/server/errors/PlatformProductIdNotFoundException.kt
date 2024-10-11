package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformProductIdNotFoundError
import java.lang.Exception
import kotlin.String


public class PlatformProductIdNotFoundException(
  cause: PlatformProductIdNotFoundError
) : Exception(cause.message) {
  public val id: String = cause.id,
}
