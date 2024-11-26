package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformInsufficientDataToChangePartnerTypeError
import java.lang.Exception


/** 파트너 타입 수정에 필요한 데이터가 부족한 경우 */
public class PlatformInsufficientDataToChangePartnerTypeException internal constructor(
  cause: PlatformInsufficientDataToChangePartnerTypeError
) : PortOneException(cause.message), SchedulePartnerException, UpdatePlatformPartnerException {
}
