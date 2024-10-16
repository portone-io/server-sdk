package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformManualTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderTransferError
import io.portone.sdk.server.errors.CreatePlatformPartnerError
import io.portone.sdk.server.errors.CreatePlatformPartnersError
import io.portone.sdk.server.errors.SchedulePartnerError
import io.portone.sdk.server.errors.SchedulePlatformPartnersError
import io.portone.sdk.server.errors.UpdatePlatformPartnerError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 사용자 정의 속성이 존재 하지 않는 경우 */
@Serializable
@SerialName("PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND")
@ConsistentCopyVisibility
public data class PlatformUserDefinedPropertyNotFoundError internal constructor(
  override val message: String? = null,
): CreatePlatformManualTransferError,
  CreatePlatformOrderCancelTransferError,
  CreatePlatformOrderTransferError,
  CreatePlatformPartnerError,
  CreatePlatformPartnersError,
  SchedulePartnerError,
  SchedulePlatformPartnersError,
  UpdatePlatformPartnerError
