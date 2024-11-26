import type { IdentityVerificationVerifiedCustomer } from "./../identityVerification/IdentityVerificationVerifiedCustomer"
import type { SelectedChannel } from "./../common/SelectedChannel"
/** 완료된 본인인증 내역 */
export type VerifiedIdentityVerification = {
	/** 본인인증 상태 */
	status: "VERIFIED"
	/** 본인인증 내역 아이디 */
	id: string
	/** 사용된 본인인증 채널 */
	channel?: SelectedChannel
	/** 인증된 고객 정보 */
	verifiedCustomer: IdentityVerificationVerifiedCustomer
	/** 사용자 지정 데이터 */
	customData?: string
	/**
	 * 본인인증 요청 시점
	 * (RFC 3339 date-time)
	 */
	requestedAt: string
	/**
	 * 업데이트 시점
	 * (RFC 3339 date-time)
	 */
	updatedAt: string
	/**
	 * 상태 업데이트 시점
	 * (RFC 3339 date-time)
	 */
	statusChangedAt: string
	/**
	 * 본인인증 완료 시점
	 * (RFC 3339 date-time)
	 */
	verifiedAt: string
	/** 본인인증 내역 PG사 아이디 */
	pgTxId: string
	/** PG사 응답 데이터 */
	pgRawResponse: string
}
