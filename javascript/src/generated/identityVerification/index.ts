export type * from "./ConfirmIdentityVerificationBody"
export type * from "./ConfirmIdentityVerificationError"
export type * from "./ConfirmIdentityVerificationResponse"
export type * from "./FailedIdentityVerification"
export type * from "./GetIdentityVerificationError"
export type * from "./IdentityVerification"
export type * from "./IdentityVerificationAlreadySentError"
export type * from "./IdentityVerificationAlreadyVerifiedError"
export type * from "./IdentityVerificationFailure"
export type * from "./IdentityVerificationMethod"
export type * from "./IdentityVerificationNotFoundError"
export type * from "./IdentityVerificationNotSentError"
export type * from "./IdentityVerificationOperator"
export type * from "./IdentityVerificationRequestedCustomer"
export type * from "./IdentityVerificationVerifiedCustomer"
export type * from "./ReadyIdentityVerification"
export type * from "./ResendIdentityVerificationError"
export type * from "./ResendIdentityVerificationResponse"
export type * from "./SendIdentityVerificationBody"
export type * from "./SendIdentityVerificationBodyCustomer"
export type * from "./SendIdentityVerificationError"
export type * from "./SendIdentityVerificationResponse"
export type * from "./VerifiedIdentityVerification"
import type { ConfirmIdentityVerificationResponse } from "#generated/identityVerification/ConfirmIdentityVerificationResponse"
import type { IdentityVerification } from "#generated/identityVerification/IdentityVerification"
import type { IdentityVerificationMethod } from "#generated/identityVerification/IdentityVerificationMethod"
import type { IdentityVerificationOperator } from "#generated/identityVerification/IdentityVerificationOperator"
import type { ResendIdentityVerificationResponse } from "#generated/identityVerification/ResendIdentityVerificationResponse"
import type { SendIdentityVerificationBodyCustomer } from "#generated/identityVerification/SendIdentityVerificationBodyCustomer"
import type { SendIdentityVerificationResponse } from "#generated/identityVerification/SendIdentityVerificationResponse"

export type Operations = {
	/**
	 * 본인인증 단건 조회
	 *
	 * 주어진 아이디에 대응되는 본인인증 내역을 조회합니다.
	 *
	 * @param identityVerificationId
	 * 조회할 본인인증 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.IdentityVerificationNotFoundError} 요청된 본인인증 건이 존재하지 않는 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getIdentityVerification: (
		/** 조회할 본인인증 아이디 */
		identityVerificationId: string,
	) => Promise<IdentityVerification>
	/**
	 * 본인인증 요청 전송
	 *
	 * SMS 또는 APP 방식을 이용하여 본인인증 요청을 전송합니다.
	 *
	 * @throws {@link Errors.ChannelNotFoundError} 요청된 채널이 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.IdentityVerificationAlreadySentError} 본인인증 건이 이미 API로 요청된 상태인 경우
	 * @throws {@link Errors.IdentityVerificationAlreadyVerifiedError} 본인인증 건이 이미 인증 완료된 상태인 경우
	 * @throws {@link Errors.IdentityVerificationNotFoundError} 요청된 본인인증 건이 존재하지 않는 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	sendIdentityVerification: (
		options: {
			/** 본인인증 아이디 */
			identityVerificationId: string,
			/** 채널 키 */
			channelKey: string,
			/** 고객 정보 */
			customer: SendIdentityVerificationBodyCustomer,
			/** 사용자 지정 데이터 */
			customData?: string,
			/** PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고) */
			bypass?: object,
			/** 통신사 */
			operator: IdentityVerificationOperator,
			/** 본인인증 방식 */
			method: IdentityVerificationMethod,
		}
	) => Promise<SendIdentityVerificationResponse>
	/**
	 * 본인인증 확인
	 *
	 * 요청된 본인인증에 대한 확인을 진행합니다.
	 *
	 * @param identityVerificationId
	 * 본인인증 아이디
	 * @param otp
	 * OTP (One-Time Password)
	 *
	 * SMS 방식에서만 사용됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.IdentityVerificationAlreadyVerifiedError} 본인인증 건이 이미 인증 완료된 상태인 경우
	 * @throws {@link Errors.IdentityVerificationNotFoundError} 요청된 본인인증 건이 존재하지 않는 경우
	 * @throws {@link Errors.IdentityVerificationNotSentError} 본인인증 건이 API로 요청된 상태가 아닌 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	confirmIdentityVerification: (
		/** 본인인증 아이디 */
		identityVerificationId: string,
		/**
		 * OTP (One-Time Password)
		 *
		 * SMS 방식에서만 사용됩니다.
		 */
		otp?: string,
	) => Promise<ConfirmIdentityVerificationResponse>
	/**
	 * SMS 본인인증 요청 재전송
	 *
	 * SMS 본인인증 요청을 재전송합니다.
	 *
	 * @param identityVerificationId
	 * 본인인증 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.IdentityVerificationAlreadyVerifiedError} 본인인증 건이 이미 인증 완료된 상태인 경우
	 * @throws {@link Errors.IdentityVerificationNotFoundError} 요청된 본인인증 건이 존재하지 않는 경우
	 * @throws {@link Errors.IdentityVerificationNotSentError} 본인인증 건이 API로 요청된 상태가 아닌 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	resendIdentityVerification: (
		/** 본인인증 아이디 */
		identityVerificationId: string,
	) => Promise<ResendIdentityVerificationResponse>
}
