import type { ArchivePlatformPartnerError } from "../..//platform/partner/ArchivePlatformPartnerError"
import type { ArchivePlatformPartnerResponse } from "../..//platform/partner/ArchivePlatformPartnerResponse"
import type { CreatePlatformPartnerBody } from "../..//platform/partner/CreatePlatformPartnerBody"
import type { CreatePlatformPartnerBodyAccount } from "../..//platform/partner/CreatePlatformPartnerBodyAccount"
import type { CreatePlatformPartnerBodyContact } from "../..//platform/partner/CreatePlatformPartnerBodyContact"
import type { CreatePlatformPartnerBodyType } from "../..//platform/partner/CreatePlatformPartnerBodyType"
import type { CreatePlatformPartnerError } from "../..//platform/partner/CreatePlatformPartnerError"
import type { CreatePlatformPartnerResponse } from "../..//platform/partner/CreatePlatformPartnerResponse"
import type { CreatePlatformPartnersError } from "../..//platform/partner/CreatePlatformPartnersError"
import type { CreatePlatformPartnersResponse } from "../..//platform/partner/CreatePlatformPartnersResponse"
import type { GetPlatformPartnerError } from "../..//platform/partner/GetPlatformPartnerError"
import type { GetPlatformPartnersError } from "../..//platform/partner/GetPlatformPartnersError"
import type { GetPlatformPartnersResponse } from "../..//platform/partner/GetPlatformPartnersResponse"
import type { PageInput } from "../..//common/PageInput"
import type { PlatformPartner } from "../..//platform/PlatformPartner"
import type { PlatformPartnerFilterInput } from "../..//platform/PlatformPartnerFilterInput"
import type { PlatformProperties } from "../..//platform/PlatformProperties"
import type { RecoverPlatformPartnerError } from "../..//platform/partner/RecoverPlatformPartnerError"
import type { RecoverPlatformPartnerResponse } from "../..//platform/partner/RecoverPlatformPartnerResponse"
import type { UpdatePlatformPartnerBodyAccount } from "../..//platform/UpdatePlatformPartnerBodyAccount"
import type { UpdatePlatformPartnerBodyContact } from "../..//platform/UpdatePlatformPartnerBodyContact"
import type { UpdatePlatformPartnerBodyType } from "../..//platform/UpdatePlatformPartnerBodyType"
import type { UpdatePlatformPartnerError } from "../..//platform/partner/UpdatePlatformPartnerError"
import type { UpdatePlatformPartnerResponse } from "../..//platform/partner/UpdatePlatformPartnerResponse"
import * as Errors from "../..//errors"
export type { ArchivePlatformPartnerResponse } from "./ArchivePlatformPartnerResponse"
export type { CreatePlatformPartnerBody } from "./CreatePlatformPartnerBody"
export type { CreatePlatformPartnerBodyAccount } from "./CreatePlatformPartnerBodyAccount"
export type { CreatePlatformPartnerBodyContact } from "./CreatePlatformPartnerBodyContact"
export type { CreatePlatformPartnerBodyType } from "./CreatePlatformPartnerBodyType"
export type { CreatePlatformPartnerBodyTypeBusiness } from "./CreatePlatformPartnerBodyTypeBusiness"
export type { CreatePlatformPartnerBodyTypeNonWhtPayer } from "./CreatePlatformPartnerBodyTypeNonWhtPayer"
export type { CreatePlatformPartnerBodyTypeWhtPayer } from "./CreatePlatformPartnerBodyTypeWhtPayer"
export type { CreatePlatformPartnerResponse } from "./CreatePlatformPartnerResponse"
export type { CreatePlatformPartnersBody } from "./CreatePlatformPartnersBody"
export type { CreatePlatformPartnersResponse } from "./CreatePlatformPartnersResponse"
export type { GetPlatformPartnersBody } from "./GetPlatformPartnersBody"
export type { GetPlatformPartnersResponse } from "./GetPlatformPartnersResponse"
export type { RecoverPlatformPartnerResponse } from "./RecoverPlatformPartnerResponse"
export type { UpdatePlatformPartnerResponse } from "./UpdatePlatformPartnerResponse"
/** @ignore */
export function PartnerClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): PartnerClient {
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
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformPartnersError = await response.json()
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
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: CreatePlatformPartnerError = await response.json()
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
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformPartnerError = await response.json()
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
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: UpdatePlatformPartnerError = await response.json()
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
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: CreatePlatformPartnersError = await response.json()
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
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: ArchivePlatformPartnerError = await response.json()
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
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: RecoverPlatformPartnerError = await response.json()
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
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAccountVerificationAlreadyUsedError} 파트너 계좌 검증 아이디를 이미 사용한 경우
	 * @throws {@link Errors.PlatformAccountVerificationFailedError} 파트너 계좌 인증이 실패한 경우
	 * @throws {@link Errors.PlatformAccountVerificationNotFoundError} 파트너 계좌 검증 아이디를 찾을 수 없는 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformCurrencyNotSupportedError} 지원 되지 않는 통화를 선택한 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerIdAlreadyExistsError} PlatformPartnerIdAlreadyExistsError
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAccountVerificationAlreadyUsedError} 파트너 계좌 검증 아이디를 이미 사용한 경우
	 * @throws {@link Errors.PlatformAccountVerificationFailedError} 파트너 계좌 인증이 실패한 경우
	 * @throws {@link Errors.PlatformAccountVerificationNotFoundError} 파트너 계좌 검증 아이디를 찾을 수 없는 경우
	 * @throws {@link Errors.PlatformArchivedPartnerError} 보관된 파트너를 업데이트하려고 하는 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformInsufficientDataToChangePartnerTypeError} 파트너 타입 수정에 필요한 데이터가 부족한 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformContractsNotFoundError} PlatformContractsNotFoundError
	 * @throws {@link Errors.PlatformCurrencyNotSupportedError} 지원 되지 않는 통화를 선택한 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerIdsAlreadyExistError} PlatformPartnerIdsAlreadyExistError
	 * @throws {@link Errors.PlatformPartnerIdsDuplicatedError} PlatformPartnerIdsDuplicatedError
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformCannotArchiveScheduledPartnerError} 예약된 업데이트가 있는 파트너를 보관하려고 하는 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	recoverPlatformPartner: (
		options: {
			/** 파트너 아이디 */
			id: string,
		}
	) => Promise<RecoverPlatformPartnerResponse>
}

