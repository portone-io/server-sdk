package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformTransferAlreadyExistsError
import java.lang.Exception
import kotlin.String


public class PlatformTransferAlreadyExistsException internal constructor(
  cause: PlatformTransferAlreadyExistsError
) : PortOneException(cause.message), CreatePlatformOrderCancelTransferException, CreatePlatformOrderTransferException {
  public val transferId: String = cause.transferId
  public val transferGraphqlId: String = cause.transferGraphqlId
}
