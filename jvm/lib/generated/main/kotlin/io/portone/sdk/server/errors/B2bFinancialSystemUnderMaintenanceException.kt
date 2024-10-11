package io.portone.sdk.server.errors

import io.portone.sdk.server.b2b.B2bFinancialSystemUnderMaintenanceError
import java.lang.Exception


/** 금융기관 시스템이 점검 중인 경우 */
public class B2bFinancialSystemUnderMaintenanceException(
  cause: B2bFinancialSystemUnderMaintenanceError
) : Exception(cause.message) {
}
