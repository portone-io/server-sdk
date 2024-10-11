package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우 */
@Serializable
@SerialName("PLATFORM_NOT_ENABLED")
public data class PlatformNotEnabledError(
  override val message: String? = null,
): ArchivePlatformAdditionalFeePolicyError,
  ): ArchivePlatformContractError,
    ): ArchivePlatformDiscountSharePolicyError,
      ): ArchivePlatformPartnerError,
        ): CancelPlatformAdditionalFeePolicyScheduleError,
          ): CancelPlatformContractScheduleError,
            ): CancelPlatformDiscountSharePolicyScheduleError,
              ): CancelPlatformPartnerScheduleError,
                ): CreatePlatformAdditionalFeePolicyError,
                  ): CreatePlatformContractError,
                    ): CreatePlatformDiscountSharePolicyError,
                      ): CreatePlatformManualTransferError,
                        ): CreatePlatformOrderCancelTransferError,
                          ): CreatePlatformOrderTransferError,
                            ): CreatePlatformPartnerError,
                              ): CreatePlatformPartnersError,
                                ): DeletePlatformTransferError,
                                  ): GetPlatformAccountHolderError,
                                    ): GetPlatformAccountTransfersError,
                                      ): GetPlatformAdditionalFeePoliciesError,
                                        ): GetPlatformAdditionalFeePolicyError,
                                          ): GetPlatformAdditionalFeePolicyScheduleError,
                                            ): GetPlatformBulkPayoutsError,
                                              ): GetPlatformContractError,
                                                ): GetPlatformContractScheduleError,
                                                  ): GetPlatformContractsError,
                                                    ): GetPlatformDiscountSharePoliciesError,
                                                      ): GetPlatformDiscountSharePolicyError,
                                                        ): GetPlatformDiscountSharePolicyFilterOptionsError,
                                                          ): GetPlatformDiscountSharePolicyScheduleError,
                                                            ): GetPlatformError,
                                                              ): GetPlatformPartnerError,
                                                                ): GetPlatformPartnerFilterOptionsError,
                                                                  ): GetPlatformPartnerScheduleError,
                                                                    ): GetPlatformPartnerSettlementsError,
                                                                      ): GetPlatformPartnersError,
                                                                        ): GetPlatformPayoutsError,
                                                                          ): GetPlatformTransferError,
                                                                            ): GetPlatformTransferSummariesError,
                                                                              ): RecoverPlatformAdditionalFeePolicyError,
                                                                                ): RecoverPlatformContractError,
                                                                                  ): RecoverPlatformDiscountSharePolicyError,
                                                                                    ): RecoverPlatformPartnerError,
                                                                                      ): RescheduleAdditionalFeePolicyError,
                                                                                        ): RescheduleContractError,
                                                                                          ): RescheduleDiscountSharePolicyError,
                                                                                            ): ReschedulePartnerError,
                                                                                              ): ScheduleAdditionalFeePolicyError,
                                                                                                ): ScheduleContractError,
                                                                                                  ): ScheduleDiscountSharePolicyError,
                                                                                                    ): SchedulePartnerError,
                                                                                                      ): SchedulePlatformPartnersError,
                                                                                                        ): UpdatePlatformAdditionalFeePolicyError,
                                                                                                          ): UpdatePlatformContractError,
                                                                                                            ): UpdatePlatformDiscountSharePolicyError,
                                                                                                              ): UpdatePlatformError,
                                                                                                                ): UpdatePlatformPartnerError,