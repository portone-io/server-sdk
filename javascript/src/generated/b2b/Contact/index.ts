import type { B2bCompanyContact } from "../..//common/B2bCompanyContact"
import type { GetB2bContactError } from "../..//b2b/Contact/GetB2bContactError"
import type { GetB2bContactIdExistenceResponse } from "../..//b2b/Contact/GetB2bContactIdExistenceResponse"
import type { UpdateB2bContactError } from "../..//b2b/Contact/UpdateB2bContactError"
import type { UpdateB2bContactResponse } from "../..//b2b/Contact/UpdateB2bContactResponse"
import type { getB2bContactIdExistenceError } from "../..//b2b/Contact/getB2bContactIdExistenceError"
import * as Errors from "../..//errors"
export type { GetB2bContactIdExistenceResponse } from "./GetB2bContactIdExistenceResponse"
export type { UpdateB2bContactBody } from "./UpdateB2bContactBody"
export type { UpdateB2bContactResponse } from "./UpdateB2bContactResponse"
/** @ignore */
export function ContactClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): ContactClient {
	return {
		getB2bContact: async (
			contactId: string,
			test?: boolean,
		): Promise<B2bCompanyContact> => {
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/contacts/${contactId}?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetB2bContactError = await response.json()
				switch (errorResponse.type) {
				case "B2B_CONTACT_NOT_FOUND":
					throw new Errors.B2bContactNotFoundError(errorResponse)
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
		updateB2bContact: async (
			options: {
				contactId: string,
				test?: boolean,
				password?: string,
				name?: string,
				phoneNumber?: string,
				email?: string,
			}
		): Promise<UpdateB2bContactResponse> => {
			const {
				contactId,
				test,
				password,
				name,
				phoneNumber,
				email,
			} = options
			const requestBody = JSON.stringify({
				password,
				name,
				phoneNumber,
				email,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/contacts/${contactId}?${query}`, baseUrl),
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
				const errorResponse: UpdateB2bContactError = await response.json()
				switch (errorResponse.type) {
				case "B2B_CONTACT_NOT_FOUND":
					throw new Errors.B2bContactNotFoundError(errorResponse)
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
		getB2bContactIdExistence: async (
			contactId: string,
			test?: boolean,
		): Promise<GetB2bContactIdExistenceResponse> => {
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/b2b/contacts/${contactId}/exists?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: getB2bContactIdExistenceError = await response.json()
				switch (errorResponse.type) {
				case "B2B_EXTERNAL_SERVICE":
					throw new Errors.B2bExternalServiceError(errorResponse)
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
export type ContactClient = {
	/**
	 * 담당자 조회
	 *
	 * 연동 사업자에 등록된 담당자를 조회합니다.
	 *
	 * @param contactId
	 * 담당자 ID
	 * @param test
	 * 테스트 모드 여부
	 *
	 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
	 *
	 * @throws {@link Errors.B2bContactNotFoundError} 담당자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bMemberCompanyNotFoundError} 연동 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getB2bContact: (
		/** 담당자 ID */
		contactId: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<B2bCompanyContact>
	/**
	 * 담당자 정보 수정
	 *
	 * 담당자 정보를 수정합니다.
	 *
	 * @throws {@link Errors.B2bContactNotFoundError} 담당자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bMemberCompanyNotFoundError} 연동 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	updateB2bContact: (
		options: {
			/** 담당자 ID */
			contactId: string,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 비밀번호 */
			password?: string,
			/** 담당자 성명 */
			name?: string,
			/** 담당자 핸드폰 번호 */
			phoneNumber?: string,
			/** 담당자 이메일 */
			email?: string,
		}
	) => Promise<UpdateB2bContactResponse>
	/**
	 * 담당자 ID 존재 여부 확인
	 *
	 * 담당자 ID가 이미 사용중인지 확인합니다.
	 *
	 * @param contactId
	 * 담당자 ID
	 * @param test
	 * 테스트 모드 여부
	 *
	 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getB2bContactIdExistence: (
		/** 담당자 ID */
		contactId: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<GetB2bContactIdExistenceResponse>
}

