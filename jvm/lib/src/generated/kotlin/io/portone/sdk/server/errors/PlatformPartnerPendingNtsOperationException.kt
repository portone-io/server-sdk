package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformPartnerPendingNtsOperationError
import java.lang.Exception


/** 파트너의 국세청 연동/해제가 진행 중인 경우 */
public class PlatformPartnerPendingNtsOperationException internal constructor(
  cause: PlatformPartnerPendingNtsOperationError
) : PortOneException(cause.message), ArchivePlatformPartnerException, RecoverPlatformPartnerException {
}
