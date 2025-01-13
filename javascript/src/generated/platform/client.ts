import { PlatformError } from "./PlatformError"
import type { Unrecognized } from "./../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../client"
import { PolicyClient } from "./policy/client"
import { PartnerClient } from "./partner/client"
import { TransferClient } from "./transfer/client"
import { PartnerSettlementClient } from "./partnerSettlement/client"
import { PayoutClient } from "./payout/client"
import { BulkPayoutClient } from "./bulkPayout/client"
import { AccountClient } from "./account/client"
import { CompanyClient } from "./company/client"
import { AccountTransferClient } from "./accountTransfer/client"
import type { CancelPlatformAdditionalFeePolicyScheduleResponse } from "../../generated/platform/CancelPlatformAdditionalFeePolicyScheduleResponse"
import type { CancelPlatformContractScheduleResponse } from "../../generated/platform/CancelPlatformContractScheduleResponse"
import type { CancelPlatformDiscountSharePolicyScheduleResponse } from "../../generated/platform/CancelPlatformDiscountSharePolicyScheduleResponse"
import type { CancelPlatformPartnerScheduleResponse } from "../../generated/platform/CancelPlatformPartnerScheduleResponse"
import type { ForbiddenError } from "../../generated/common/ForbiddenError"
import type { InvalidRequestError } from "../../generated/common/InvalidRequestError"
import type { Platform } from "../../generated/platform/Platform"
import type { PlatformAccountVerificationAlreadyUsedError } from "../../generated/platform/PlatformAccountVerificationAlreadyUsedError"
import type { PlatformAccountVerificationFailedError } from "../../generated/platform/PlatformAccountVerificationFailedError"
import type { PlatformAccountVerificationNotFoundError } from "../../generated/platform/PlatformAccountVerificationNotFoundError"
import type { PlatformAdditionalFeePolicy } from "../../generated/platform/PlatformAdditionalFeePolicy"
import type { PlatformAdditionalFeePolicyNotFoundError } from "../../generated/platform/PlatformAdditionalFeePolicyNotFoundError"
import type { PlatformAdditionalFeePolicyScheduleAlreadyExistsError } from "../../generated/platform/PlatformAdditionalFeePolicyScheduleAlreadyExistsError"
import type { PlatformArchivedAdditionalFeePolicyError } from "../../generated/platform/PlatformArchivedAdditionalFeePolicyError"
import type { PlatformArchivedContractError } from "../../generated/platform/PlatformArchivedContractError"
import type { PlatformArchivedDiscountSharePolicyError } from "../../generated/platform/PlatformArchivedDiscountSharePolicyError"
import type { PlatformArchivedPartnerError } from "../../generated/platform/PlatformArchivedPartnerError"
import type { PlatformArchivedPartnersCannotBeScheduledError } from "../../generated/platform/PlatformArchivedPartnersCannotBeScheduledError"
import type { PlatformCompanyVerificationAlreadyUsedError } from "../../generated/platform/PlatformCompanyVerificationAlreadyUsedError"
import type { PlatformContract } from "../../generated/platform/PlatformContract"
import type { PlatformContractNotFoundError } from "../../generated/platform/PlatformContractNotFoundError"
import type { PlatformContractScheduleAlreadyExistsError } from "../../generated/platform/PlatformContractScheduleAlreadyExistsError"
import type { PlatformDiscountSharePolicy } from "../../generated/platform/PlatformDiscountSharePolicy"
import type { PlatformDiscountSharePolicyFilterOptions } from "../../generated/platform/PlatformDiscountSharePolicyFilterOptions"
import type { PlatformDiscountSharePolicyNotFoundError } from "../../generated/platform/PlatformDiscountSharePolicyNotFoundError"
import type { PlatformDiscountSharePolicyScheduleAlreadyExistsError } from "../../generated/platform/PlatformDiscountSharePolicyScheduleAlreadyExistsError"
import type { PlatformInsufficientDataToChangePartnerTypeError } from "../../generated/platform/PlatformInsufficientDataToChangePartnerTypeError"
import type { PlatformInvalidSettlementFormulaError } from "../../generated/platform/PlatformInvalidSettlementFormulaError"
import type { PlatformMemberCompanyConnectedPartnerBrnUnchangeableError } from "../../generated/platform/PlatformMemberCompanyConnectedPartnerBrnUnchangeableError"
import type { PlatformMemberCompanyConnectedPartnerCannotBeScheduledError } from "../../generated/platform/PlatformMemberCompanyConnectedPartnerCannotBeScheduledError"
import type { PlatformMemberCompanyConnectedPartnerTypeUnchangeableError } from "../../generated/platform/PlatformMemberCompanyConnectedPartnerTypeUnchangeableError"
import type { PlatformMemberCompanyConnectedPartnersCannotBeScheduledError } from "../../generated/platform/PlatformMemberCompanyConnectedPartnersCannotBeScheduledError"
import type { PlatformNotEnabledError } from "../../generated/platform/PlatformNotEnabledError"
import type { PlatformPartner } from "../../generated/platform/PlatformPartner"
import type { PlatformPartnerFilterInput } from "../../generated/platform/PlatformPartnerFilterInput"
import type { PlatformPartnerFilterOptions } from "../../generated/platform/PlatformPartnerFilterOptions"
import type { PlatformPartnerNotFoundError } from "../../generated/platform/PlatformPartnerNotFoundError"
import type { PlatformPartnerScheduleAlreadyExistsError } from "../../generated/platform/PlatformPartnerScheduleAlreadyExistsError"
import type { PlatformPartnerSchedulesAlreadyExistError } from "../../generated/platform/PlatformPartnerSchedulesAlreadyExistError"
import type { PlatformRoundType } from "../../generated/platform/PlatformRoundType"
import type { PlatformSetting } from "../../generated/platform/PlatformSetting"
import type { PlatformUserDefinedPropertyNotFoundError } from "../../generated/platform/PlatformUserDefinedPropertyNotFoundError"
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
import type { UnauthorizedError } from "../../generated/common/UnauthorizedError"
import type { UpdatePlatformAdditionalFeePolicyBody } from "../../generated/platform/UpdatePlatformAdditionalFeePolicyBody"
import type { UpdatePlatformBodySettlementFormula } from "../../generated/platform/UpdatePlatformBodySettlementFormula"
import type { UpdatePlatformBodySettlementRule } from "../../generated/platform/UpdatePlatformBodySettlementRule"
import type { UpdatePlatformContractBody } from "../../generated/platform/UpdatePlatformContractBody"
import type { UpdatePlatformDiscountSharePolicyBody } from "../../generated/platform/UpdatePlatformDiscountSharePolicyBody"
import type { UpdatePlatformPartnerBody } from "../../generated/platform/UpdatePlatformPartnerBody"
import type { UpdatePlatformResponse } from "../../generated/platform/UpdatePlatformResponse"
import type { UpdatePlatformSettingResponse } from "../../generated/platform/UpdatePlatformSettingResponse"
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
				throw new GetPlatformError(await response.json())
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
				throw new UpdatePlatformError(await response.json())
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
				throw new GetPlatformDiscountSharePolicyFilterOptionsError(await response.json())
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
				throw new GetPlatformDiscountSharePolicyScheduleError(await response.json())
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
				throw new RescheduleDiscountSharePolicyError(await response.json())
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
				throw new ScheduleDiscountSharePolicyError(await response.json())
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
				throw new CancelPlatformDiscountSharePolicyScheduleError(await response.json())
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
				throw new GetPlatformAdditionalFeePolicyScheduleError(await response.json())
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
				throw new RescheduleAdditionalFeePolicyError(await response.json())
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
				throw new ScheduleAdditionalFeePolicyError(await response.json())
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
				throw new CancelPlatformAdditionalFeePolicyScheduleError(await response.json())
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
				throw new GetPlatformPartnerFilterOptionsError(await response.json())
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
				throw new GetPlatformPartnerScheduleError(await response.json())
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
				throw new ReschedulePartnerError(await response.json())
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
				throw new SchedulePartnerError(await response.json())
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
				throw new CancelPlatformPartnerScheduleError(await response.json())
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
				throw new SchedulePlatformPartnersError(await response.json())
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
				throw new GetPlatformContractScheduleError(await response.json())
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
				throw new RescheduleContractError(await response.json())
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
				throw new ScheduleContractError(await response.json())
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
				throw new CancelPlatformContractScheduleError(await response.json())
			}
			return response.json()
		},
		getPlatformSetting: async (
			options?: {
			}
		): Promise<PlatformSetting> => {
			const response = await fetch(
				new URL("/platform/setting", baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformSettingError(await response.json())
			}
			return response.json()
		},
		updatePlatformSetting: async (
			options?: {
				defaultWithdrawalMemo?: string,
				defaultDepositMemo?: string,
			}
		): Promise<UpdatePlatformSettingResponse> => {
			const defaultWithdrawalMemo = options?.defaultWithdrawalMemo
			const defaultDepositMemo = options?.defaultDepositMemo
			const requestBody = JSON.stringify({
				defaultWithdrawalMemo,
				defaultDepositMemo,
			})
			const response = await fetch(
				new URL("/platform/setting", baseUrl),
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
				throw new UpdatePlatformSettingError(await response.json())
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
		company: CompanyClient(init),
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
	/**
	 * 플랫폼 설정 조회
	 *
	 * 설정 정보를 조회합니다.
	 *
	 * @throws {@link GetPlatformSettingError}
	 */
	getPlatformSetting: (
		options?: {
		}
	) => Promise<PlatformSetting>
	/**
	 * 플랫폼 설정 업데이트
	 *
	 * 설정 정보를 업데이트합니다.
	 *
	 * @throws {@link UpdatePlatformSettingError}
	 */
	updatePlatformSetting: (
		options?: {
			/** 기본 보내는 이 통장 메모 */
			defaultWithdrawalMemo?: string,
			/** 기본 받는 이 통장 메모 */
			defaultDepositMemo?: string,
		}
	) => Promise<UpdatePlatformSettingResponse>
	policy: PolicyClient
	partner: PartnerClient
	transfer: TransferClient
	partnerSettlement: PartnerSettlementClient
	payout: PayoutClient
	bulkPayout: BulkPayoutClient
	account: AccountClient
	company: CompanyClient
	accountTransfer: AccountTransferClient
}
export class GetPlatformError extends PlatformError {
	declare readonly data: InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformError.prototype)
		this.name = "GetPlatformError"
	}
}
export class UpdatePlatformError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformInvalidSettlementFormulaError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformInvalidSettlementFormulaError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, UpdatePlatformError.prototype)
		this.name = "UpdatePlatformError"
	}
}
export class GetPlatformDiscountSharePolicyFilterOptionsError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformDiscountSharePolicyFilterOptionsError.prototype)
		this.name = "GetPlatformDiscountSharePolicyFilterOptionsError"
	}
}
export class GetPlatformDiscountSharePolicyScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformDiscountSharePolicyScheduleError.prototype)
		this.name = "GetPlatformDiscountSharePolicyScheduleError"
	}
}
export class RescheduleDiscountSharePolicyError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, RescheduleDiscountSharePolicyError.prototype)
		this.name = "RescheduleDiscountSharePolicyError"
	}
}
export class ScheduleDiscountSharePolicyError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformArchivedDiscountSharePolicyError | PlatformDiscountSharePolicyNotFoundError | PlatformDiscountSharePolicyScheduleAlreadyExistsError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformArchivedDiscountSharePolicyError | PlatformDiscountSharePolicyNotFoundError | PlatformDiscountSharePolicyScheduleAlreadyExistsError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ScheduleDiscountSharePolicyError.prototype)
		this.name = "ScheduleDiscountSharePolicyError"
	}
}
export class CancelPlatformDiscountSharePolicyScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CancelPlatformDiscountSharePolicyScheduleError.prototype)
		this.name = "CancelPlatformDiscountSharePolicyScheduleError"
	}
}
export class GetPlatformAdditionalFeePolicyScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformAdditionalFeePolicyScheduleError.prototype)
		this.name = "GetPlatformAdditionalFeePolicyScheduleError"
	}
}
export class RescheduleAdditionalFeePolicyError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, RescheduleAdditionalFeePolicyError.prototype)
		this.name = "RescheduleAdditionalFeePolicyError"
	}
}
export class ScheduleAdditionalFeePolicyError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformAdditionalFeePolicyScheduleAlreadyExistsError | PlatformArchivedAdditionalFeePolicyError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformAdditionalFeePolicyScheduleAlreadyExistsError | PlatformArchivedAdditionalFeePolicyError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ScheduleAdditionalFeePolicyError.prototype)
		this.name = "ScheduleAdditionalFeePolicyError"
	}
}
export class CancelPlatformAdditionalFeePolicyScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CancelPlatformAdditionalFeePolicyScheduleError.prototype)
		this.name = "CancelPlatformAdditionalFeePolicyScheduleError"
	}
}
export class GetPlatformPartnerFilterOptionsError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformPartnerFilterOptionsError.prototype)
		this.name = "GetPlatformPartnerFilterOptionsError"
	}
}
export class GetPlatformPartnerScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformPartnerScheduleError.prototype)
		this.name = "GetPlatformPartnerScheduleError"
	}
}
export class ReschedulePartnerError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformMemberCompanyConnectedPartnerCannotBeScheduledError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformMemberCompanyConnectedPartnerCannotBeScheduledError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ReschedulePartnerError.prototype)
		this.name = "ReschedulePartnerError"
	}
}
export class SchedulePartnerError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAccountVerificationAlreadyUsedError | PlatformAccountVerificationFailedError | PlatformAccountVerificationNotFoundError | PlatformArchivedPartnerError | PlatformCompanyVerificationAlreadyUsedError | PlatformContractNotFoundError | PlatformInsufficientDataToChangePartnerTypeError | PlatformMemberCompanyConnectedPartnerBrnUnchangeableError | PlatformMemberCompanyConnectedPartnerCannotBeScheduledError | PlatformMemberCompanyConnectedPartnerTypeUnchangeableError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformPartnerScheduleAlreadyExistsError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAccountVerificationAlreadyUsedError | PlatformAccountVerificationFailedError | PlatformAccountVerificationNotFoundError | PlatformArchivedPartnerError | PlatformCompanyVerificationAlreadyUsedError | PlatformContractNotFoundError | PlatformInsufficientDataToChangePartnerTypeError | PlatformMemberCompanyConnectedPartnerBrnUnchangeableError | PlatformMemberCompanyConnectedPartnerCannotBeScheduledError | PlatformMemberCompanyConnectedPartnerTypeUnchangeableError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformPartnerScheduleAlreadyExistsError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, SchedulePartnerError.prototype)
		this.name = "SchedulePartnerError"
	}
}
export class CancelPlatformPartnerScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CancelPlatformPartnerScheduleError.prototype)
		this.name = "CancelPlatformPartnerScheduleError"
	}
}
export class SchedulePlatformPartnersError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformArchivedPartnersCannotBeScheduledError | PlatformContractNotFoundError | PlatformMemberCompanyConnectedPartnersCannotBeScheduledError | PlatformNotEnabledError | PlatformPartnerSchedulesAlreadyExistError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformArchivedPartnersCannotBeScheduledError | PlatformContractNotFoundError | PlatformMemberCompanyConnectedPartnersCannotBeScheduledError | PlatformNotEnabledError | PlatformPartnerSchedulesAlreadyExistError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, SchedulePlatformPartnersError.prototype)
		this.name = "SchedulePlatformPartnersError"
	}
}
export class GetPlatformContractScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformContractScheduleError.prototype)
		this.name = "GetPlatformContractScheduleError"
	}
}
export class RescheduleContractError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, RescheduleContractError.prototype)
		this.name = "RescheduleContractError"
	}
}
export class ScheduleContractError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformArchivedContractError | PlatformContractNotFoundError | PlatformContractScheduleAlreadyExistsError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformArchivedContractError | PlatformContractNotFoundError | PlatformContractScheduleAlreadyExistsError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ScheduleContractError.prototype)
		this.name = "ScheduleContractError"
	}
}
export class CancelPlatformContractScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CancelPlatformContractScheduleError.prototype)
		this.name = "CancelPlatformContractScheduleError"
	}
}
export class GetPlatformSettingError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformSettingError.prototype)
		this.name = "GetPlatformSettingError"
	}
}
export class UpdatePlatformSettingError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, UpdatePlatformSettingError.prototype)
		this.name = "UpdatePlatformSettingError"
	}
}
