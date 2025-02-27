package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformBtxNotEnabledError
import java.lang.Exception


/** BTX 기능이 활성화되지 않아 요청을 처리할 수 없는 경우 */
public class PlatformBtxNotEnabledException internal constructor(
  cause: PlatformBtxNotEnabledError
) : PortOneException(cause.message), ConnectBulkPartnerMemberCompanyException, ConnectPartnerMemberCompanyException, DisconnectBulkPartnerMemberCompanyException, DisconnectPartnerMemberCompanyException {
}
