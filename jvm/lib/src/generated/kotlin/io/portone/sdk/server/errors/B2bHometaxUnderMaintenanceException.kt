package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bHometaxUnderMaintenanceError
import java.lang.Exception


/** 홈택스가 점검중이거나 순단이 발생한 경우 */
public class B2bHometaxUnderMaintenanceException(
  cause: B2bHometaxUnderMaintenanceError
) : Exception(cause.message) {
}
