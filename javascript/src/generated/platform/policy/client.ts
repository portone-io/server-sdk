import { PolicyError } from "./PolicyError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { ArchivePlatformAdditionalFeePolicyResponse } from "../../../generated/platform/policy/ArchivePlatformAdditionalFeePolicyResponse"
import type { ArchivePlatformContractResponse } from "../../../generated/platform/policy/ArchivePlatformContractResponse"
import type { ArchivePlatformDiscountSharePolicyResponse } from "../../../generated/platform/policy/ArchivePlatformDiscountSharePolicyResponse"
import type { CreatePlatformAdditionalFeePolicyResponse } from "../../../generated/platform/policy/CreatePlatformAdditionalFeePolicyResponse"
import type { CreatePlatformContractResponse } from "../../../generated/platform/policy/CreatePlatformContractResponse"
import type { CreatePlatformDiscountSharePolicyResponse } from "../../../generated/platform/policy/CreatePlatformDiscountSharePolicyResponse"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetPlatformAdditionalFeePoliciesResponse } from "../../../generated/platform/policy/GetPlatformAdditionalFeePoliciesResponse"
import type { GetPlatformContractsResponse } from "../../../generated/platform/policy/GetPlatformContractsResponse"
import type { GetPlatformDiscountSharePoliciesResponse } from "../../../generated/platform/policy/GetPlatformDiscountSharePoliciesResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformAdditionalFeePolicy } from "../../../generated/platform/PlatformAdditionalFeePolicy"
import type { PlatformAdditionalFeePolicyAlreadyExistsError } from "../../../generated/platform/policy/PlatformAdditionalFeePolicyAlreadyExistsError"
import type { PlatformAdditionalFeePolicyFilterInput } from "../../../generated/platform/policy/PlatformAdditionalFeePolicyFilterInput"
import type { PlatformAdditionalFeePolicyNotFoundError } from "../../../generated/platform/PlatformAdditionalFeePolicyNotFoundError"
import type { PlatformArchivedAdditionalFeePolicyError } from "../../../generated/platform/PlatformArchivedAdditionalFeePolicyError"
import type { PlatformArchivedContractError } from "../../../generated/platform/PlatformArchivedContractError"
import type { PlatformArchivedDiscountSharePolicyError } from "../../../generated/platform/PlatformArchivedDiscountSharePolicyError"
import type { PlatformCannotArchiveScheduledAdditionalFeePolicyError } from "../../../generated/platform/policy/PlatformCannotArchiveScheduledAdditionalFeePolicyError"
import type { PlatformCannotArchiveScheduledContractError } from "../../../generated/platform/policy/PlatformCannotArchiveScheduledContractError"
import type { PlatformCannotArchiveScheduledDiscountSharePolicyError } from "../../../generated/platform/policy/PlatformCannotArchiveScheduledDiscountSharePolicyError"
import type { PlatformContract } from "../../../generated/platform/PlatformContract"
import type { PlatformContractAlreadyExistsError } from "../../../generated/platform/policy/PlatformContractAlreadyExistsError"
import type { PlatformContractFilterInput } from "../../../generated/platform/policy/PlatformContractFilterInput"
import type { PlatformContractNotFoundError } from "../../../generated/platform/PlatformContractNotFoundError"
import type { PlatformDiscountSharePolicy } from "../../../generated/platform/PlatformDiscountSharePolicy"
import type { PlatformDiscountSharePolicyAlreadyExistsError } from "../../../generated/platform/policy/PlatformDiscountSharePolicyAlreadyExistsError"
import type { PlatformDiscountSharePolicyFilterInput } from "../../../generated/platform/policy/PlatformDiscountSharePolicyFilterInput"
import type { PlatformDiscountSharePolicyNotFoundError } from "../../../generated/platform/PlatformDiscountSharePolicyNotFoundError"
import type { PlatformFeeInput } from "../../../generated/platform/PlatformFeeInput"
import type { PlatformNotEnabledError } from "../../../generated/platform/PlatformNotEnabledError"
import type { PlatformPayer } from "../../../generated/platform/PlatformPayer"
import type { PlatformSettlementCycleInput } from "../../../generated/platform/PlatformSettlementCycleInput"
import type { RecoverPlatformAdditionalFeePolicyResponse } from "../../../generated/platform/policy/RecoverPlatformAdditionalFeePolicyResponse"
import type { RecoverPlatformContractResponse } from "../../../generated/platform/policy/RecoverPlatformContractResponse"
import type { RecoverPlatformDiscountSharePolicyResponse } from "../../../generated/platform/policy/RecoverPlatformDiscountSharePolicyResponse"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
import type { UpdatePlatformAdditionalFeePolicyResponse } from "../../../generated/platform/policy/UpdatePlatformAdditionalFeePolicyResponse"
import type { UpdatePlatformContractResponse } from "../../../generated/platform/policy/UpdatePlatformContractResponse"
import type { UpdatePlatformDiscountSharePolicyResponse } from "../../../generated/platform/policy/UpdatePlatformDiscountSharePolicyResponse"
export function PolicyClient(init: PortOneClientInit): PolicyClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPlatformDiscountSharePolicies: async (
			options?: {
				page?: PageInput,
				filter?: PlatformDiscountSharePolicyFilterInput,
			}
		): Promise<GetPlatformDiscountSharePoliciesResponse> => {
			const page = options?.page
			const filter = options?.filter
			const requestBody = JSON.stringify({
				page,
				filter,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/discount-share-policies?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformDiscountSharePoliciesError(await response.json())
			}
			return response.json()
		},
		createPlatformDiscountSharePolicy: async (
			options: {
				id?: string,
				name: string,
				partnerShareRate: number,
				memo?: string,
			}
		): Promise<CreatePlatformDiscountSharePolicyResponse> => {
			const {
				id,
				name,
				partnerShareRate,
				memo,
			} = options
			const requestBody = JSON.stringify({
				id,
				name,
				partnerShareRate,
				memo,
			})
			const response = await fetch(
				new URL("/platform/discount-share-policies", baseUrl),
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
				throw new CreatePlatformDiscountSharePolicyError(await response.json())
			}
			return response.json()
		},
		getPlatformDiscountSharePolicy: async (
			options: {
				id: string,
			}
		): Promise<PlatformDiscountSharePolicy> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformDiscountSharePolicyError(await response.json())
			}
			return response.json()
		},
		updatePlatformDiscountSharePolicy: async (
			options: {
				id: string,
				name?: string,
				partnerShareRate?: number,
				memo?: string,
			}
		): Promise<UpdatePlatformDiscountSharePolicyResponse> => {
			const {
				id,
				name,
				partnerShareRate,
				memo,
			} = options
			const requestBody = JSON.stringify({
				name,
				partnerShareRate,
				memo,
			})
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}`, baseUrl),
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
				throw new UpdatePlatformDiscountSharePolicyError(await response.json())
			}
			return response.json()
		},
		archivePlatformDiscountSharePolicy: async (
			options: {
				id: string,
			}
		): Promise<ArchivePlatformDiscountSharePolicyResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}/archive`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new ArchivePlatformDiscountSharePolicyError(await response.json())
			}
			return response.json()
		},
		recoverPlatformDiscountSharePolicy: async (
			options: {
				id: string,
			}
		): Promise<RecoverPlatformDiscountSharePolicyResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}/recover`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new RecoverPlatformDiscountSharePolicyError(await response.json())
			}
			return response.json()
		},
		getPlatformAdditionalFeePolicies: async (
			options?: {
				page?: PageInput,
				filter?: PlatformAdditionalFeePolicyFilterInput,
			}
		): Promise<GetPlatformAdditionalFeePoliciesResponse> => {
			const page = options?.page
			const filter = options?.filter
			const requestBody = JSON.stringify({
				page,
				filter,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/additional-fee-policies?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformAdditionalFeePoliciesError(await response.json())
			}
			return response.json()
		},
		createPlatformAdditionalFeePolicy: async (
			options: {
				id?: string,
				name: string,
				fee: PlatformFeeInput,
				memo?: string,
				vatPayer: PlatformPayer,
			}
		): Promise<CreatePlatformAdditionalFeePolicyResponse> => {
			const {
				id,
				name,
				fee,
				memo,
				vatPayer,
			} = options
			const requestBody = JSON.stringify({
				id,
				name,
				fee,
				memo,
				vatPayer,
			})
			const response = await fetch(
				new URL("/platform/additional-fee-policies", baseUrl),
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
				throw new CreatePlatformAdditionalFeePolicyError(await response.json())
			}
			return response.json()
		},
		getPlatformAdditionalFeePolicy: async (
			options: {
				id: string,
			}
		): Promise<PlatformAdditionalFeePolicy> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformAdditionalFeePolicyError(await response.json())
			}
			return response.json()
		},
		updatePlatformAdditionalFeePolicy: async (
			options: {
				id: string,
				fee?: PlatformFeeInput,
				name?: string,
				memo?: string,
				vatPayer?: PlatformPayer,
			}
		): Promise<UpdatePlatformAdditionalFeePolicyResponse> => {
			const {
				id,
				fee,
				name,
				memo,
				vatPayer,
			} = options
			const requestBody = JSON.stringify({
				fee,
				name,
				memo,
				vatPayer,
			})
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}`, baseUrl),
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
				throw new UpdatePlatformAdditionalFeePolicyError(await response.json())
			}
			return response.json()
		},
		archivePlatformAdditionalFeePolicy: async (
			options: {
				id: string,
			}
		): Promise<ArchivePlatformAdditionalFeePolicyResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}/archive`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new ArchivePlatformAdditionalFeePolicyError(await response.json())
			}
			return response.json()
		},
		recoverPlatformAdditionalFeePolicy: async (
			options: {
				id: string,
			}
		): Promise<RecoverPlatformAdditionalFeePolicyResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}/recover`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new RecoverPlatformAdditionalFeePolicyError(await response.json())
			}
			return response.json()
		},
		getPlatformContracts: async (
			options?: {
				page?: PageInput,
				filter?: PlatformContractFilterInput,
			}
		): Promise<GetPlatformContractsResponse> => {
			const page = options?.page
			const filter = options?.filter
			const requestBody = JSON.stringify({
				page,
				filter,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/contracts?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformContractsError(await response.json())
			}
			return response.json()
		},
		createPlatformContract: async (
			options: {
				id?: string,
				name: string,
				memo?: string,
				platformFee: PlatformFeeInput,
				settlementCycle: PlatformSettlementCycleInput,
				platformFeeVatPayer: PlatformPayer,
				subtractPaymentVatAmount: boolean,
			}
		): Promise<CreatePlatformContractResponse> => {
			const {
				id,
				name,
				memo,
				platformFee,
				settlementCycle,
				platformFeeVatPayer,
				subtractPaymentVatAmount,
			} = options
			const requestBody = JSON.stringify({
				id,
				name,
				memo,
				platformFee,
				settlementCycle,
				platformFeeVatPayer,
				subtractPaymentVatAmount,
			})
			const response = await fetch(
				new URL("/platform/contracts", baseUrl),
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
				throw new CreatePlatformContractError(await response.json())
			}
			return response.json()
		},
		getPlatformContract: async (
			options: {
				id: string,
			}
		): Promise<PlatformContract> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformContractError(await response.json())
			}
			return response.json()
		},
		updatePlatformContract: async (
			options: {
				id: string,
				name?: string,
				memo?: string,
				platformFee?: PlatformFeeInput,
				settlementCycle?: PlatformSettlementCycleInput,
				platformFeeVatPayer?: PlatformPayer,
				subtractPaymentVatAmount?: boolean,
			}
		): Promise<UpdatePlatformContractResponse> => {
			const {
				id,
				name,
				memo,
				platformFee,
				settlementCycle,
				platformFeeVatPayer,
				subtractPaymentVatAmount,
			} = options
			const requestBody = JSON.stringify({
				name,
				memo,
				platformFee,
				settlementCycle,
				platformFeeVatPayer,
				subtractPaymentVatAmount,
			})
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}`, baseUrl),
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
				throw new UpdatePlatformContractError(await response.json())
			}
			return response.json()
		},
		archivePlatformContract: async (
			options: {
				id: string,
			}
		): Promise<ArchivePlatformContractResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}/archive`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new ArchivePlatformContractError(await response.json())
			}
			return response.json()
		},
		recoverPlatformContract: async (
			options: {
				id: string,
			}
		): Promise<RecoverPlatformContractResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}/recover`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new RecoverPlatformContractError(await response.json())
			}
			return response.json()
		},
	}
}
export type PolicyClient = {
	/**
	 * 할인 분담 정책 다건 조회
	 *
	 * 여러 할인 분담을 조회합니다.
	 *
	 * @throws {@link GetPlatformDiscountSharePoliciesError}
	 */
	getPlatformDiscountSharePolicies: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: PageInput,
			/** 조회할 할인 분담 정책 조건 필터 */
			filter?: PlatformDiscountSharePolicyFilterInput,
		}
	) => Promise<GetPlatformDiscountSharePoliciesResponse>
	/**
	 * 할인 분담 정책 생성
	 *
	 * 새로운 할인 분담을 생성합니다.
	 *
	 * @throws {@link CreatePlatformDiscountSharePolicyError}
	 */
	createPlatformDiscountSharePolicy: (
		options: {
			/**
			 * 할인 분담에 부여할 고유 아이디
			 *
			 * 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
			 */
			id?: string,
			/** 할인 분담에 부여할 이름 */
			name: string,
			/**
			 * 파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
			 * (int32)
			 */
			partnerShareRate: number,
			/** 해당 할인 분담에 대한 메모 ex) 파트너 브랜드 쿠폰 */
			memo?: string,
		}
	) => Promise<CreatePlatformDiscountSharePolicyResponse>
	/**
	 * 할인 분담 정책 조회
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 조회합니다.
	 *
	 * @throws {@link GetPlatformDiscountSharePolicyError}
	 */
	getPlatformDiscountSharePolicy: (
		options: {
			/** 조회할 할인 분담 정책 아이디 */
			id: string,
		}
	) => Promise<PlatformDiscountSharePolicy>
	/**
	 * 할인 분담 정책 수정
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 업데이트합니다.
	 *
	 * @throws {@link UpdatePlatformDiscountSharePolicyError}
	 */
	updatePlatformDiscountSharePolicy: (
		options: {
			/** 업데이트할 할인 분담 정책 아이디 */
			id: string,
			/** 할인 분담 정책 이름 */
			name?: string,
			/**
			 * 할인 분담율
			 *
			 * 파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
			 * (int32)
			 */
			partnerShareRate?: number,
			/** 해당 할인 분담에 대한 메모 */
			memo?: string,
		}
	) => Promise<UpdatePlatformDiscountSharePolicyResponse>
	/**
	 * 할인 분담 정책 보관
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 보관합니다.
	 *
	 * @throws {@link ArchivePlatformDiscountSharePolicyError}
	 */
	archivePlatformDiscountSharePolicy: (
		options: {
			/** 할인 분담 아이디 */
			id: string,
		}
	) => Promise<ArchivePlatformDiscountSharePolicyResponse>
	/**
	 * 할인 분담 정책 복원
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 복원합니다.
	 *
	 * @throws {@link RecoverPlatformDiscountSharePolicyError}
	 */
	recoverPlatformDiscountSharePolicy: (
		options: {
			/** 할인 분담 아이디 */
			id: string,
		}
	) => Promise<RecoverPlatformDiscountSharePolicyResponse>
	/**
	 * 추가 수수료 정책 다건 조회
	 *
	 * 여러 추가 수수료 정책을 조회합니다.
	 *
	 * @throws {@link GetPlatformAdditionalFeePoliciesError}
	 */
	getPlatformAdditionalFeePolicies: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: PageInput,
			/** 조회할 추가 수수료 정책 조건 필터 */
			filter?: PlatformAdditionalFeePolicyFilterInput,
		}
	) => Promise<GetPlatformAdditionalFeePoliciesResponse>
	/**
	 * 추가 수수료 정책 생성
	 *
	 * 새로운 추가 수수료 정책을 생성합니다.
	 *
	 * @throws {@link CreatePlatformAdditionalFeePolicyError}
	 */
	createPlatformAdditionalFeePolicy: (
		options: {
			/**
			 * 생성할 추가 수수료 정책 아이디
			 *
			 * 명시하지 않으면 id 가 임의로 생성됩니다.
			 */
			id?: string,
			/** 이름 */
			name: string,
			/** 수수료 정보 */
			fee: PlatformFeeInput,
			/** 메모 */
			memo?: string,
			/** 부가세 부담 주체 */
			vatPayer: PlatformPayer,
		}
	) => Promise<CreatePlatformAdditionalFeePolicyResponse>
	/**
	 * 추가 수수료 정책 조회
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 조회합니다.
	 *
	 * @throws {@link GetPlatformAdditionalFeePolicyError}
	 */
	getPlatformAdditionalFeePolicy: (
		options: {
			/** 조회할 추가 수수료 정책 아이디 */
			id: string,
		}
	) => Promise<PlatformAdditionalFeePolicy>
	/**
	 * 추가 수수료 정책 수정
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 업데이트합니다.
	 *
	 * @throws {@link UpdatePlatformAdditionalFeePolicyError}
	 */
	updatePlatformAdditionalFeePolicy: (
		options: {
			/** 업데이트할 추가 수수료 정책 아이디 */
			id: string,
			/** 책정 수수료 */
			fee?: PlatformFeeInput,
			/** 추가 수수료 정책 이름 */
			name?: string,
			/** 해당 추가 수수료 정책에 대한 메모 */
			memo?: string,
			/** 부가세를 부담할 주체 */
			vatPayer?: PlatformPayer,
		}
	) => Promise<UpdatePlatformAdditionalFeePolicyResponse>
	/**
	 * 추가 수수료 정책 보관
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 보관합니다.
	 *
	 * @throws {@link ArchivePlatformAdditionalFeePolicyError}
	 */
	archivePlatformAdditionalFeePolicy: (
		options: {
			/** 추가 수수료 정책 아이디 */
			id: string,
		}
	) => Promise<ArchivePlatformAdditionalFeePolicyResponse>
	/**
	 * 추가 수수료 정책 복원
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 복원합니다.
	 *
	 * @throws {@link RecoverPlatformAdditionalFeePolicyError}
	 */
	recoverPlatformAdditionalFeePolicy: (
		options: {
			/** 추가 수수료 정책 아이디 */
			id: string,
		}
	) => Promise<RecoverPlatformAdditionalFeePolicyResponse>
	/**
	 * 계약 다건 조회
	 *
	 * 여러 계약을 조회합니다.
	 *
	 * @throws {@link GetPlatformContractsError}
	 */
	getPlatformContracts: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: PageInput,
			/** 조회할 계약 조건 필터 */
			filter?: PlatformContractFilterInput,
		}
	) => Promise<GetPlatformContractsResponse>
	/**
	 * 계약 생성
	 *
	 * 새로운 계약을 생성합니다.
	 *
	 * @throws {@link CreatePlatformContractError}
	 */
	createPlatformContract: (
		options: {
			/**
			 * 계약에 부여할 고유 아이디
			 *
			 * 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
			 */
			id?: string,
			/** 계약 이름 */
			name: string,
			/** 계약 내부 표기를 위한 메모 */
			memo?: string,
			/** 중개수수료 */
			platformFee: PlatformFeeInput,
			/** 정산 주기 */
			settlementCycle: PlatformSettlementCycleInput,
			/** 중개수수료에 대한 부가세 부담 주체 */
			platformFeeVatPayer: PlatformPayer,
			/** 정산 시 결제금액 부가세 감액 여부 */
			subtractPaymentVatAmount: boolean,
		}
	) => Promise<CreatePlatformContractResponse>
	/**
	 * 계약 조회
	 *
	 * 주어진 아이디에 대응되는 계약을 조회합니다.
	 *
	 * @throws {@link GetPlatformContractError}
	 */
	getPlatformContract: (
		options: {
			/** 조회할 계약 아이디 */
			id: string,
		}
	) => Promise<PlatformContract>
	/**
	 * 계약 수정
	 *
	 * 주어진 아이디에 대응되는 계약을 업데이트합니다.
	 *
	 * @throws {@link UpdatePlatformContractError}
	 */
	updatePlatformContract: (
		options: {
			/** 업데이트할 계약 아이디 */
			id: string,
			/** 계약 이름 */
			name?: string,
			/** 계약 내부 표기를 위한 메모 */
			memo?: string,
			/** 중개수수료 */
			platformFee?: PlatformFeeInput,
			/** 정산 주기 */
			settlementCycle?: PlatformSettlementCycleInput,
			/** 중개수수료에 대한 부가세 부담 주체 */
			platformFeeVatPayer?: PlatformPayer,
			/** 정산 시 결제금액 부가세 감액 여부 */
			subtractPaymentVatAmount?: boolean,
		}
	) => Promise<UpdatePlatformContractResponse>
	/**
	 * 계약 보관
	 *
	 * 주어진 아이디에 대응되는 계약을 보관합니다.
	 *
	 * @throws {@link ArchivePlatformContractError}
	 */
	archivePlatformContract: (
		options: {
			/** 계약 아이디 */
			id: string,
		}
	) => Promise<ArchivePlatformContractResponse>
	/**
	 * 계약 복원
	 *
	 * 주어진 아이디에 대응되는 계약을 복원합니다.
	 *
	 * @throws {@link RecoverPlatformContractError}
	 */
	recoverPlatformContract: (
		options: {
			/** 계약 아이디 */
			id: string,
		}
	) => Promise<RecoverPlatformContractResponse>
}
export class GetPlatformDiscountSharePoliciesError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformDiscountSharePoliciesError.prototype)
		this.name = "GetPlatformDiscountSharePoliciesError"
	}
}
export class CreatePlatformDiscountSharePolicyError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyAlreadyExistsError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyAlreadyExistsError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CreatePlatformDiscountSharePolicyError.prototype)
		this.name = "CreatePlatformDiscountSharePolicyError"
	}
}
export class GetPlatformDiscountSharePolicyError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformDiscountSharePolicyError.prototype)
		this.name = "GetPlatformDiscountSharePolicyError"
	}
}
export class UpdatePlatformDiscountSharePolicyError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformArchivedDiscountSharePolicyError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformArchivedDiscountSharePolicyError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, UpdatePlatformDiscountSharePolicyError.prototype)
		this.name = "UpdatePlatformDiscountSharePolicyError"
	}
}
export class ArchivePlatformDiscountSharePolicyError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformCannotArchiveScheduledDiscountSharePolicyError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformCannotArchiveScheduledDiscountSharePolicyError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ArchivePlatformDiscountSharePolicyError.prototype)
		this.name = "ArchivePlatformDiscountSharePolicyError"
	}
}
export class RecoverPlatformDiscountSharePolicyError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, RecoverPlatformDiscountSharePolicyError.prototype)
		this.name = "RecoverPlatformDiscountSharePolicyError"
	}
}
export class GetPlatformAdditionalFeePoliciesError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformAdditionalFeePoliciesError.prototype)
		this.name = "GetPlatformAdditionalFeePoliciesError"
	}
}
export class CreatePlatformAdditionalFeePolicyError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyAlreadyExistsError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyAlreadyExistsError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CreatePlatformAdditionalFeePolicyError.prototype)
		this.name = "CreatePlatformAdditionalFeePolicyError"
	}
}
export class GetPlatformAdditionalFeePolicyError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformAdditionalFeePolicyError.prototype)
		this.name = "GetPlatformAdditionalFeePolicyError"
	}
}
export class UpdatePlatformAdditionalFeePolicyError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformArchivedAdditionalFeePolicyError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformArchivedAdditionalFeePolicyError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, UpdatePlatformAdditionalFeePolicyError.prototype)
		this.name = "UpdatePlatformAdditionalFeePolicyError"
	}
}
export class ArchivePlatformAdditionalFeePolicyError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformCannotArchiveScheduledAdditionalFeePolicyError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformCannotArchiveScheduledAdditionalFeePolicyError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ArchivePlatformAdditionalFeePolicyError.prototype)
		this.name = "ArchivePlatformAdditionalFeePolicyError"
	}
}
export class RecoverPlatformAdditionalFeePolicyError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, RecoverPlatformAdditionalFeePolicyError.prototype)
		this.name = "RecoverPlatformAdditionalFeePolicyError"
	}
}
export class GetPlatformContractsError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformContractsError.prototype)
		this.name = "GetPlatformContractsError"
	}
}
export class CreatePlatformContractError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformContractAlreadyExistsError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformContractAlreadyExistsError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CreatePlatformContractError.prototype)
		this.name = "CreatePlatformContractError"
	}
}
export class GetPlatformContractError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformContractError.prototype)
		this.name = "GetPlatformContractError"
	}
}
export class UpdatePlatformContractError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformArchivedContractError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformArchivedContractError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, UpdatePlatformContractError.prototype)
		this.name = "UpdatePlatformContractError"
	}
}
export class ArchivePlatformContractError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformCannotArchiveScheduledContractError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformCannotArchiveScheduledContractError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ArchivePlatformContractError.prototype)
		this.name = "ArchivePlatformContractError"
	}
}
export class RecoverPlatformContractError extends PolicyError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, RecoverPlatformContractError.prototype)
		this.name = "RecoverPlatformContractError"
	}
}
