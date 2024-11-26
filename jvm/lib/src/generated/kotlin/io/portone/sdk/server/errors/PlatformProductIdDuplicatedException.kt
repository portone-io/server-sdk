package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformProductIdDuplicatedError
import java.lang.Exception
import kotlin.String


public class PlatformProductIdDuplicatedException internal constructor(
  cause: PlatformProductIdDuplicatedError
) : PortOneException(cause.message), CreatePlatformOrderCancelTransferException, CreatePlatformOrderTransferException {
  public val id: String = cause.id
}
