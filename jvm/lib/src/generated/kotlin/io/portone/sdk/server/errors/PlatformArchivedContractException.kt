package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformArchivedContractError
import java.lang.Exception


/** 보관된 계약을 업데이트하려고 하는 경우 */
public class PlatformArchivedContractException internal constructor(
  cause: PlatformArchivedContractError
) : PortOneException(cause.message), ScheduleContractException, UpdatePlatformContractException {
}
