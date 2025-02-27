package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformTargetPartnerNotFoundError
import java.lang.Exception


/** 처리 대상 파트너가 존재하지 않는 경우 */
public class PlatformTargetPartnerNotFoundException internal constructor(
  cause: PlatformTargetPartnerNotFoundError
) : PortOneException(cause.message), ConnectBulkPartnerMemberCompanyException, DisconnectBulkPartnerMemberCompanyException {
}
