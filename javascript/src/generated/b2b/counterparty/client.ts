import { CounterpartyError } from "./CounterpartyError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { B2bCertificate } from "../../../generated/b2b/counterparty/B2bCertificate"
import type { B2bCertificateUnregisteredError } from "../../../generated/b2b/counterparty/B2bCertificateUnregisteredError"
import type { B2bCounterparty } from "../../../generated/b2b/counterparty/B2bCounterparty"
import type { B2bCounterpartyBrnInvalidError } from "../../../generated/b2b/counterparty/B2bCounterpartyBrnInvalidError"
import type { B2bCounterpartyBrnModificationNotAllowedError } from "../../../generated/b2b/counterparty/B2bCounterpartyBrnModificationNotAllowedError"
import type { B2bCounterpartyCreateOptions } from "../../../generated/b2b/counterparty/B2bCounterpartyCreateOptions"
import type { B2bCounterpartyFilter } from "../../../generated/b2b/counterparty/B2bCounterpartyFilter"
import type { B2bCounterpartyIdAlreadyExistsByPartnerError } from "../../../generated/b2b/counterparty/B2bCounterpartyIdAlreadyExistsByPartnerError"
import type { B2bCounterpartyIdAlreadyExistsError } from "../../../generated/b2b/counterparty/B2bCounterpartyIdAlreadyExistsError"
import type { B2bCounterpartyInput } from "../../../generated/b2b/counterparty/B2bCounterpartyInput"
import type { B2bCounterpartyMissingRequiredFieldsError } from "../../../generated/b2b/counterparty/B2bCounterpartyMissingRequiredFieldsError"
import type { B2bCounterpartyNotFoundError } from "../../../generated/common/B2bCounterpartyNotFoundError"
import type { B2bCounterpartyNtsConnectionFailedError } from "../../../generated/b2b/counterparty/B2bCounterpartyNtsConnectionFailedError"
import type { B2bCounterpartyNtsNotConnectedError } from "../../../generated/common/B2bCounterpartyNtsNotConnectedError"
import type { B2bCounterpartyOngoingTaxInvoiceExistsError } from "../../../generated/b2b/counterparty/B2bCounterpartyOngoingTaxInvoiceExistsError"
import type { B2bCounterpartyPartnerNotConnectableError } from "../../../generated/b2b/counterparty/B2bCounterpartyPartnerNotConnectableError"
import type { B2bCounterpartyPartnerNotDeletableError } from "../../../generated/b2b/counterparty/B2bCounterpartyPartnerNotDeletableError"
import type { B2bCounterpartyPartnerNotUpdatableError } from "../../../generated/b2b/counterparty/B2bCounterpartyPartnerNotUpdatableError"
import type { B2bCounterpartySelfOriginBrnMismatchError } from "../../../generated/b2b/counterparty/B2bCounterpartySelfOriginBrnMismatchError"
import type { B2bCounterpartyTooManyAdditionalContactsError } from "../../../generated/b2b/counterparty/B2bCounterpartyTooManyAdditionalContactsError"
import type { B2bCounterpartyVerificationBrnMismatchError } from "../../../generated/b2b/counterparty/B2bCounterpartyVerificationBrnMismatchError"
import type { B2bCounterpartyVerificationInvalidError } from "../../../generated/b2b/counterparty/B2bCounterpartyVerificationInvalidError"
import type { B2bCounterpartyVerificationNotFoundError } from "../../../generated/b2b/counterparty/B2bCounterpartyVerificationNotFoundError"
import type { B2bCounterpartyVerificationTypeMismatchError } from "../../../generated/b2b/counterparty/B2bCounterpartyVerificationTypeMismatchError"
import type { B2bExternalServiceError } from "../../../generated/common/B2bExternalServiceError"
import type { B2bNotEnabledError } from "../../../generated/common/B2bNotEnabledError"
import type { CreateB2bCounterpartyResponse } from "../../../generated/b2b/counterparty/CreateB2bCounterpartyResponse"
import type { DeleteB2bCounterpartyResponse } from "../../../generated/b2b/counterparty/DeleteB2bCounterpartyResponse"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetB2bCounterpartiesResponse } from "../../../generated/b2b/counterparty/GetB2bCounterpartiesResponse"
import type { GetB2bCounterpartyCertificateRegistrationUrlResponse } from "../../../generated/b2b/counterparty/GetB2bCounterpartyCertificateRegistrationUrlResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { PageInput } from "../../../generated/common/PageInput"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
import type { UpdateB2bCounterpartyResponse } from "../../../generated/b2b/counterparty/UpdateB2bCounterpartyResponse"
import type { ValidateB2bCounterpartyCertificateResponse } from "../../../generated/b2b/counterparty/ValidateB2bCounterpartyCertificateResponse"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function CounterpartyClient(init: PortOneClientInit): CounterpartyClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getB2bCounterpartyCertificateRegistrationUrl: async (
			options: {
				brn: string,
				test?: boolean,
			}
		): Promise<GetB2bCounterpartyCertificateRegistrationUrlResponse> => {
			const {
				brn,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/counterparties/${encodeURIComponent(brn)}/certificate/registration-url?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetB2bCounterpartyCertificateRegistrationUrlError(await response.json())
			}
			return response.json()
		},
		validateB2bCounterpartyCertificate: async (
			options: {
				brn: string,
				test?: boolean,
			}
		): Promise<ValidateB2bCounterpartyCertificateResponse> => {
			const {
				brn,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/counterparties/${encodeURIComponent(brn)}/certificate/validate?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new ValidateB2bCounterpartyCertificateError(await response.json())
			}
			return response.json()
		},
		getB2bCounterpartyCertificate: async (
			options: {
				brn: string,
				test?: boolean,
			}
		): Promise<B2bCertificate> => {
			const {
				brn,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/counterparties/${encodeURIComponent(brn)}/certificate?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetB2bCounterpartyCertificateError(await response.json())
			}
			return response.json()
		},
		getB2bCounterparty: async (
			options: {
				counterpartyId: string,
				test?: boolean,
			}
		): Promise<B2bCounterparty> => {
			const {
				counterpartyId,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/counterparties/${encodeURIComponent(counterpartyId)}?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetB2bCounterpartyError(await response.json())
			}
			return response.json()
		},
		deleteB2bCounterparty: async (
			options: {
				counterpartyId: string,
				test?: boolean,
			}
		): Promise<DeleteB2bCounterpartyResponse> => {
			const {
				counterpartyId,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/counterparties/${encodeURIComponent(counterpartyId)}?${query}`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new DeleteB2bCounterpartyError(await response.json())
			}
			return response.json()
		},
		updateB2bCounterparty: async (
			options_: {
				counterpartyId: string,
				test?: boolean,
				counterparty: B2bCounterpartyInput,
				options?: B2bCounterpartyCreateOptions,
			}
		): Promise<UpdateB2bCounterpartyResponse> => {
			const {
				counterpartyId,
				test,
				counterparty,
				options,
			} = options_
			const requestBody = JSON.stringify({
				counterparty,
				options,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/counterparties/${encodeURIComponent(counterpartyId)}?${query}`, baseUrl),
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
				throw new UpdateB2bCounterpartyError(await response.json())
			}
			return response.json()
		},
		getB2bCounterparties: async (
			options?: {
				test?: boolean,
				page?: PageInput,
				filter?: B2bCounterpartyFilter,
			}
		): Promise<GetB2bCounterpartiesResponse> => {
			const test = options?.test
			const page = options?.page
			const filter = options?.filter
			const requestBody = JSON.stringify({
				page,
				filter,
			})
			const query = [
				["test", test],
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/counterparties?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetB2bCounterpartiesError(await response.json())
			}
			return response.json()
		},
		createB2bCounterparty: async (
			options_: {
				test?: boolean,
				counterpartyId?: string,
				counterparty: B2bCounterpartyInput,
				options?: B2bCounterpartyCreateOptions,
			}
		): Promise<CreateB2bCounterpartyResponse> => {
			const {
				test,
				counterpartyId,
				counterparty,
				options,
			} = options_
			const requestBody = JSON.stringify({
				counterpartyId,
				counterparty,
				options,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/counterparties?${query}`, baseUrl),
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
				throw new CreateB2bCounterpartyError(await response.json())
			}
			return response.json()
		},
	}
}
export type CounterpartyClient = {
	/**
	 * 사업자 인증서 등록 URL 조회
	 *
	 * 연동 사업자의 인증서를 등록하기 위한 URL을 조회합니다.
	 *
	 * @throws {@link GetB2bCounterpartyCertificateRegistrationUrlError}
	 */
	getB2bCounterpartyCertificateRegistrationUrl: (
		options: {
			/** 사업자등록번호 */
			brn: string,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<GetB2bCounterpartyCertificateRegistrationUrlResponse>
	/**
	 * 사업자 인증서 유효성 검증
	 *
	 * 연동 사업자가 등록한 인증서의 유효성을 검증합니다.
	 *
	 * @throws {@link ValidateB2bCounterpartyCertificateError}
	 */
	validateB2bCounterpartyCertificate: (
		options: {
			/** 사업자등록번호 */
			brn: string,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<ValidateB2bCounterpartyCertificateResponse>
	/**
	 * 인증서 조회
	 *
	 * 연동 사업자의 인증서를 조회합니다.
	 *
	 * @throws {@link GetB2bCounterpartyCertificateError}
	 */
	getB2bCounterpartyCertificate: (
		options: {
			/** 사업자등록번호 */
			brn: string,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<B2bCertificate>
	/**
	 * 거래처 조회
	 *
	 * 거래처를 조회합니다.
	 *
	 * @throws {@link GetB2bCounterpartyError}
	 */
	getB2bCounterparty: (
		options: {
			/** 거래처 ID */
			counterpartyId: string,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<B2bCounterparty>
	/**
	 * 거래처 삭제
	 *
	 * 거래처를 삭제합니다.
	 *
	 * @throws {@link DeleteB2bCounterpartyError}
	 */
	deleteB2bCounterparty: (
		options: {
			/** 거래처 ID */
			counterpartyId: string,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<DeleteB2bCounterpartyResponse>
	/**
	 * 거래처 정보 수정
	 *
	 * 거래처 정보를 수정합니다.
	 *
	 * @throws {@link UpdateB2bCounterpartyError}
	 */
	updateB2bCounterparty: (
		options: {
			/** 거래처 ID */
			counterpartyId: string,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 거래처 정보 */
			counterparty: B2bCounterpartyInput,
			/**
			 * 확인 옵션
			 *
			 * 사업자 정보 및 휴폐업 상태 조회 옵션입니다.
			 */
			options?: B2bCounterpartyCreateOptions,
		}
	) => Promise<UpdateB2bCounterpartyResponse>
	/**
	 * 거래처 검색
	 *
	 * 거래처를 검색합니다.
	 *
	 * @throws {@link GetB2bCounterpartiesError}
	 */
	getB2bCounterparties: (
		options?: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 페이지 정보 */
			page?: PageInput,
			/** 검색 필터 */
			filter?: B2bCounterpartyFilter,
		}
	) => Promise<GetB2bCounterpartiesResponse>
	/**
	 * 거래처 생성
	 *
	 * 거래처를 생성합니다.
	 *
	 * @throws {@link CreateB2bCounterpartyError}
	 */
	createB2bCounterparty: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/**
			 * 거래처 아이디
			 *
			 * 입력하지 않으면 임의의 ID가 채번됩니다.
			 */
			counterpartyId?: string,
			/** 거래처 정보 */
			counterparty: B2bCounterpartyInput,
			/** 거래처 생성 옵션 */
			options?: B2bCounterpartyCreateOptions,
		}
	) => Promise<CreateB2bCounterpartyResponse>
}
export class GetB2bCounterpartyCertificateRegistrationUrlError extends CounterpartyError {
	declare readonly data: B2bCounterpartyNotFoundError | B2bCounterpartyNtsNotConnectedError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bCounterpartyNotFoundError | B2bCounterpartyNtsNotConnectedError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetB2bCounterpartyCertificateRegistrationUrlError.prototype)
		this.name = "GetB2bCounterpartyCertificateRegistrationUrlError"
	}
}
export class ValidateB2bCounterpartyCertificateError extends CounterpartyError {
	declare readonly data: B2bCertificateUnregisteredError | B2bCounterpartyNotFoundError | B2bCounterpartyNtsNotConnectedError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bCertificateUnregisteredError | B2bCounterpartyNotFoundError | B2bCounterpartyNtsNotConnectedError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ValidateB2bCounterpartyCertificateError.prototype)
		this.name = "ValidateB2bCounterpartyCertificateError"
	}
}
export class GetB2bCounterpartyCertificateError extends CounterpartyError {
	declare readonly data: B2bCertificateUnregisteredError | B2bCounterpartyNotFoundError | B2bCounterpartyNtsNotConnectedError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bCertificateUnregisteredError | B2bCounterpartyNotFoundError | B2bCounterpartyNtsNotConnectedError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetB2bCounterpartyCertificateError.prototype)
		this.name = "GetB2bCounterpartyCertificateError"
	}
}
export class GetB2bCounterpartyError extends CounterpartyError {
	declare readonly data: B2bCounterpartyNotFoundError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bCounterpartyNotFoundError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetB2bCounterpartyError.prototype)
		this.name = "GetB2bCounterpartyError"
	}
}
export class DeleteB2bCounterpartyError extends CounterpartyError {
	declare readonly data: B2bCounterpartyNotFoundError | B2bCounterpartyOngoingTaxInvoiceExistsError | B2bCounterpartyPartnerNotDeletableError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bCounterpartyNotFoundError | B2bCounterpartyOngoingTaxInvoiceExistsError | B2bCounterpartyPartnerNotDeletableError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, DeleteB2bCounterpartyError.prototype)
		this.name = "DeleteB2bCounterpartyError"
	}
}
export class UpdateB2bCounterpartyError extends CounterpartyError {
	declare readonly data: B2bCounterpartyBrnModificationNotAllowedError | B2bCounterpartyMissingRequiredFieldsError | B2bCounterpartyNotFoundError | B2bCounterpartyPartnerNotUpdatableError | B2bCounterpartyTooManyAdditionalContactsError | B2bCounterpartyVerificationBrnMismatchError | B2bCounterpartyVerificationInvalidError | B2bCounterpartyVerificationNotFoundError | B2bCounterpartyVerificationTypeMismatchError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bCounterpartyBrnModificationNotAllowedError | B2bCounterpartyMissingRequiredFieldsError | B2bCounterpartyNotFoundError | B2bCounterpartyPartnerNotUpdatableError | B2bCounterpartyTooManyAdditionalContactsError | B2bCounterpartyVerificationBrnMismatchError | B2bCounterpartyVerificationInvalidError | B2bCounterpartyVerificationNotFoundError | B2bCounterpartyVerificationTypeMismatchError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, UpdateB2bCounterpartyError.prototype)
		this.name = "UpdateB2bCounterpartyError"
	}
}
export class GetB2bCounterpartiesError extends CounterpartyError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetB2bCounterpartiesError.prototype)
		this.name = "GetB2bCounterpartiesError"
	}
}
export class CreateB2bCounterpartyError extends CounterpartyError {
	declare readonly data: B2bCounterpartyBrnInvalidError | B2bCounterpartyIdAlreadyExistsError | B2bCounterpartyIdAlreadyExistsByPartnerError | B2bCounterpartyMissingRequiredFieldsError | B2bCounterpartyNtsConnectionFailedError | B2bCounterpartyPartnerNotConnectableError | B2bCounterpartySelfOriginBrnMismatchError | B2bCounterpartyTooManyAdditionalContactsError | B2bCounterpartyVerificationBrnMismatchError | B2bCounterpartyVerificationInvalidError | B2bCounterpartyVerificationNotFoundError | B2bCounterpartyVerificationTypeMismatchError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: B2bCounterpartyBrnInvalidError | B2bCounterpartyIdAlreadyExistsError | B2bCounterpartyIdAlreadyExistsByPartnerError | B2bCounterpartyMissingRequiredFieldsError | B2bCounterpartyNtsConnectionFailedError | B2bCounterpartyPartnerNotConnectableError | B2bCounterpartySelfOriginBrnMismatchError | B2bCounterpartyTooManyAdditionalContactsError | B2bCounterpartyVerificationBrnMismatchError | B2bCounterpartyVerificationInvalidError | B2bCounterpartyVerificationNotFoundError | B2bCounterpartyVerificationTypeMismatchError | B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CreateB2bCounterpartyError.prototype)
		this.name = "CreateB2bCounterpartyError"
	}
}
