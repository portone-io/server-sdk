package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bRegularMaintenanceTimeError
import java.lang.Exception


/** 금융기관 시스템이 정기 점검 중인 경우 */
public class B2bRegularMaintenanceTimeException(
  cause: B2bRegularMaintenanceTimeError
) : Exception(cause.message) {
}
