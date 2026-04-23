package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformArchivedPartnerNtsNotAllowedError
import java.lang.Exception


/** 보관된 파트너는 국세청 연동/연동해제를 할 수 없는 경우 */
public class PlatformArchivedPartnerNtsNotAllowedException internal constructor(
  cause: PlatformArchivedPartnerNtsNotAllowedError
) : PortOneException(cause.message), ConnectPartnerCounterpartyException, DisconnectPartnerCounterpartyException {
}
