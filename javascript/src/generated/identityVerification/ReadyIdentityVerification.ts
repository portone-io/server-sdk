import type { IdentityVerificationRequestedCustomer } from "./../identityVerification/IdentityVerificationRequestedCustomer"
import type { PortOneVersion } from "./../common/PortOneVersion"
import type { SelectedChannel } from "./../common/SelectedChannel"
/** 준비 상태의 본인인증 내역 */
export type ReadyIdentityVerification = {
	/** 본인인증 상태 */
	status: "READY"
	/** 고객사 본인인증 번호 */
	id: string
	/** 사용된 본인인증 채널 */
	channel?: SelectedChannel
	/** 요청 시 고객 정보 */
	requestedCustomer: IdentityVerificationRequestedCustomer
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
	/** 포트원 버전 */
	version: PortOneVersion
}
