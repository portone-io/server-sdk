import * as Errors from "../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../client"
import { PolicyClient } from "./policy/client"
import { PartnerClient } from "./partner/client"
import { TransferClient } from "./transfer/client"
import { PartnerSettlementClient } from "./partnerSettlement/client"
import { PayoutClient } from "./payout/client"
import { BulkPayoutClient } from "./bulkPayout/client"
import { AccountClient } from "./account/client"
import { AccountTransferClient } from "./accountTransfer/client"
import type { CancelPlatformAdditionalFeePolicyScheduleResponse } from "../../generated/platform/CancelPlatformAdditionalFeePolicyScheduleResponse"
import type { CancelPlatformContractScheduleResponse } from "../../generated/platform/CancelPlatformContractScheduleResponse"
import type { CancelPlatformDiscountSharePolicyScheduleResponse } from "../../generated/platform/CancelPlatformDiscountSharePolicyScheduleResponse"
import type { CancelPlatformPartnerScheduleResponse } from "../../generated/platform/CancelPlatformPartnerScheduleResponse"
import type { Platform } from "../../generated/platform/Platform"
import type { PlatformAdditionalFeePolicy } from "../../generated/platform/PlatformAdditionalFeePolicy"
import type { PlatformContract } from "../../generated/platform/PlatformContract"
import type { PlatformDiscountSharePolicy } from "../../generated/platform/PlatformDiscountSharePolicy"
import type { PlatformDiscountSharePolicyFilterOptions } from "../../generated/platform/PlatformDiscountSharePolicyFilterOptions"
import type { PlatformPartner } from "../../generated/platform/PlatformPartner"
import type { PlatformPartnerFilterInput } from "../../generated/platform/PlatformPartnerFilterInput"
import type { PlatformPartnerFilterOptions } from "../../generated/platform/PlatformPartnerFilterOptions"
import type { PlatformRoundType } from "../../generated/platform/PlatformRoundType"
import type { ReschedulePlatformAdditionalFeePolicyResponse } from "../../generated/platform/ReschedulePlatformAdditionalFeePolicyResponse"
import type { ReschedulePlatformContractResponse } from "../../generated/platform/ReschedulePlatformContractResponse"
import type { ReschedulePlatformDiscountSharePolicyResponse } from "../../generated/platform/ReschedulePlatformDiscountSharePolicyResponse"
import type { ReschedulePlatformPartnerResponse } from "../../generated/platform/ReschedulePlatformPartnerResponse"
import type { SchedulePlatformAdditionalFeePolicyResponse } from "../../generated/platform/SchedulePlatformAdditionalFeePolicyResponse"
import type { SchedulePlatformContractResponse } from "../../generated/platform/SchedulePlatformContractResponse"
import type { SchedulePlatformDiscountSharePolicyResponse } from "../../generated/platform/SchedulePlatformDiscountSharePolicyResponse"
import type { SchedulePlatformPartnerResponse } from "../../generated/platform/SchedulePlatformPartnerResponse"
import type { SchedulePlatformPartnersBodyUpdate } from "../../generated/platform/SchedulePlatformPartnersBodyUpdate"
import type { SchedulePlatformPartnersResponse } from "../../generated/platform/SchedulePlatformPartnersResponse"
import type { UpdatePlatformAdditionalFeePolicyBody } from "../../generated/platform/UpdatePlatformAdditionalFeePolicyBody"
import type { UpdatePlatformBodySettlementFormula } from "../../generated/platform/UpdatePlatformBodySettlementFormula"
import type { UpdatePlatformBodySettlementRule } from "../../generated/platform/UpdatePlatformBodySettlementRule"
import type { UpdatePlatformContractBody } from "../../generated/platform/UpdatePlatformContractBody"
import type { UpdatePlatformDiscountSharePolicyBody } from "../../generated/platform/UpdatePlatformDiscountSharePolicyBody"
import type { UpdatePlatformPartnerBody } from "../../generated/platform/UpdatePlatformPartnerBody"
import type { UpdatePlatformResponse } from "../../generated/platform/UpdatePlatformResponse"
import type { CancelPlatformAdditionalFeePolicyScheduleError as _InternalCancelPlatformAdditionalFeePolicyScheduleError } from "../../generated/platform/CancelPlatformAdditionalFeePolicyScheduleError"
import type { CancelPlatformContractScheduleError as _InternalCancelPlatformContractScheduleError } from "../../generated/platform/CancelPlatformContractScheduleError"
import type { CancelPlatformDiscountSharePolicyScheduleError as _InternalCancelPlatformDiscountSharePolicyScheduleError } from "../../generated/platform/CancelPlatformDiscountSharePolicyScheduleError"
import type { CancelPlatformPartnerScheduleError as _InternalCancelPlatformPartnerScheduleError } from "../../generated/platform/CancelPlatformPartnerScheduleError"
import type { GetPlatformAdditionalFeePolicyScheduleError as _InternalGetPlatformAdditionalFeePolicyScheduleError } from "../../generated/platform/GetPlatformAdditionalFeePolicyScheduleError"
import type { GetPlatformContractScheduleError as _InternalGetPlatformContractScheduleError } from "../../generated/platform/GetPlatformContractScheduleError"
import type { GetPlatformDiscountSharePolicyFilterOptionsError as _InternalGetPlatformDiscountSharePolicyFilterOptionsError } from "../../generated/platform/GetPlatformDiscountSharePolicyFilterOptionsError"
import type { GetPlatformDiscountSharePolicyScheduleError as _InternalGetPlatformDiscountSharePolicyScheduleError } from "../../generated/platform/GetPlatformDiscountSharePolicyScheduleError"
import type { GetPlatformError as _InternalGetPlatformError } from "../../generated/platform/GetPlatformError"
import type { GetPlatformPartnerFilterOptionsError as _InternalGetPlatformPartnerFilterOptionsError } from "../../generated/platform/GetPlatformPartnerFilterOptionsError"
import type { GetPlatformPartnerScheduleError as _InternalGetPlatformPartnerScheduleError } from "../../generated/platform/GetPlatformPartnerScheduleError"
import type { RescheduleAdditionalFeePolicyError as _InternalRescheduleAdditionalFeePolicyError } from "../../generated/platform/RescheduleAdditionalFeePolicyError"
import type { RescheduleContractError as _InternalRescheduleContractError } from "../../generated/platform/RescheduleContractError"
import type { RescheduleDiscountSharePolicyError as _InternalRescheduleDiscountSharePolicyError } from "../../generated/platform/RescheduleDiscountSharePolicyError"
import type { ReschedulePartnerError as _InternalReschedulePartnerError } from "../../generated/platform/ReschedulePartnerError"
import type { ScheduleAdditionalFeePolicyError as _InternalScheduleAdditionalFeePolicyError } from "../../generated/platform/ScheduleAdditionalFeePolicyError"
import type { ScheduleContractError as _InternalScheduleContractError } from "../../generated/platform/ScheduleContractError"
import type { ScheduleDiscountSharePolicyError as _InternalScheduleDiscountSharePolicyError } from "../../generated/platform/ScheduleDiscountSharePolicyError"
import type { SchedulePartnerError as _InternalSchedulePartnerError } from "../../generated/platform/SchedulePartnerError"
import type { SchedulePlatformPartnersError as _InternalSchedulePlatformPartnersError } from "../../generated/platform/SchedulePlatformPartnersError"
import type { UpdatePlatformError as _InternalUpdatePlatformError } from "../../generated/platform/UpdatePlatformError"
export function PlatformClient(init: PortOneClientInit): PlatformClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPlatform: async (
			options?: {
			}
		): Promise<Platform> => {
			const response = await fetch(
				new URL("/platform", baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformError = await response.json()
				switch (errorResponse.type) {
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		updatePlatform: async (
			options?: {
				roundType?: PlatformRoundType,
				settlementFormula?: UpdatePlatformBodySettlementFormula,
				settlementRule?: UpdatePlatformBodySettlementRule,
			}
		): Promise<UpdatePlatformResponse> => {
			const roundType = options?.roundType
			const settlementFormula = options?.settlementFormula
			const settlementRule = options?.settlementRule
			const requestBody = JSON.stringify({
				roundType,
				settlementFormula,
				settlementRule,
			})
			const response = await fetch(
				new URL("/platform", baseUrl),
				{
					method: "PATCH",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalUpdatePlatformError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_INVALID_SETTLEMENT_FORMULA":
					throw new Errors.PlatformInvalidSettlementFormulaError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPlatformDiscountSharePolicyFilterOptions: async (
			options?: {
				isArchived?: boolean,
			}
		): Promise<PlatformDiscountSharePolicyFilterOptions> => {
			const isArchived = options?.isArchived
			const query = [
				["isArchived", isArchived],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/discount-share-policy-filter-options?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformDiscountSharePolicyFilterOptionsError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPlatformDiscountSharePolicySchedule: async (
			options: {
				id: string,
			}
		): Promise<PlatformDiscountSharePolicy> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformDiscountSharePolicyScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
					throw new Errors.PlatformDiscountSharePolicyNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		rescheduleDiscountSharePolicy: async (
			options: {
				id: string,
				update: UpdatePlatformDiscountSharePolicyBody,
				appliedAt: string,
			}
		): Promise<ReschedulePlatformDiscountSharePolicyResponse> => {
			const {
				id,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "PUT",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalRescheduleDiscountSharePolicyError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
					throw new Errors.PlatformDiscountSharePolicyNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		scheduleDiscountSharePolicy: async (
			options: {
				id: string,
				update: UpdatePlatformDiscountSharePolicyBody,
				appliedAt: string,
			}
		): Promise<SchedulePlatformDiscountSharePolicyResponse> => {
			const {
				id,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalScheduleDiscountSharePolicyError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ARCHIVED_DISCOUNT_SHARE_POLICY":
					throw new Errors.PlatformArchivedDiscountSharePolicyError(errorResponse)
				case "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
					throw new Errors.PlatformDiscountSharePolicyNotFoundError(errorResponse)
				case "PLATFORM_DISCOUNT_SHARE_POLICY_SCHEDULE_ALREADY_EXISTS":
					throw new Errors.PlatformDiscountSharePolicyScheduleAlreadyExistsError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		cancelPlatformDiscountSharePolicySchedule: async (
			options: {
				id: string,
			}
		): Promise<CancelPlatformDiscountSharePolicyScheduleResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalCancelPlatformDiscountSharePolicyScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
					throw new Errors.PlatformDiscountSharePolicyNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPlatformAdditionalFeePolicySchedule: async (
			options: {
				id: string,
			}
		): Promise<PlatformAdditionalFeePolicy> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformAdditionalFeePolicyScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
					throw new Errors.PlatformAdditionalFeePolicyNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		rescheduleAdditionalFeePolicy: async (
			options: {
				id: string,
				update: UpdatePlatformAdditionalFeePolicyBody,
				appliedAt: string,
			}
		): Promise<ReschedulePlatformAdditionalFeePolicyResponse> => {
			const {
				id,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "PUT",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalRescheduleAdditionalFeePolicyError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
					throw new Errors.PlatformAdditionalFeePolicyNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		scheduleAdditionalFeePolicy: async (
			options: {
				id: string,
				update: UpdatePlatformAdditionalFeePolicyBody,
				appliedAt: string,
			}
		): Promise<SchedulePlatformAdditionalFeePolicyResponse> => {
			const {
				id,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalScheduleAdditionalFeePolicyError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
					throw new Errors.PlatformAdditionalFeePolicyNotFoundError(errorResponse)
				case "PLATFORM_ADDITIONAL_FEE_POLICY_SCHEDULE_ALREADY_EXISTS":
					throw new Errors.PlatformAdditionalFeePolicyScheduleAlreadyExistsError(errorResponse)
				case "PLATFORM_ARCHIVED_ADDITIONAL_FEE_POLICY":
					throw new Errors.PlatformArchivedAdditionalFeePolicyError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		cancelPlatformAdditionalFeePolicySchedule: async (
			options: {
				id: string,
			}
		): Promise<CancelPlatformAdditionalFeePolicyScheduleResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalCancelPlatformAdditionalFeePolicyScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
					throw new Errors.PlatformAdditionalFeePolicyNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPlatformPartnerFilterOptions: async (
			options?: {
				isArchived?: boolean,
			}
		): Promise<PlatformPartnerFilterOptions> => {
			const isArchived = options?.isArchived
			const query = [
				["isArchived", isArchived],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/partner-filter-options?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformPartnerFilterOptionsError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPlatformPartnerSchedule: async (
			options: {
				id: string,
			}
		): Promise<PlatformPartner> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/partners/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformPartnerScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "PLATFORM_PARTNER_NOT_FOUND":
					throw new Errors.PlatformPartnerNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		reschedulePartner: async (
			options: {
				id: string,
				update: UpdatePlatformPartnerBody,
				appliedAt: string,
			}
		): Promise<ReschedulePlatformPartnerResponse> => {
			const {
				id,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/partners/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "PUT",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalReschedulePartnerError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "PLATFORM_PARTNER_NOT_FOUND":
					throw new Errors.PlatformPartnerNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		schedulePartner: async (
			options: {
				id: string,
				update: UpdatePlatformPartnerBody,
				appliedAt: string,
			}
		): Promise<SchedulePlatformPartnerResponse> => {
			const {
				id,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/partners/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalSchedulePartnerError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED":
					throw new Errors.PlatformAccountVerificationAlreadyUsedError(errorResponse)
				case "PLATFORM_ACCOUNT_VERIFICATION_FAILED":
					throw new Errors.PlatformAccountVerificationFailedError(errorResponse)
				case "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND":
					throw new Errors.PlatformAccountVerificationNotFoundError(errorResponse)
				case "PLATFORM_ARCHIVED_PARTNER":
					throw new Errors.PlatformArchivedPartnerError(errorResponse)
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_INSUFFICIENT_DATA_TO_CHANGE_PARTNER_TYPE":
					throw new Errors.PlatformInsufficientDataToChangePartnerTypeError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "PLATFORM_PARTNER_NOT_FOUND":
					throw new Errors.PlatformPartnerNotFoundError(errorResponse)
				case "PLATFORM_PARTNER_SCHEDULE_ALREADY_EXISTS":
					throw new Errors.PlatformPartnerScheduleAlreadyExistsError(errorResponse)
				case "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
					throw new Errors.PlatformUserDefinedPropertyNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		cancelPlatformPartnerSchedule: async (
			options: {
				id: string,
			}
		): Promise<CancelPlatformPartnerScheduleResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/partners/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalCancelPlatformPartnerScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "PLATFORM_PARTNER_NOT_FOUND":
					throw new Errors.PlatformPartnerNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		schedulePlatformPartners: async (
			options: {
				filter?: PlatformPartnerFilterInput,
				update: SchedulePlatformPartnersBodyUpdate,
				appliedAt: string,
			}
		): Promise<SchedulePlatformPartnersResponse> => {
			const {
				filter,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				filter,
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL("/platform/partners/schedule", baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalSchedulePlatformPartnersError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ARCHIVED_PARTNERS_CANNOT_BE_SCHEDULED":
					throw new Errors.PlatformArchivedPartnersCannotBeScheduledError(errorResponse)
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "PLATFORM_PARTNER_SCHEDULES_ALREADY_EXIST":
					throw new Errors.PlatformPartnerSchedulesAlreadyExistError(errorResponse)
				case "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
					throw new Errors.PlatformUserDefinedPropertyNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPlatformContractSchedule: async (
			options: {
				id: string,
			}
		): Promise<PlatformContract> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformContractScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		rescheduleContract: async (
			options: {
				id: string,
				update: UpdatePlatformContractBody,
				appliedAt: string,
			}
		): Promise<ReschedulePlatformContractResponse> => {
			const {
				id,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "PUT",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalRescheduleContractError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		scheduleContract: async (
			options: {
				id: string,
				update: UpdatePlatformContractBody,
				appliedAt: string,
			}
		): Promise<SchedulePlatformContractResponse> => {
			const {
				id,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalScheduleContractError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ARCHIVED_CONTRACT":
					throw new Errors.PlatformArchivedContractError(errorResponse)
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_CONTRACT_SCHEDULE_ALREADY_EXISTS":
					throw new Errors.PlatformContractScheduleAlreadyExistsError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		cancelPlatformContractSchedule: async (
			options: {
				id: string,
			}
		): Promise<CancelPlatformContractScheduleResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}/schedule`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalCancelPlatformContractScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		policy: PolicyClient(init),
		partner: PartnerClient(init),
		transfer: TransferClient(init),
		partnerSettlement: PartnerSettlementClient(init),
		payout: PayoutClient(init),
		bulkPayout: BulkPayoutClient(init),
		account: AccountClient(init),
		accountTransfer: AccountTransferClient(init),
	}
}
export type PlatformClient = {
	/**
	 * 고객사의 플랫폼 정보를 조회합니다.
	 * 요청된 Authorization header 를 통해 자동으로 요청자의 고객사를 특정합니다.
	 *
	 * @throws {@link GetPlatformError}
	 */
	getPlatform: (
		options?: {
		}
	) => Promise<Platform>
	/**
	 * 고객사의 플랫폼 관련 정보를 업데이트합니다.
	 * 요청된 Authorization header 를 통해 자동으로 요청자의 고객사를 특정합니다.
	 *
	 * @throws {@link UpdatePlatformError}
	 */
	updatePlatform: (
		options?: {
			/** 파트너 정산금액의 소수점 처리 방식 */
			roundType?: PlatformRoundType,
			/** 수수료 및 할인 분담 정책 관련 계산식 */
			settlementFormula?: UpdatePlatformBodySettlementFormula,
			/** 정산 규칙 */
			settlementRule?: UpdatePlatformBodySettlementRule,
		}
	) => Promise<UpdatePlatformResponse>
	/**
	 * 할인 분담 정책 다건 조회 시 필요한 필터 옵션을 조회합니다.
	 *
	 * @throws {@link GetPlatformDiscountSharePolicyFilterOptionsError}
	 */
	getPlatformDiscountSharePolicyFilterOptions: (
		options?: {
			/**
			 * 보관 조회 여부
			 *
			 * true 이면 보관된 할인 분담의 필터 옵션을 조회하고, false 이면 보관되지 않은 할인 분담의 필터 옵션을 조회합니다. 기본값은 false 입니다.
			 */
			isArchived?: boolean,
		}
	) => Promise<PlatformDiscountSharePolicyFilterOptions>
	/**
	 * 주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 조회합니다.
	 *
	 * @throws {@link GetPlatformDiscountSharePolicyScheduleError}
	 */
	getPlatformDiscountSharePolicySchedule: (
		options: {
			/** 할인 분담 정책 아이디 */
			id: string,
		}
	) => Promise<PlatformDiscountSharePolicy>
	/**
	 * 주어진 아이디에 대응되는 할인 분담에 예약 업데이트를 재설정합니다.
	 *
	 * @throws {@link RescheduleDiscountSharePolicyError}
	 */
	rescheduleDiscountSharePolicy: (
		options: {
			/** 할인 분담 정책 아이디 */
			id: string,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformDiscountSharePolicyBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<ReschedulePlatformDiscountSharePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 할인 분담에 업데이트를 예약합니다.
	 *
	 * @throws {@link ScheduleDiscountSharePolicyError}
	 */
	scheduleDiscountSharePolicy: (
		options: {
			/** 할인 분담 정책 아이디 */
			id: string,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformDiscountSharePolicyBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<SchedulePlatformDiscountSharePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 취소합니다.
	 *
	 * @throws {@link CancelPlatformDiscountSharePolicyScheduleError}
	 */
	cancelPlatformDiscountSharePolicySchedule: (
		options: {
			/** 할인 분담 정책 아이디 */
			id: string,
		}
	) => Promise<CancelPlatformDiscountSharePolicyScheduleResponse>
	/**
	 * 주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 조회합니다.
	 *
	 * @throws {@link GetPlatformAdditionalFeePolicyScheduleError}
	 */
	getPlatformAdditionalFeePolicySchedule: (
		options: {
			/** 추가 수수료 정책 아이디 */
			id: string,
		}
	) => Promise<PlatformAdditionalFeePolicy>
	/** @throws {@link RescheduleAdditionalFeePolicyError} */
	rescheduleAdditionalFeePolicy: (
		options: {
			/** 추가 수수료 정책 아이디 */
			id: string,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformAdditionalFeePolicyBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<ReschedulePlatformAdditionalFeePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 추가 수수료 정책에 업데이트를 예약합니다.
	 *
	 * @throws {@link ScheduleAdditionalFeePolicyError}
	 */
	scheduleAdditionalFeePolicy: (
		options: {
			/** 추가 수수료 정책 아이디 */
			id: string,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformAdditionalFeePolicyBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<SchedulePlatformAdditionalFeePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 취소합니다.
	 *
	 * @throws {@link CancelPlatformAdditionalFeePolicyScheduleError}
	 */
	cancelPlatformAdditionalFeePolicySchedule: (
		options: {
			/** 추가 수수료 정책 아이디 */
			id: string,
		}
	) => Promise<CancelPlatformAdditionalFeePolicyScheduleResponse>
	/**
	 * 파트너 다건 조회 시 필요한 필터 옵션을 조회합니다.
	 *
	 * @throws {@link GetPlatformPartnerFilterOptionsError}
	 */
	getPlatformPartnerFilterOptions: (
		options?: {
			/**
			 * 보관 조회 여부
			 *
			 * true 이면 보관된 파트너의 필터 옵션을 조회하고, false 이면 보관되지 않은 파트너의 필터 옵션을 조회합니다. 기본값은 false 입니다.
			 */
			isArchived?: boolean,
		}
	) => Promise<PlatformPartnerFilterOptions>
	/**
	 * 주어진 아이디에 대응되는 파트너의 예약 업데이트를 조회합니다.
	 *
	 * @throws {@link GetPlatformPartnerScheduleError}
	 */
	getPlatformPartnerSchedule: (
		options: {
			/** 파트너 아이디 */
			id: string,
		}
	) => Promise<PlatformPartner>
	/**
	 * 주어진 아이디에 대응되는 파트너에 예약 업데이트를 재설정합니다.
	 *
	 * @throws {@link ReschedulePartnerError}
	 */
	reschedulePartner: (
		options: {
			/** 파트너 아이디 */
			id: string,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformPartnerBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<ReschedulePlatformPartnerResponse>
	/**
	 * 주어진 아이디에 대응되는 파트너에 업데이트를 예약합니다.
	 *
	 * @throws {@link SchedulePartnerError}
	 */
	schedulePartner: (
		options: {
			/** 파트너 아이디 */
			id: string,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformPartnerBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<SchedulePlatformPartnerResponse>
	/**
	 * 주어진 아이디에 대응되는 파트너의 예약 업데이트를 취소합니다.
	 *
	 * @throws {@link CancelPlatformPartnerScheduleError}
	 */
	cancelPlatformPartnerSchedule: (
		options: {
			/** 파트너 아이디 */
			id: string,
		}
	) => Promise<CancelPlatformPartnerScheduleResponse>
	/** @throws {@link SchedulePlatformPartnersError} */
	schedulePlatformPartners: (
		options: {
			filter?: PlatformPartnerFilterInput,
			update: SchedulePlatformPartnersBodyUpdate,
			/** (RFC 3339 date-time) */
			appliedAt: string,
		}
	) => Promise<SchedulePlatformPartnersResponse>
	/**
	 * 주어진 아이디에 대응되는 계약의 예약 업데이트를 조회합니다.
	 *
	 * @throws {@link GetPlatformContractScheduleError}
	 */
	getPlatformContractSchedule: (
		options: {
			/** 계약 아이디 */
			id: string,
		}
	) => Promise<PlatformContract>
	/**
	 * 주어진 아이디에 대응되는 계약에 예약 업데이트를 재설정합니다.
	 *
	 * @throws {@link RescheduleContractError}
	 */
	rescheduleContract: (
		options: {
			/** 계약 아이디 */
			id: string,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformContractBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<ReschedulePlatformContractResponse>
	/**
	 * 주어진 아이디에 대응되는 계약에 업데이트를 예약합니다.
	 *
	 * @throws {@link ScheduleContractError}
	 */
	scheduleContract: (
		options: {
			/** 계약 아이디 */
			id: string,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformContractBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<SchedulePlatformContractResponse>
	/**
	 * 주어진 아이디에 대응되는 계약의 예약 업데이트를 취소합니다.
	 *
	 * @throws {@link CancelPlatformContractScheduleError}
	 */
	cancelPlatformContractSchedule: (
		options: {
			/** 계약 아이디 */
			id: string,
		}
	) => Promise<CancelPlatformContractScheduleResponse>
	policy: PolicyClient
	partner: PartnerClient
	transfer: TransferClient
	partnerSettlement: PartnerSettlementClient
	payout: PayoutClient
	bulkPayout: BulkPayoutClient
	account: AccountClient
	accountTransfer: AccountTransferClient
}
export type GetPlatformError =
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformError(error: Error): error is GetPlatformError {
	return (
		error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type UpdatePlatformError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformInvalidSettlementFormulaError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isUpdatePlatformError(error: Error): error is UpdatePlatformError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformInvalidSettlementFormulaError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetPlatformDiscountSharePolicyFilterOptionsError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformDiscountSharePolicyFilterOptionsError(error: Error): error is GetPlatformDiscountSharePolicyFilterOptionsError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetPlatformDiscountSharePolicyScheduleError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformDiscountSharePolicyNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformDiscountSharePolicyScheduleError(error: Error): error is GetPlatformDiscountSharePolicyScheduleError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformDiscountSharePolicyNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type RescheduleDiscountSharePolicyError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformDiscountSharePolicyNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isRescheduleDiscountSharePolicyError(error: Error): error is RescheduleDiscountSharePolicyError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformDiscountSharePolicyNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type ScheduleDiscountSharePolicyError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformArchivedDiscountSharePolicyError
	| Errors.PlatformDiscountSharePolicyNotFoundError
	| Errors.PlatformDiscountSharePolicyScheduleAlreadyExistsError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isScheduleDiscountSharePolicyError(error: Error): error is ScheduleDiscountSharePolicyError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformArchivedDiscountSharePolicyError
		|| error instanceof Errors.PlatformDiscountSharePolicyNotFoundError
		|| error instanceof Errors.PlatformDiscountSharePolicyScheduleAlreadyExistsError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type CancelPlatformDiscountSharePolicyScheduleError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformDiscountSharePolicyNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isCancelPlatformDiscountSharePolicyScheduleError(error: Error): error is CancelPlatformDiscountSharePolicyScheduleError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformDiscountSharePolicyNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetPlatformAdditionalFeePolicyScheduleError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformAdditionalFeePolicyNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformAdditionalFeePolicyScheduleError(error: Error): error is GetPlatformAdditionalFeePolicyScheduleError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformAdditionalFeePolicyNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type RescheduleAdditionalFeePolicyError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformAdditionalFeePolicyNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isRescheduleAdditionalFeePolicyError(error: Error): error is RescheduleAdditionalFeePolicyError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformAdditionalFeePolicyNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type ScheduleAdditionalFeePolicyError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformAdditionalFeePolicyNotFoundError
	| Errors.PlatformAdditionalFeePolicyScheduleAlreadyExistsError
	| Errors.PlatformArchivedAdditionalFeePolicyError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isScheduleAdditionalFeePolicyError(error: Error): error is ScheduleAdditionalFeePolicyError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformAdditionalFeePolicyNotFoundError
		|| error instanceof Errors.PlatformAdditionalFeePolicyScheduleAlreadyExistsError
		|| error instanceof Errors.PlatformArchivedAdditionalFeePolicyError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type CancelPlatformAdditionalFeePolicyScheduleError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformAdditionalFeePolicyNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isCancelPlatformAdditionalFeePolicyScheduleError(error: Error): error is CancelPlatformAdditionalFeePolicyScheduleError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformAdditionalFeePolicyNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetPlatformPartnerFilterOptionsError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformPartnerFilterOptionsError(error: Error): error is GetPlatformPartnerFilterOptionsError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetPlatformPartnerScheduleError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformPartnerNotFoundError
	| Errors.UnauthorizedError
export function isGetPlatformPartnerScheduleError(error: Error): error is GetPlatformPartnerScheduleError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformPartnerNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type ReschedulePartnerError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformContractNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformPartnerNotFoundError
	| Errors.UnauthorizedError
export function isReschedulePartnerError(error: Error): error is ReschedulePartnerError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformContractNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformPartnerNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type SchedulePartnerError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformAccountVerificationAlreadyUsedError
	| Errors.PlatformAccountVerificationFailedError
	| Errors.PlatformAccountVerificationNotFoundError
	| Errors.PlatformArchivedPartnerError
	| Errors.PlatformContractNotFoundError
	| Errors.PlatformInsufficientDataToChangePartnerTypeError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformPartnerNotFoundError
	| Errors.PlatformPartnerScheduleAlreadyExistsError
	| Errors.PlatformUserDefinedPropertyNotFoundError
	| Errors.UnauthorizedError
export function isSchedulePartnerError(error: Error): error is SchedulePartnerError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformAccountVerificationAlreadyUsedError
		|| error instanceof Errors.PlatformAccountVerificationFailedError
		|| error instanceof Errors.PlatformAccountVerificationNotFoundError
		|| error instanceof Errors.PlatformArchivedPartnerError
		|| error instanceof Errors.PlatformContractNotFoundError
		|| error instanceof Errors.PlatformInsufficientDataToChangePartnerTypeError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformPartnerNotFoundError
		|| error instanceof Errors.PlatformPartnerScheduleAlreadyExistsError
		|| error instanceof Errors.PlatformUserDefinedPropertyNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type CancelPlatformPartnerScheduleError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformPartnerNotFoundError
	| Errors.UnauthorizedError
export function isCancelPlatformPartnerScheduleError(error: Error): error is CancelPlatformPartnerScheduleError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformPartnerNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type SchedulePlatformPartnersError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformArchivedPartnersCannotBeScheduledError
	| Errors.PlatformContractNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformPartnerSchedulesAlreadyExistError
	| Errors.PlatformUserDefinedPropertyNotFoundError
	| Errors.UnauthorizedError
export function isSchedulePlatformPartnersError(error: Error): error is SchedulePlatformPartnersError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformArchivedPartnersCannotBeScheduledError
		|| error instanceof Errors.PlatformContractNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformPartnerSchedulesAlreadyExistError
		|| error instanceof Errors.PlatformUserDefinedPropertyNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetPlatformContractScheduleError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformContractNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformContractScheduleError(error: Error): error is GetPlatformContractScheduleError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformContractNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type RescheduleContractError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformContractNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isRescheduleContractError(error: Error): error is RescheduleContractError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformContractNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type ScheduleContractError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformArchivedContractError
	| Errors.PlatformContractNotFoundError
	| Errors.PlatformContractScheduleAlreadyExistsError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isScheduleContractError(error: Error): error is ScheduleContractError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformArchivedContractError
		|| error instanceof Errors.PlatformContractNotFoundError
		|| error instanceof Errors.PlatformContractScheduleAlreadyExistsError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type CancelPlatformContractScheduleError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformContractNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isCancelPlatformContractScheduleError(error: Error): error is CancelPlatformContractScheduleError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformContractNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
