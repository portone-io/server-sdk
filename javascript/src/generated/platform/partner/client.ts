import { PartnerError } from "./PartnerError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { ArchivePlatformPartnerResponse } from "../../../generated/platform/partner/ArchivePlatformPartnerResponse"
import type { ConnectBulkPartnerMemberCompanyResponse } from "../../../generated/platform/partner/ConnectBulkPartnerMemberCompanyResponse"
import type { ConnectPartnerMemberCompanyResponse } from "../../../generated/platform/partner/ConnectPartnerMemberCompanyResponse"
import type { CreatePlatformPartnerBody } from "../../../generated/platform/partner/CreatePlatformPartnerBody"
import type { CreatePlatformPartnerBodyAccount } from "../../../generated/platform/partner/CreatePlatformPartnerBodyAccount"
import type { CreatePlatformPartnerBodyContact } from "../../../generated/platform/partner/CreatePlatformPartnerBodyContact"
import type { CreatePlatformPartnerBodyType } from "../../../generated/platform/partner/CreatePlatformPartnerBodyType"
import type { CreatePlatformPartnerResponse } from "../../../generated/platform/partner/CreatePlatformPartnerResponse"
import type { CreatePlatformPartnersResponse } from "../../../generated/platform/partner/CreatePlatformPartnersResponse"
import type { DisconnectBulkPartnerMemberCompanyResponse } from "../../../generated/platform/partner/DisconnectBulkPartnerMemberCompanyResponse"
import type { DisconnectPartnerMemberCompanyResponse } from "../../../generated/platform/partner/DisconnectPartnerMemberCompanyResponse"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetPlatformPartnersResponse } from "../../../generated/platform/partner/GetPlatformPartnersResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformAccountVerificationAlreadyUsedError } from "../../../generated/platform/PlatformAccountVerificationAlreadyUsedError"
import type { PlatformAccountVerificationFailedError } from "../../../generated/platform/PlatformAccountVerificationFailedError"
import type { PlatformAccountVerificationNotFoundError } from "../../../generated/platform/PlatformAccountVerificationNotFoundError"
import type { PlatformArchivedPartnerError } from "../../../generated/platform/PlatformArchivedPartnerError"
import type { PlatformBtxNotEnabledError } from "../../../generated/platform/partner/PlatformBtxNotEnabledError"
import type { PlatformCannotArchiveScheduledPartnerError } from "../../../generated/platform/partner/PlatformCannotArchiveScheduledPartnerError"
import type { PlatformCompanyVerificationAlreadyUsedError } from "../../../generated/platform/PlatformCompanyVerificationAlreadyUsedError"
import type { PlatformContractNotFoundError } from "../../../generated/platform/PlatformContractNotFoundError"
import type { PlatformContractsNotFoundError } from "../../../generated/platform/partner/PlatformContractsNotFoundError"
import type { PlatformCurrencyNotSupportedError } from "../../../generated/platform/PlatformCurrencyNotSupportedError"
import type { PlatformExternalApiFailedError } from "../../../generated/platform/PlatformExternalApiFailedError"
import type { PlatformInsufficientDataToChangePartnerTypeError } from "../../../generated/platform/PlatformInsufficientDataToChangePartnerTypeError"
import type { PlatformMemberCompanyConnectedPartnerBrnUnchangeableError } from "../../../generated/platform/PlatformMemberCompanyConnectedPartnerBrnUnchangeableError"
import type { PlatformMemberCompanyConnectedPartnerTypeUnchangeableError } from "../../../generated/platform/PlatformMemberCompanyConnectedPartnerTypeUnchangeableError"
import type { PlatformMemberCompanyNotConnectableStatusError } from "../../../generated/platform/partner/PlatformMemberCompanyNotConnectableStatusError"
import type { PlatformMemberCompanyNotConnectedError } from "../../../generated/platform/partner/PlatformMemberCompanyNotConnectedError"
import type { PlatformNotEnabledError } from "../../../generated/platform/PlatformNotEnabledError"
import type { PlatformOngoingTaxInvoiceExistsError } from "../../../generated/platform/partner/PlatformOngoingTaxInvoiceExistsError"
import type { PlatformPartner } from "../../../generated/platform/PlatformPartner"
import type { PlatformPartnerFilterInput } from "../../../generated/platform/PlatformPartnerFilterInput"
import type { PlatformPartnerIdAlreadyExistsError } from "../../../generated/platform/partner/PlatformPartnerIdAlreadyExistsError"
import type { PlatformPartnerIdsAlreadyExistError } from "../../../generated/platform/partner/PlatformPartnerIdsAlreadyExistError"
import type { PlatformPartnerIdsDuplicatedError } from "../../../generated/platform/partner/PlatformPartnerIdsDuplicatedError"
import type { PlatformPartnerNotFoundError } from "../../../generated/platform/PlatformPartnerNotFoundError"
import type { PlatformPartnerScheduleExistsError } from "../../../generated/platform/partner/PlatformPartnerScheduleExistsError"
import type { PlatformPartnerTaxationTypeIsSimpleError } from "../../../generated/platform/partner/PlatformPartnerTaxationTypeIsSimpleError"
import type { PlatformPartnerTypeIsNotBusinessError } from "../../../generated/platform/partner/PlatformPartnerTypeIsNotBusinessError"
import type { PlatformProperties } from "../../../generated/platform/PlatformProperties"
import type { PlatformTargetPartnerNotFoundError } from "../../../generated/platform/partner/PlatformTargetPartnerNotFoundError"
import type { PlatformUserDefinedPropertyNotFoundError } from "../../../generated/platform/PlatformUserDefinedPropertyNotFoundError"
import type { RecoverPlatformPartnerResponse } from "../../../generated/platform/partner/RecoverPlatformPartnerResponse"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
import type { UpdatePlatformPartnerBodyAccount } from "../../../generated/platform/UpdatePlatformPartnerBodyAccount"
import type { UpdatePlatformPartnerBodyContact } from "../../../generated/platform/UpdatePlatformPartnerBodyContact"
import type { UpdatePlatformPartnerBodyType } from "../../../generated/platform/UpdatePlatformPartnerBodyType"
import type { UpdatePlatformPartnerResponse } from "../../../generated/platform/partner/UpdatePlatformPartnerResponse"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
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
				throw new GetPlatformPartnersError(await response.json())
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
				throw new CreatePlatformPartnerError(await response.json())
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
				throw new CreatePlatformPartnersError(await response.json())
			}
			return response.json()
		},
		connectBulkPartnerMemberCompany: async (
			options?: {
				filter?: PlatformPartnerFilterInput,
			}
		): Promise<ConnectBulkPartnerMemberCompanyResponse> => {
			const filter = options?.filter
			const requestBody = JSON.stringify({
				filter,
			})
			const response = await fetch(
				new URL("/platform/partners/member-company-connect", baseUrl),
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
				throw new ConnectBulkPartnerMemberCompanyError(await response.json())
			}
			return response.json()
		},
		connectPartnerMemberCompany: async (
			options: {
				id: string,
			}
		): Promise<ConnectPartnerMemberCompanyResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/partners/member-company-connect/${encodeURIComponent(id)}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new ConnectPartnerMemberCompanyError(await response.json())
			}
			return response.json()
		},
		disconnectBulkPartnerMemberCompany: async (
			options?: {
				filter?: PlatformPartnerFilterInput,
			}
		): Promise<DisconnectBulkPartnerMemberCompanyResponse> => {
			const filter = options?.filter
			const requestBody = JSON.stringify({
				filter,
			})
			const response = await fetch(
				new URL("/platform/partners/member-company-disconnect", baseUrl),
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
				throw new DisconnectBulkPartnerMemberCompanyError(await response.json())
			}
			return response.json()
		},
		disconnectPartnerMemberCompany: async (
			options: {
				id: string,
			}
		): Promise<DisconnectPartnerMemberCompanyResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/partners/member-company-disconnect/${encodeURIComponent(id)}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new DisconnectPartnerMemberCompanyError(await response.json())
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
				throw new GetPlatformPartnerError(await response.json())
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
				throw new UpdatePlatformPartnerError(await response.json())
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
				throw new ArchivePlatformPartnerError(await response.json())
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
				throw new RecoverPlatformPartnerError(await response.json())
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
	 * 파트너 일괄 국세청 연동
	 *
	 * 파트너들을 일괄 국세청 연동합니다.
	 *
	 * @throws {@link ConnectBulkPartnerMemberCompanyError}
	 */
	connectBulkPartnerMemberCompany: (
		options?: {
			/** 일괄 국세청 연동할 파트너 조건 필터 */
			filter?: PlatformPartnerFilterInput,
		}
	) => Promise<ConnectBulkPartnerMemberCompanyResponse>
	/**
	 * 파트너 국세청 연동
	 *
	 * 파트너를 국세청 연동합니다.
	 *
	 * @throws {@link ConnectPartnerMemberCompanyError}
	 */
	connectPartnerMemberCompany: (
		options: {
			/** 파트너 아이디 */
			id: string,
		}
	) => Promise<ConnectPartnerMemberCompanyResponse>
	/**
	 * 파트너 일괄 국세청 연동 해제
	 *
	 * 파트너들을 일괄 국세청 연동 해제합니다.
	 *
	 * @throws {@link DisconnectBulkPartnerMemberCompanyError}
	 */
	disconnectBulkPartnerMemberCompany: (
		options?: {
			/** 일괄 국세청 연동 해제할 파트너 조건 필터 */
			filter?: PlatformPartnerFilterInput,
		}
	) => Promise<DisconnectBulkPartnerMemberCompanyResponse>
	/**
	 * 파트너 국세청 연동 해제
	 *
	 * 파트너를 국세청 연동 해제합니다.
	 *
	 * @throws {@link DisconnectPartnerMemberCompanyError}
	 */
	disconnectPartnerMemberCompany: (
		options: {
			/** 파트너 아이디 */
			id: string,
		}
	) => Promise<DisconnectPartnerMemberCompanyResponse>
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
	 * 파트너 보관
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
export class GetPlatformPartnersError extends PartnerError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformPartnersError.prototype)
		this.name = "GetPlatformPartnersError"
	}
}
export class CreatePlatformPartnerError extends PartnerError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAccountVerificationAlreadyUsedError | PlatformAccountVerificationFailedError | PlatformAccountVerificationNotFoundError | PlatformCompanyVerificationAlreadyUsedError | PlatformContractNotFoundError | PlatformCurrencyNotSupportedError | PlatformNotEnabledError | PlatformPartnerIdAlreadyExistsError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAccountVerificationAlreadyUsedError | PlatformAccountVerificationFailedError | PlatformAccountVerificationNotFoundError | PlatformCompanyVerificationAlreadyUsedError | PlatformContractNotFoundError | PlatformCurrencyNotSupportedError | PlatformNotEnabledError | PlatformPartnerIdAlreadyExistsError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CreatePlatformPartnerError.prototype)
		this.name = "CreatePlatformPartnerError"
	}
}
export class CreatePlatformPartnersError extends PartnerError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformContractsNotFoundError | PlatformCurrencyNotSupportedError | PlatformNotEnabledError | PlatformPartnerIdsAlreadyExistError | PlatformPartnerIdsDuplicatedError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformContractsNotFoundError | PlatformCurrencyNotSupportedError | PlatformNotEnabledError | PlatformPartnerIdsAlreadyExistError | PlatformPartnerIdsDuplicatedError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CreatePlatformPartnersError.prototype)
		this.name = "CreatePlatformPartnersError"
	}
}
export class ConnectBulkPartnerMemberCompanyError extends PartnerError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformBtxNotEnabledError | PlatformExternalApiFailedError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformTargetPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformBtxNotEnabledError | PlatformExternalApiFailedError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformTargetPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ConnectBulkPartnerMemberCompanyError.prototype)
		this.name = "ConnectBulkPartnerMemberCompanyError"
	}
}
export class ConnectPartnerMemberCompanyError extends PartnerError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformBtxNotEnabledError | PlatformExternalApiFailedError | PlatformMemberCompanyNotConnectableStatusError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformPartnerScheduleExistsError | PlatformPartnerTaxationTypeIsSimpleError | PlatformPartnerTypeIsNotBusinessError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformBtxNotEnabledError | PlatformExternalApiFailedError | PlatformMemberCompanyNotConnectableStatusError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformPartnerScheduleExistsError | PlatformPartnerTaxationTypeIsSimpleError | PlatformPartnerTypeIsNotBusinessError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ConnectPartnerMemberCompanyError.prototype)
		this.name = "ConnectPartnerMemberCompanyError"
	}
}
export class DisconnectBulkPartnerMemberCompanyError extends PartnerError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformBtxNotEnabledError | PlatformExternalApiFailedError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformTargetPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformBtxNotEnabledError | PlatformExternalApiFailedError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformTargetPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, DisconnectBulkPartnerMemberCompanyError.prototype)
		this.name = "DisconnectBulkPartnerMemberCompanyError"
	}
}
export class DisconnectPartnerMemberCompanyError extends PartnerError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformBtxNotEnabledError | PlatformExternalApiFailedError | PlatformMemberCompanyNotConnectedError | PlatformNotEnabledError | PlatformOngoingTaxInvoiceExistsError | PlatformPartnerNotFoundError | PlatformPartnerTaxationTypeIsSimpleError | PlatformPartnerTypeIsNotBusinessError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformBtxNotEnabledError | PlatformExternalApiFailedError | PlatformMemberCompanyNotConnectedError | PlatformNotEnabledError | PlatformOngoingTaxInvoiceExistsError | PlatformPartnerNotFoundError | PlatformPartnerTaxationTypeIsSimpleError | PlatformPartnerTypeIsNotBusinessError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, DisconnectPartnerMemberCompanyError.prototype)
		this.name = "DisconnectPartnerMemberCompanyError"
	}
}
export class GetPlatformPartnerError extends PartnerError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformPartnerError.prototype)
		this.name = "GetPlatformPartnerError"
	}
}
export class UpdatePlatformPartnerError extends PartnerError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAccountVerificationAlreadyUsedError | PlatformAccountVerificationFailedError | PlatformAccountVerificationNotFoundError | PlatformArchivedPartnerError | PlatformCompanyVerificationAlreadyUsedError | PlatformContractNotFoundError | PlatformInsufficientDataToChangePartnerTypeError | PlatformMemberCompanyConnectedPartnerBrnUnchangeableError | PlatformMemberCompanyConnectedPartnerTypeUnchangeableError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAccountVerificationAlreadyUsedError | PlatformAccountVerificationFailedError | PlatformAccountVerificationNotFoundError | PlatformArchivedPartnerError | PlatformCompanyVerificationAlreadyUsedError | PlatformContractNotFoundError | PlatformInsufficientDataToChangePartnerTypeError | PlatformMemberCompanyConnectedPartnerBrnUnchangeableError | PlatformMemberCompanyConnectedPartnerTypeUnchangeableError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, UpdatePlatformPartnerError.prototype)
		this.name = "UpdatePlatformPartnerError"
	}
}
export class ArchivePlatformPartnerError extends PartnerError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformCannotArchiveScheduledPartnerError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformCannotArchiveScheduledPartnerError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ArchivePlatformPartnerError.prototype)
		this.name = "ArchivePlatformPartnerError"
	}
}
export class RecoverPlatformPartnerError extends PartnerError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, RecoverPlatformPartnerError.prototype)
		this.name = "RecoverPlatformPartnerError"
	}
}
