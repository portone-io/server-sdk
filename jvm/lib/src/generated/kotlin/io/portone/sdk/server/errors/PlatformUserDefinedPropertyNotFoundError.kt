package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 사용자 정의 속성이 존재 하지 않는 경우 */
@Serializable
@SerialName("PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND")
internal data class PlatformUserDefinedPropertyNotFoundError(
  override val message: String? = null,
) : CreatePlatformManualTransferError.Recognized, CreatePlatformOrderCancelTransferError.Recognized, CreatePlatformOrderTransferError.Recognized, CreatePlatformPartnerError.Recognized, CreatePlatformPartnersError.Recognized, SchedulePartnerError.Recognized, SchedulePlatformPartnersError.Recognized, UpdatePlatformPartnerError.Recognized


