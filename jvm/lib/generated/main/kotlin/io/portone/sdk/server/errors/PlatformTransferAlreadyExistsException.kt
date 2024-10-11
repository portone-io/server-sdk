package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformTransferAlreadyExistsError
import java.lang.Exception
import kotlin.String


public class PlatformTransferAlreadyExistsException(
  cause: PlatformTransferAlreadyExistsError
) : Exception(cause.message) {
  public val transferId: String = cause.transferId,
  public val transferGraphqlId: String = cause.transferGraphqlId,
}
