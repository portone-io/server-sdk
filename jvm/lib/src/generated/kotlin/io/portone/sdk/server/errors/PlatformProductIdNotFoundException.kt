package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformProductIdNotFoundError
import java.lang.Exception
import kotlin.String


public class PlatformProductIdNotFoundException internal constructor(
  cause: PlatformProductIdNotFoundError
) : PortOneException(cause.message), CreatePlatformOrderCancelTransferException {
  public val id: String = cause.id
}
