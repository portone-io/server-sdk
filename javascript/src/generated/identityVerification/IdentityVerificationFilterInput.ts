import type { Carrier } from "./../identityVerification/Carrier"
import type { IdentityVerificationFilterCustomerInput } from "./../identityVerification/IdentityVerificationFilterCustomerInput"
import type { IdentityVerificationStatus } from "./../identityVerification/IdentityVerificationStatus"
import type { IdentityVerificationTimeRangeField } from "./../identityVerification/IdentityVerificationTimeRangeField"
import type { PgCompany } from "./../common/PgCompany"
import type { PgProvider } from "./../common/PgProvider"
import type { PortOneVersion } from "./../common/PortOneVersion"
/** 본인인증 다건 조회를 위한 입력 정보 */
export type IdentityVerificationFilterInput = {
	/**
	 * 상점 아이디
	 *
	 * Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 본인인증 내역을 조회합니다.
	 */
	storeId?: string
	/**
	 * 조회 기준 시점 유형
	 *
	 * 값을 입력하지 않으면 REQUESTED_AT으로 설정됩니다.
	 */
	timeRangeField?: IdentityVerificationTimeRangeField
	/**
	 * 조회 기준 시점 범위의 시작
	 *
	 * 값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
	 * (RFC 3339 date-time)
	 */
	from?: string
	/**
	 * 조회 기준 시점 범위의 끝
	 *
	 * 값을 입력하지 않으면 현재 시점으로 설정됩니다.
	 * (RFC 3339 date-time)
	 */
	until?: string
	/**
	 * 고객사 본인인증 번호
	 *
	 * V1 본인인증 건의 경우 `imp_uid`에 대응됩니다.
	 */
	identityVerificationId?: string
	/**
	 * 포트원 본인인증 시도 번호
	 *
	 * V1 본인인증 건의 경우 `imp_uid`에 대응됩니다.
	 */
	identityVerificationTxId?: string
	/** 테스트 결제 필터링 */
	isTest?: boolean
	/**
	 * 본인인증 상태 리스트
	 *
	 * 값을 입력하지 않으면 필터링이 적용되지 않습니다.
	 */
	statuses?: IdentityVerificationStatus[]
	/** PG사 본인인증 번호 */
	pgTxId?: string
	/** PG 상점아이디 */
	pgMerchantId?: string
	/**
	 * PG사 결제 모듈 리스트
	 *
	 * 값을 입력하지 않으면 PG사 결제 모듈 필터링이 적용되지 않습니다.
	 */
	pgProviders?: PgProvider[]
	/**
	 * PG사 리스트
	 *
	 * 값을 입력하지 않으면 PG사 필터링이 적용되지 않습니다.
	 */
	pgCompanies?: PgCompany[]
	/** 통신사 리스트 */
	carriers?: Carrier[]
	/** 포트원 버전 */
	version?: PortOneVersion
	/**
	 * 고객 정보
	 *
	 * 인증이 완료되지 않은 본인인증 내역의 경우 요청 시 고객 정보로, 인증이 완료된 본인인증 내역의 경우 인증된 고객 정보로 필터링합니다.
	 */
	customer?: IdentityVerificationFilterCustomerInput
}
