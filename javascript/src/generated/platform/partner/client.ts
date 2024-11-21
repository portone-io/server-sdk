import * as Errors from "../../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { ArchivePlatformPartnerResponse } from "../../../generated/platform/partner/ArchivePlatformPartnerResponse"
import type { CreatePlatformPartnerBody } from "../../../generated/platform/partner/CreatePlatformPartnerBody"
import type { CreatePlatformPartnerBodyAccount } from "../../../generated/platform/partner/CreatePlatformPartnerBodyAccount"
import type { CreatePlatformPartnerBodyContact } from "../../../generated/platform/partner/CreatePlatformPartnerBodyContact"
import type { CreatePlatformPartnerBodyType } from "../../../generated/platform/partner/CreatePlatformPartnerBodyType"
import type { CreatePlatformPartnerResponse } from "../../../generated/platform/partner/CreatePlatformPartnerResponse"
import type { CreatePlatformPartnersResponse } from "../../../generated/platform/partner/CreatePlatformPartnersResponse"
import type { GetPlatformPartnersResponse } from "../../../generated/platform/partner/GetPlatformPartnersResponse"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformPartner } from "../../../generated/platform/PlatformPartner"
import type { PlatformPartnerFilterInput } from "../../../generated/platform/PlatformPartnerFilterInput"
import type { PlatformProperties } from "../../../generated/platform/PlatformProperties"
import type { RecoverPlatformPartnerResponse } from "../../../generated/platform/partner/RecoverPlatformPartnerResponse"
import type { UpdatePlatformPartnerBodyAccount } from "../../../generated/platform/UpdatePlatformPartnerBodyAccount"
import type { UpdatePlatformPartnerBodyContact } from "../../../generated/platform/UpdatePlatformPartnerBodyContact"
import type { UpdatePlatformPartnerBodyType } from "../../../generated/platform/UpdatePlatformPartnerBodyType"
import type { UpdatePlatformPartnerResponse } from "../../../generated/platform/partner/UpdatePlatformPartnerResponse"
import type { ArchivePlatformPartnerError as _InternalArchivePlatformPartnerError } from "../../../generated/platform/partner/ArchivePlatformPartnerError"
import type { CreatePlatformPartnerError as _InternalCreatePlatformPartnerError } from "../../../generated/platform/partner/CreatePlatformPartnerError"
import type { CreatePlatformPartnersError as _InternalCreatePlatformPartnersError } from "../../../generated/platform/partner/CreatePlatformPartnersError"
import type { GetPlatformPartnerError as _InternalGetPlatformPartnerError } from "../../../generated/platform/partner/GetPlatformPartnerError"
import type { GetPlatformPartnersError as _InternalGetPlatformPartnersError } from "../../../generated/platform/partner/GetPlatformPartnersError"
import type { RecoverPlatformPartnerError as _InternalRecoverPlatformPartnerError } from "../../../generated/platform/partner/RecoverPlatformPartnerError"
import type { UpdatePlatformPartnerError as _InternalUpdatePlatformPartnerError } from "../../../generated/platform/partner/UpdatePlatformPartnerError"
export function PartnerClient(init: PortOneClientInit): PartnerClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPlatformPartners: async (
			options?: {
				page?: PageInput,
				filter?: PlatformPartnerFilterInput,
			}
		): Promise<GetPlatformPartnersResponse> => {
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
				new URL(`/platform/partners?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformPartnersError = await response.json()
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
		createPlatformPartner: async (
			options: {
				id?: string,
				name: string,
				contact: CreatePlatformPartnerBodyContact,
				account: CreatePlatformPartnerBodyAccount,
				defaultContractId: string,
				memo?: string,
				tags: string[],
				type: CreatePlatformPartnerBodyType,
				userDefinedProperties?: PlatformProperties,
			}
		): Promise<CreatePlatformPartnerResponse> => {
			const {
				id,
				name,
				contact,
				account,
				defaultContractId,
				memo,
				tags,
				type,
				userDefinedProperties,
			} = options
			const requestBody = JSON.stringify({
				id,
				name,
				contact,
				account,
				defaultContractId,
				memo,
				tags,
				type,
				userDefinedProperties,
			})
			const response = await fetch(
				new URL("/platform/partners", baseUrl),
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
				const errorResponse: _InternalCreatePlatformPartnerError = await response.json()
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
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_CURRENCY_NOT_SUPPORTED":
					throw new Errors.PlatformCurrencyNotSupportedError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "PLATFORM_PARTNER_ID_ALREADY_EXISTS":
					throw new Errors.PlatformPartnerIdAlreadyExistsError(errorResponse)
				case "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
					throw new Errors.PlatformUserDefinedPropertyNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPlatformPartner: async (
			options: {
				id: string,
			}
		): Promise<PlatformPartner> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/partners/${encodeURIComponent(id)}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformPartnerError = await response.json()
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
		updatePlatformPartner: async (
			options: {
				id: string,
				name?: string,
				contact?: UpdatePlatformPartnerBodyContact,
				account?: UpdatePlatformPartnerBodyAccount,
				defaultContractId?: string,
				memo?: string,
				tags?: string[],
				type?: UpdatePlatformPartnerBodyType,
				userDefinedProperties?: PlatformProperties,
			}
		): Promise<UpdatePlatformPartnerResponse> => {
			const {
				id,
				name,
				contact,
				account,
				defaultContractId,
				memo,
				tags,
				type,
				userDefinedProperties,
			} = options
			const requestBody = JSON.stringify({
				name,
				contact,
				account,
				defaultContractId,
				memo,
				tags,
				type,
				userDefinedProperties,
			})
			const response = await fetch(
				new URL(`/platform/partners/${encodeURIComponent(id)}`, baseUrl),
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
				const errorResponse: _InternalUpdatePlatformPartnerError = await response.json()
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
				case "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
					throw new Errors.PlatformUserDefinedPropertyNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		createPlatformPartners: async (
			options: {
				partners: CreatePlatformPartnerBody[],
			}
		): Promise<CreatePlatformPartnersResponse> => {
			const {
				partners,
			} = options
			const requestBody = JSON.stringify({
				partners,
			})
			const response = await fetch(
				new URL("/platform/partners/batch", baseUrl),
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
				const errorResponse: _InternalCreatePlatformPartnersError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_CONTRACTS_NOT_FOUND":
					throw new Errors.PlatformContractsNotFoundError(errorResponse)
				case "PLATFORM_CURRENCY_NOT_SUPPORTED":
					throw new Errors.PlatformCurrencyNotSupportedError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "PLATFORM_PARTNER_IDS_ALREADY_EXISTS":
					throw new Errors.PlatformPartnerIdsAlreadyExistError(errorResponse)
				case "PLATFORM_PARTNER_IDS_DUPLICATED":
					throw new Errors.PlatformPartnerIdsDuplicatedError(errorResponse)
				case "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
					throw new Errors.PlatformUserDefinedPropertyNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		archivePlatformPartner: async (
			options: {
				id: string,
			}
		): Promise<ArchivePlatformPartnerResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/partners/${encodeURIComponent(id)}/archive`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalArchivePlatformPartnerError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_PARTNER":
					throw new Errors.PlatformCannotArchiveScheduledPartnerError(errorResponse)
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
		recoverPlatformPartner: async (
			options: {
				id: string,
			}
		): Promise<RecoverPlatformPartnerResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/partners/${encodeURIComponent(id)}/recover`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalRecoverPlatformPartnerError = await response.json()
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
	}
}
export type PartnerClient = {
	/**
	 * 파트너 다건 조회
	 *
	 * 여러 파트너를 조회합니다.
	 *
	 * @throws {@link GetPlatformPartnersError}
	 */
	getPlatformPartners: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: PageInput,
			/** 조회할 파트너 조건 필터 */
			filter?: PlatformPartnerFilterInput,
		}
	) => Promise<GetPlatformPartnersResponse>
	/**
	 * 파트너 생성
	 *
	 * 새로운 파트너를 생성합니다.
	 *
	 * @throws {@link CreatePlatformPartnerError}
	 */
	createPlatformPartner: (
		options: {
			/**
			 * 파트너에 부여할 고유 아이디
			 *
			 * 고객사 서버에 등록된 파트너 지칭 아이디와 동일하게 설정하는 것을 권장합니다. 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
			 */
			id?: string,
			/** 파트너 법인명 혹은 이름 */
			name: string,
			/** 파트너 담당자 연락 정보 */
			contact: CreatePlatformPartnerBodyContact,
			/**
			 * 정산 계좌
			 *
			 * 파트너의 사업자등록번호가 존재하는 경우 명시합니다. 별도로 검증하지는 않으며, 번호와 기호 모두 입력 가능합니다.
			 */
			account: CreatePlatformPartnerBodyAccount,
			/**
			 * 기본 계약 아이디
			 *
			 * 이미 존재하는 계약 아이디를 등록해야 합니다.
			 */
			defaultContractId: string,
			/**
			 * 파트너에 대한 메모
			 *
			 * 총 256자까지 입력할 수 있습니다.
			 */
			memo?: string,
			/**
			 * 파트너에 부여할 태그 리스트
			 *
			 * 최대 10개까지 입력할 수 있습니다.
			 */
			tags: string[],
			/**
			 * 파트너 유형별 추가 정보
			 *
			 * 사업자/원천징수 대상자 중 추가할 파트너의 유형에 따른 정보를 입력해야 합니다.
			 */
			type: CreatePlatformPartnerBodyType,
			/** 사용자 정의 속성 */
			userDefinedProperties?: PlatformProperties,
		}
	) => Promise<CreatePlatformPartnerResponse>
	/**
	 * 파트너 조회
	 *
	 * 파트너 객체를 조회합니다.
	 *
	 * @throws {@link GetPlatformPartnerError}
	 */
	getPlatformPartner: (
		options: {
			/** 조회하고 싶은 파트너 아이디 */
			id: string,
		}
	) => Promise<PlatformPartner>
	/**
	 * 파트너 수정
	 *
	 * 주어진 아이디에 대응되는 파트너 정보를 업데이트합니다.
	 *
	 * @throws {@link UpdatePlatformPartnerError}
	 */
	updatePlatformPartner: (
		options: {
			/** 업데이트할 파트너 아이디 */
			id: string,
			/** 파트너 법인명 혹은 이름 */
			name?: string,
			/** 파트너 담당자 연락 정보 */
			contact?: UpdatePlatformPartnerBodyContact,
			/** 정산 계좌 */
			account?: UpdatePlatformPartnerBodyAccount,
			/** 파트너에 설정된 기본 계약 아이디 */
			defaultContractId?: string,
			/** 파트너에 대한 메모 */
			memo?: string,
			/** 파트너의 태그 리스트 */
			tags?: string[],
			/** 파트너 유형별 정보 */
			type?: UpdatePlatformPartnerBodyType,
			/** 사용자 정의 속성 */
			userDefinedProperties?: PlatformProperties,
		}
	) => Promise<UpdatePlatformPartnerResponse>
	/**
	 * 파트너 다건 생성
	 *
	 * 새로운 파트너를 다건 생성합니다.
	 *
	 * @throws {@link CreatePlatformPartnersError}
	 */
	createPlatformPartners: (
		options: {
			/** 생성할 파트너 리스트 정보 */
			partners: CreatePlatformPartnerBody[],
		}
	) => Promise<CreatePlatformPartnersResponse>
	/**
	 * 파트너 복원
	 *
	 * 주어진 아이디에 대응되는 파트너를 보관합니다.
	 *
	 * @throws {@link ArchivePlatformPartnerError}
	 */
	archivePlatformPartner: (
		options: {
			/** 파트너 아이디 */
			id: string,
		}
	) => Promise<ArchivePlatformPartnerResponse>
	/**
	 * 파트너 복원
	 *
	 * 주어진 아이디에 대응되는 파트너를 복원합니다.
	 *
	 * @throws {@link RecoverPlatformPartnerError}
	 */
	recoverPlatformPartner: (
		options: {
			/** 파트너 아이디 */
			id: string,
		}
	) => Promise<RecoverPlatformPartnerResponse>
}
export type GetPlatformPartnersError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformPartnersError(error: Error): error is GetPlatformPartnersError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type CreatePlatformPartnerError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformAccountVerificationAlreadyUsedError
	| Errors.PlatformAccountVerificationFailedError
	| Errors.PlatformAccountVerificationNotFoundError
	| Errors.PlatformContractNotFoundError
	| Errors.PlatformCurrencyNotSupportedError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformPartnerIdAlreadyExistsError
	| Errors.PlatformUserDefinedPropertyNotFoundError
	| Errors.UnauthorizedError
export function isCreatePlatformPartnerError(error: Error): error is CreatePlatformPartnerError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformAccountVerificationAlreadyUsedError
		|| error instanceof Errors.PlatformAccountVerificationFailedError
		|| error instanceof Errors.PlatformAccountVerificationNotFoundError
		|| error instanceof Errors.PlatformContractNotFoundError
		|| error instanceof Errors.PlatformCurrencyNotSupportedError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformPartnerIdAlreadyExistsError
		|| error instanceof Errors.PlatformUserDefinedPropertyNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetPlatformPartnerError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformPartnerNotFoundError
	| Errors.UnauthorizedError
export function isGetPlatformPartnerError(error: Error): error is GetPlatformPartnerError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformPartnerNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type UpdatePlatformPartnerError =
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
	| Errors.PlatformUserDefinedPropertyNotFoundError
	| Errors.UnauthorizedError
export function isUpdatePlatformPartnerError(error: Error): error is UpdatePlatformPartnerError {
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
		|| error instanceof Errors.PlatformUserDefinedPropertyNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type CreatePlatformPartnersError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformContractsNotFoundError
	| Errors.PlatformCurrencyNotSupportedError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformPartnerIdsAlreadyExistError
	| Errors.PlatformPartnerIdsDuplicatedError
	| Errors.PlatformUserDefinedPropertyNotFoundError
	| Errors.UnauthorizedError
export function isCreatePlatformPartnersError(error: Error): error is CreatePlatformPartnersError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformContractsNotFoundError
		|| error instanceof Errors.PlatformCurrencyNotSupportedError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformPartnerIdsAlreadyExistError
		|| error instanceof Errors.PlatformPartnerIdsDuplicatedError
		|| error instanceof Errors.PlatformUserDefinedPropertyNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type ArchivePlatformPartnerError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformCannotArchiveScheduledPartnerError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformPartnerNotFoundError
	| Errors.UnauthorizedError
export function isArchivePlatformPartnerError(error: Error): error is ArchivePlatformPartnerError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformCannotArchiveScheduledPartnerError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformPartnerNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type RecoverPlatformPartnerError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformPartnerNotFoundError
	| Errors.UnauthorizedError
export function isRecoverPlatformPartnerError(error: Error): error is RecoverPlatformPartnerError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformPartnerNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
