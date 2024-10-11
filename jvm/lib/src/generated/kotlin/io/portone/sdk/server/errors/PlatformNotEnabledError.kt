package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ArchivePlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.ArchivePlatformContractError
import io.portone.sdk.server.errors.ArchivePlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.ArchivePlatformPartnerError
import io.portone.sdk.server.errors.CancelPlatformAdditionalFeePolicyScheduleError
import io.portone.sdk.server.errors.CancelPlatformContractScheduleError
import io.portone.sdk.server.errors.CancelPlatformDiscountSharePolicyScheduleError
import io.portone.sdk.server.errors.CancelPlatformPartnerScheduleError
import io.portone.sdk.server.errors.CreatePlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.CreatePlatformContractError
import io.portone.sdk.server.errors.CreatePlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.CreatePlatformManualTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderTransferError
import io.portone.sdk.server.errors.CreatePlatformPartnerError
import io.portone.sdk.server.errors.CreatePlatformPartnersError
import io.portone.sdk.server.errors.DeletePlatformTransferError
import io.portone.sdk.server.errors.GetPlatformAccountHolderError
import io.portone.sdk.server.errors.GetPlatformAccountTransfersError
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePoliciesError
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePolicyScheduleError
import io.portone.sdk.server.errors.GetPlatformBulkPayoutsError
import io.portone.sdk.server.errors.GetPlatformContractError
import io.portone.sdk.server.errors.GetPlatformContractScheduleError
import io.portone.sdk.server.errors.GetPlatformContractsError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePoliciesError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyFilterOptionsError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyScheduleError
import io.portone.sdk.server.errors.GetPlatformError
import io.portone.sdk.server.errors.GetPlatformPartnerError
import io.portone.sdk.server.errors.GetPlatformPartnerFilterOptionsError
import io.portone.sdk.server.errors.GetPlatformPartnerScheduleError
import io.portone.sdk.server.errors.GetPlatformPartnerSettlementsError
import io.portone.sdk.server.errors.GetPlatformPartnersError
import io.portone.sdk.server.errors.GetPlatformPayoutsError
import io.portone.sdk.server.errors.GetPlatformTransferError
import io.portone.sdk.server.errors.GetPlatformTransferSummariesError
import io.portone.sdk.server.errors.RecoverPlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.RecoverPlatformContractError
import io.portone.sdk.server.errors.RecoverPlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.RecoverPlatformPartnerError
import io.portone.sdk.server.errors.RescheduleAdditionalFeePolicyError
import io.portone.sdk.server.errors.RescheduleContractError
import io.portone.sdk.server.errors.RescheduleDiscountSharePolicyError
import io.portone.sdk.server.errors.ReschedulePartnerError
import io.portone.sdk.server.errors.ScheduleAdditionalFeePolicyError
import io.portone.sdk.server.errors.ScheduleContractError
import io.portone.sdk.server.errors.ScheduleDiscountSharePolicyError
import io.portone.sdk.server.errors.SchedulePartnerError
import io.portone.sdk.server.errors.SchedulePlatformPartnersError
import io.portone.sdk.server.errors.UpdatePlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.UpdatePlatformContractError
import io.portone.sdk.server.errors.UpdatePlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.UpdatePlatformError
import io.portone.sdk.server.errors.UpdatePlatformPartnerError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우 */
@Serializable
@SerialName("PLATFORM_NOT_ENABLED")
public data class PlatformNotEnabledError(
  val message: String? = null,
): ArchivePlatformAdditionalFeePolicyError,
  ArchivePlatformContractError,
  ArchivePlatformDiscountSharePolicyError,
  ArchivePlatformPartnerError,
  CancelPlatformAdditionalFeePolicyScheduleError,
  CancelPlatformContractScheduleError,
  CancelPlatformDiscountSharePolicyScheduleError,
  CancelPlatformPartnerScheduleError,
  CreatePlatformAdditionalFeePolicyError,
  CreatePlatformContractError,
  CreatePlatformDiscountSharePolicyError,
  CreatePlatformManualTransferError,
  CreatePlatformOrderCancelTransferError,
  CreatePlatformOrderTransferError,
  CreatePlatformPartnerError,
  CreatePlatformPartnersError,
  DeletePlatformTransferError,
  GetPlatformAccountHolderError,
  GetPlatformAccountTransfersError,
  GetPlatformAdditionalFeePoliciesError,
  GetPlatformAdditionalFeePolicyError,
  GetPlatformAdditionalFeePolicyScheduleError,
  GetPlatformBulkPayoutsError,
  GetPlatformContractError,
  GetPlatformContractScheduleError,
  GetPlatformContractsError,
  GetPlatformDiscountSharePoliciesError,
  GetPlatformDiscountSharePolicyError,
  GetPlatformDiscountSharePolicyFilterOptionsError,
  GetPlatformDiscountSharePolicyScheduleError,
  GetPlatformError,
  GetPlatformPartnerError,
  GetPlatformPartnerFilterOptionsError,
  GetPlatformPartnerScheduleError,
  GetPlatformPartnerSettlementsError,
  GetPlatformPartnersError,
  GetPlatformPayoutsError,
  GetPlatformTransferError,
  GetPlatformTransferSummariesError,
  RecoverPlatformAdditionalFeePolicyError,
  RecoverPlatformContractError,
  RecoverPlatformDiscountSharePolicyError,
  RecoverPlatformPartnerError,
  RescheduleAdditionalFeePolicyError,
  RescheduleContractError,
  RescheduleDiscountSharePolicyError,
  ReschedulePartnerError,
  ScheduleAdditionalFeePolicyError,
  ScheduleContractError,
  ScheduleDiscountSharePolicyError,
  SchedulePartnerError,
  SchedulePlatformPartnersError,
  UpdatePlatformAdditionalFeePolicyError,
  UpdatePlatformContractError,
  UpdatePlatformDiscountSharePolicyError,
  UpdatePlatformError,
  UpdatePlatformPartnerError
