package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우 */
@Serializable
@SerialName("PLATFORM_NOT_ENABLED")
internal data class PlatformNotEnabledError(
  override val message: String? = null,
) : ArchivePlatformAdditionalFeePolicyError.Recognized, ArchivePlatformContractError.Recognized, ArchivePlatformDiscountSharePolicyError.Recognized, ArchivePlatformPartnerError.Recognized, CancelPlatformAdditionalFeePolicyScheduleError.Recognized, CancelPlatformContractScheduleError.Recognized, CancelPlatformDiscountSharePolicyScheduleError.Recognized, CancelPlatformPartnerScheduleError.Recognized, CreatePlatformAdditionalFeePolicyError.Recognized, CreatePlatformContractError.Recognized, CreatePlatformDiscountSharePolicyError.Recognized, CreatePlatformManualTransferError.Recognized, CreatePlatformOrderCancelTransferError.Recognized, CreatePlatformOrderTransferError.Recognized, CreatePlatformPartnerError.Recognized, CreatePlatformPartnersError.Recognized, DeletePlatformTransferError.Recognized, GetPlatformAccountHolderError.Recognized, GetPlatformAccountTransfersError.Recognized, GetPlatformAdditionalFeePoliciesError.Recognized, GetPlatformAdditionalFeePolicyError.Recognized, GetPlatformAdditionalFeePolicyScheduleError.Recognized, GetPlatformBulkPayoutsError.Recognized, GetPlatformCompanyStateError.Recognized, GetPlatformContractError.Recognized, GetPlatformContractScheduleError.Recognized, GetPlatformContractsError.Recognized, GetPlatformDiscountSharePoliciesError.Recognized, GetPlatformDiscountSharePolicyError.Recognized, GetPlatformDiscountSharePolicyFilterOptionsError.Recognized, GetPlatformDiscountSharePolicyScheduleError.Recognized, GetPlatformError.Recognized, GetPlatformPartnerError.Recognized, GetPlatformPartnerFilterOptionsError.Recognized, GetPlatformPartnerScheduleError.Recognized, GetPlatformPartnerSettlementsError.Recognized, GetPlatformPartnersError.Recognized, GetPlatformPayoutsError.Recognized, GetPlatformSettingError.Recognized, GetPlatformTransferError.Recognized, GetPlatformTransferSummariesError.Recognized, RecoverPlatformAdditionalFeePolicyError.Recognized, RecoverPlatformContractError.Recognized, RecoverPlatformDiscountSharePolicyError.Recognized, RecoverPlatformPartnerError.Recognized, RescheduleAdditionalFeePolicyError.Recognized, RescheduleContractError.Recognized, RescheduleDiscountSharePolicyError.Recognized, ReschedulePartnerError.Recognized, ScheduleAdditionalFeePolicyError.Recognized, ScheduleContractError.Recognized, ScheduleDiscountSharePolicyError.Recognized, SchedulePartnerError.Recognized, SchedulePlatformPartnersError.Recognized, UpdatePlatformAdditionalFeePolicyError.Recognized, UpdatePlatformContractError.Recognized, UpdatePlatformDiscountSharePolicyError.Recognized, UpdatePlatformError.Recognized, UpdatePlatformPartnerError.Recognized, UpdatePlatformSettingError.Recognized


