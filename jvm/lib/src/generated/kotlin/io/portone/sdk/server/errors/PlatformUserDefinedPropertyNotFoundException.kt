package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformUserDefinedPropertyNotFoundError
import java.lang.Exception


/** 사용자 정의 속성이 존재 하지 않는 경우 */
public class PlatformUserDefinedPropertyNotFoundException internal constructor(
  cause: PlatformUserDefinedPropertyNotFoundError
) : PortOneException(cause.message), CreatePlatformManualTransferException, CreatePlatformOrderCancelTransferException, CreatePlatformOrderTransferException, CreatePlatformPartnerException, CreatePlatformPartnersException, SchedulePartnerException, SchedulePlatformPartnersException, UpdatePlatformPartnerException {
}
