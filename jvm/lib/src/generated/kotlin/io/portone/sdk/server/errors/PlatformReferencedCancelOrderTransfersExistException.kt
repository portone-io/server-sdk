package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformReferencedCancelOrderTransfersExistError
import java.lang.Exception
import kotlin.Array
import kotlin.String


/** 취소 정산건이 참조 중인 정산건이 포함된 경우 */
public class PlatformReferencedCancelOrderTransfersExistException internal constructor(
  cause: PlatformReferencedCancelOrderTransfersExistError
) : PortOneException(cause.message), DeletePlatformPartnerSettlementsException {
  public val ids: List<String> = cause.ids
}
