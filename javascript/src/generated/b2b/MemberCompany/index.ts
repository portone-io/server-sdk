import type { B2bCertificate } from "../..//b2b/MemberCompany/B2bCertificate"
import type { B2bCompanyContactInput } from "../..//b2b/MemberCompany/B2bCompanyContactInput"
import type { B2bCompanyState } from "../..//b2b/MemberCompany/B2bCompanyState"
import type { B2bMemberCompany } from "../..//b2b/MemberCompany/B2bMemberCompany"
import type { B2bMemberCompanyInput } from "../..//b2b/MemberCompany/B2bMemberCompanyInput"
import type { Bank } from "../..//common/Bank"
import type { GetB2bAccountHolderError } from "../..//b2b/MemberCompany/GetB2bAccountHolderError"
import type { GetB2bBankAccountHolderResponse } from "../..//b2b/MemberCompany/GetB2bBankAccountHolderResponse"
import type { GetB2bCertificateError } from "../..//b2b/MemberCompany/GetB2bCertificateError"
import type { GetB2bCertificateRegistrationUrlError } from "../..//b2b/MemberCompany/GetB2bCertificateRegistrationUrlError"
import type { GetB2bCertificateRegistrationUrlResponse } from "../..//b2b/MemberCompany/GetB2bCertificateRegistrationUrlResponse"
import type { GetB2bCompanyStateError } from "../..//b2b/MemberCompany/GetB2bCompanyStateError"
import type { GetB2bMemberCompanyError } from "../..//b2b/MemberCompany/GetB2bMemberCompanyError"
import type { RegisterB2bMemberCompanyError } from "../..//b2b/MemberCompany/RegisterB2bMemberCompanyError"
import type { RegisterB2bMemberCompanyResponse } from "../..//b2b/MemberCompany/RegisterB2bMemberCompanyResponse"
import type { UpdateB2bMemberCompanyError } from "../..//b2b/MemberCompany/UpdateB2bMemberCompanyError"
import type { UpdateB2bMemberCompanyResponse } from "../..//b2b/MemberCompany/UpdateB2bMemberCompanyResponse"
import type { ValidateB2bCertificateError } from "../..//b2b/MemberCompany/ValidateB2bCertificateError"
import type { ValidateB2bCertificateResponse } from "../..//b2b/MemberCompany/ValidateB2bCertificateResponse"
import * as Errors from "../..//errors"
export type { B2bCertificate } from "./B2bCertificate"
export type { B2bCertificateType } from "./B2bCertificateType"
export type { B2bCompanyContactInput } from "./B2bCompanyContactInput"
export type { B2bCompanyState } from "./B2bCompanyState"
export type { B2bCompanyStateTaxationType } from "./B2bCompanyStateTaxationType"
export type { B2bMemberCompany } from "./B2bMemberCompany"
export type { B2bMemberCompanyInput } from "./B2bMemberCompanyInput"
export type { GetB2bBankAccountHolderResponse } from "./GetB2bBankAccountHolderResponse"
export type { GetB2bCertificateRegistrationUrlResponse } from "./GetB2bCertificateRegistrationUrlResponse"
export type { Input } from "./Input"
export type { RegisterB2bMemberCompanyBody } from "./RegisterB2bMemberCompanyBody"
export type { RegisterB2bMemberCompanyResponse } from "./RegisterB2bMemberCompanyResponse"
export type { UpdateB2bMemberCompanyBody } from "./UpdateB2bMemberCompanyBody"
export type { UpdateB2bMemberCompanyResponse } from "./UpdateB2bMemberCompanyResponse"
export type { ValidateB2bCertificateResponse } from "./ValidateB2bCertificateResponse"
/** @ignore */
export function MemberCompanyClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): MemberCompanyClient {
	return {
		getB2bMemberCompany: async (
			brn: string,
			test?: boolean,
		): Promise<B2bMemberCompany> => {
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/member-companies/${brn}?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetB2bMemberCompanyError = await response.json()
				switch (errorResponse.type) {
				case "B2B_EXTERNAL_SERVICE":
					throw new Errors.B2bExternalServiceError(errorResponse)
				case "B2B_MEMBER_COMPANY_NOT_FOUND":
					throw new Errors.B2bMemberCompanyNotFoundError(errorResponse)
				case "B2B_NOT_ENABLED":
					throw new Errors.B2bNotEnabledError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		updateB2bMemberCompany: async (
			options: {
				brn: string,
				test?: boolean,
				companyName?: string,
				representativeName?: string,
				address?: string,
				businessType?: string,
				businessClass?: string,
			}
		): Promise<UpdateB2bMemberCompanyResponse> => {
			const {
				brn,
				test,
				companyName,
				representativeName,
				address,
				businessType,
				businessClass,
			} = options
			const requestBody = JSON.stringify({
				companyName,
				representativeName,
				address,
				businessType,
				businessClass,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/member-companies/${brn}?${query}`, baseUrl),
				{
					method: "patch",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: UpdateB2bMemberCompanyError = await response.json()
				switch (errorResponse.type) {
				case "B2B_EXTERNAL_SERVICE":
					throw new Errors.B2bExternalServiceError(errorResponse)
				case "B2B_MEMBER_COMPANY_NOT_FOUND":
					throw new Errors.B2bMemberCompanyNotFoundError(errorResponse)
				case "B2B_NOT_ENABLED":
					throw new Errors.B2bNotEnabledError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		registerB2bMemberCompany: async (
			company: B2bMemberCompanyInput,
			contact: B2bCompanyContactInput,
			test?: boolean,
		): Promise<RegisterB2bMemberCompanyResponse> => {
			const requestBody = JSON.stringify({
				company,
				contact,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/member-companies?${query}`, baseUrl),
				{
					method: "post",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: RegisterB2bMemberCompanyError = await response.json()
				switch (errorResponse.type) {
				case "B2B_COMPANY_ALREADY_REGISTERED":
					throw new Errors.B2bCompanyAlreadyRegisteredError(errorResponse)
				case "B2B_EXTERNAL_SERVICE":
					throw new Errors.B2bExternalServiceError(errorResponse)
				case "B2B_ID_ALREADY_EXISTS":
					throw new Errors.B2bIdAlreadyExistsError(errorResponse)
				case "B2B_NOT_ENABLED":
					throw new Errors.B2bNotEnabledError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getB2bCertificateRegistrationUrl: async (
			brn: string,
			test?: boolean,
		): Promise<GetB2bCertificateRegistrationUrlResponse> => {
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/member-companies/${brn}/certificate/registration-url?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetB2bCertificateRegistrationUrlError = await response.json()
				switch (errorResponse.type) {
				case "B2B_EXTERNAL_SERVICE":
					throw new Errors.B2bExternalServiceError(errorResponse)
				case "B2B_MEMBER_COMPANY_NOT_FOUND":
					throw new Errors.B2bMemberCompanyNotFoundError(errorResponse)
				case "B2B_NOT_ENABLED":
					throw new Errors.B2bNotEnabledError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		validateB2bCertificate: async (
			brn: string,
			test?: boolean,
		): Promise<ValidateB2bCertificateResponse> => {
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/member-companies/${brn}/certificate/validate?${query}`, baseUrl),
				{
					method: "post",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: ValidateB2bCertificateError = await response.json()
				switch (errorResponse.type) {
				case "B2B_CERTIFICATE_UNREGISTERED":
					throw new Errors.B2bCertificateUnregisteredError(errorResponse)
				case "B2B_EXTERNAL_SERVICE":
					throw new Errors.B2bExternalServiceError(errorResponse)
				case "B2B_MEMBER_COMPANY_NOT_FOUND":
					throw new Errors.B2bMemberCompanyNotFoundError(errorResponse)
				case "B2B_NOT_ENABLED":
					throw new Errors.B2bNotEnabledError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getB2bCertificate: async (
			brn: string,
			test?: boolean,
		): Promise<B2bCertificate> => {
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/member-companies/${brn}/certificate?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetB2bCertificateError = await response.json()
				switch (errorResponse.type) {
				case "B2B_CERTIFICATE_UNREGISTERED":
					throw new Errors.B2bCertificateUnregisteredError(errorResponse)
				case "B2B_EXTERNAL_SERVICE":
					throw new Errors.B2bExternalServiceError(errorResponse)
				case "B2B_MEMBER_COMPANY_NOT_FOUND":
					throw new Errors.B2bMemberCompanyNotFoundError(errorResponse)
				case "B2B_NOT_ENABLED":
					throw new Errors.B2bNotEnabledError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getB2bBankAccountHolder: async (
			bank: Bank,
			accountNumber: string,
			test?: boolean,
		): Promise<GetB2bBankAccountHolderResponse> => {
			const requestBody = JSON.stringify({
				bank,
				accountNumber,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/bank-accounts/holder?${query}`, baseUrl),
				{
					method: "post",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: GetB2bAccountHolderError = await response.json()
				switch (errorResponse.type) {
				case "B2B_BANK_ACCOUNT_NOT_FOUND":
					throw new Errors.B2bBankAccountNotFoundError(errorResponse)
				case "B2B_EXTERNAL_SERVICE":
					throw new Errors.B2bExternalServiceError(errorResponse)
				case "B2B_FINANCIAL_SYSTEM_COMMUNICATION":
					throw new Errors.B2bFinancialSystemCommunicationError(errorResponse)
				case "B2B_FINANCIAL_SYSTEM_FAILURE":
					throw new Errors.B2bFinancialSystemFailureError(errorResponse)
				case "B2B_FINANCIAL_SYSTEM_UNDER_MAINTENANCE":
					throw new Errors.B2bFinancialSystemUnderMaintenanceError(errorResponse)
				case "B2B_FOREIGN_EXCHANGE_ACCOUNT":
					throw new Errors.B2bForeignExchangeAccountError(errorResponse)
				case "B2B_NOT_ENABLED":
					throw new Errors.B2bNotEnabledError(errorResponse)
				case "B2B_REGULAR_MAINTENANCE_TIME":
					throw new Errors.B2bRegularMaintenanceTimeError(errorResponse)
				case "B2B_SUSPENDED_ACCOUNT":
					throw new Errors.B2bSuspendedAccountError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getB2bCompanyState: async (
			brn: string,
			test?: boolean,
		): Promise<B2bCompanyState> => {
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/companies/${brn}/state?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetB2bCompanyStateError = await response.json()
				switch (errorResponse.type) {
				case "B2B_COMPANY_NOT_FOUND":
					throw new Errors.B2bCompanyNotFoundError(errorResponse)
				case "B2B_EXTERNAL_SERVICE":
					throw new Errors.B2bExternalServiceError(errorResponse)
				case "B2B_HOMETAX_UNDER_MAINTENANCE":
					throw new Errors.B2bHometaxUnderMaintenanceError(errorResponse)
				case "B2B_NOT_ENABLED":
					throw new Errors.B2bNotEnabledError(errorResponse)
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
	}
}
export type MemberCompanyClient = {
	/**
	 * 연동 사업자 조회
	 *
	 * 포트원 B2B 서비스에 연동된 사업자를 조회합니다.
	 *
	 * @param brn
	 * 사업자등록번호
	 * @param test
	 * 테스트 모드 여부
	 *
	 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bMemberCompanyNotFoundError} 연동 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getB2bMemberCompany: (
		/** 사업자등록번호 */
		brn: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<B2bMemberCompany>
	/**
	 * 연동 사업자 정보 수정
	 *
	 * 연동 사업자 정보를 수정합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bMemberCompanyNotFoundError} 연동 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	updateB2bMemberCompany: (
		options: {
			/** 사업자등록번호 */
			brn: string,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 회사명 */
			companyName?: string,
			/** 대표자 성명 */
			representativeName?: string,
			/** 회사 주소 */
			address?: string,
			/** 업태 */
			businessType?: string,
			/** 업종 */
			businessClass?: string,
		}
	) => Promise<UpdateB2bMemberCompanyResponse>
	/**
	 * 사업자 연동
	 *
	 * 포트원 B2B 서비스에 사업자를 연동합니다.
	 *
	 * @param test
	 * 테스트 모드 여부
	 *
	 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
	 * @param company
	 * 사업자 정보
	 * @param contact
	 * 담당자 정보
	 *
	 * @throws {@link Errors.B2bCompanyAlreadyRegisteredError} 사업자가 이미 연동되어 있는 경우
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bIdAlreadyExistsError} ID가 이미 사용중인 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	registerB2bMemberCompany: (
		/** 사업자 정보 */
		company: B2bMemberCompanyInput,
		/** 담당자 정보 */
		contact: B2bCompanyContactInput,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<RegisterB2bMemberCompanyResponse>
	/**
	 * 사업자 인증서 등록 URL 조회
	 *
	 * 연동 사업자의 인증서를 등록하기 위한 URL을 조회합니다.
	 *
	 * @param brn
	 * 사업자등록번호
	 * @param test
	 * 테스트 모드 여부
	 *
	 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bMemberCompanyNotFoundError} 연동 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getB2bCertificateRegistrationUrl: (
		/** 사업자등록번호 */
		brn: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<GetB2bCertificateRegistrationUrlResponse>
	/**
	 * 사업자 인증서 유효성 검증
	 *
	 * 연동 사업자가 등록한 인증서의 유효성을 검증합니다.
	 *
	 * @param brn
	 * 사업자등록번호
	 * @param test
	 * 테스트 모드 여부
	 *
	 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
	 *
	 * @throws {@link Errors.B2bCertificateUnregisteredError} 인증서가 등록되어 있지 않은 경우
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bMemberCompanyNotFoundError} 연동 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	validateB2bCertificate: (
		/** 사업자등록번호 */
		brn: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<ValidateB2bCertificateResponse>
	/**
	 * 인증서 조회
	 *
	 * 연동 사업자의 인증서를 조회합니다.
	 *
	 * @param brn
	 * 사업자등록번호
	 * @param test
	 * 테스트 모드 여부
	 *
	 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
	 *
	 * @throws {@link Errors.B2bCertificateUnregisteredError} 인증서가 등록되어 있지 않은 경우
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bMemberCompanyNotFoundError} 연동 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getB2bCertificate: (
		/** 사업자등록번호 */
		brn: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<B2bCertificate>
	/**
	 * 예금주 조회
	 *
	 * 원하는 계좌의 예금주를 조회합니다.
	 *
	 * @param test
	 * 테스트 모드 여부
	 *
	 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
	 * @param bank
	 * 은행
	 * @param accountNumber
	 * 계좌번호
	 *
	 * @throws {@link Errors.B2bBankAccountNotFoundError} 계좌가 존재하지 않는 경우
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bFinancialSystemCommunicationError} 금융기관과의 통신에 실패한 경우
	 * @throws {@link Errors.B2bFinancialSystemFailureError} 금융기관 장애
	 * @throws {@link Errors.B2bFinancialSystemUnderMaintenanceError} 금융기관 시스템이 점검 중인 경우
	 * @throws {@link Errors.B2bForeignExchangeAccountError} 계좌 정보 조회가 불가능한 외화 계좌인 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bRegularMaintenanceTimeError} 금융기관 시스템이 정기 점검 중인 경우
	 * @throws {@link Errors.B2bSuspendedAccountError} 정지 계좌인 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getB2bBankAccountHolder: (
		/** 은행 */
		bank: Bank,
		/** 계좌번호 */
		accountNumber: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<GetB2bBankAccountHolderResponse>
	/**
	 * 사업자 상태 조회
	 *
	 * 원하는 사업자의 상태를 조회합니다. 포트원 B2B 서비스에 연동 및 등록되지 않은 사업자도 조회 가능합니다.
	 *
	 * @param brn
	 * 사업자등록번호
	 * @param test
	 * 테스트 모드 여부
	 *
	 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
	 *
	 * @throws {@link Errors.B2bCompanyNotFoundError} 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bHometaxUnderMaintenanceError} 홈택스가 점검중이거나 순단이 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getB2bCompanyState: (
		/** 사업자등록번호 */
		brn: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<B2bCompanyState>
}

