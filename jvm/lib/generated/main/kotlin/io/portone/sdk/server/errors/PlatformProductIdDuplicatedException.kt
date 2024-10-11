package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformProductIdDuplicatedError
import java.lang.Exception
import kotlin.String


public class PlatformProductIdDuplicatedException(
  cause: PlatformProductIdDuplicatedError
) : Exception(cause.message) {
  public val id: String = cause.id,
}
