import type { CashReceiptStatus } from "./../../payment/cashReceipt/CashReceiptStatus"
import type { CashReceiptTimeRangeField } from "./../../payment/cashReceipt/CashReceiptTimeRangeField"
import type { PgCompany } from "./../../common/PgCompany"
import type { PgProvider } from "./../../common/PgProvider"
import type { PortOneVersion } from "./../../common/PortOneVersion"
/** 현금영수증 다건 조회를 위한 입력 정보 */
export type CashReceiptFilterInput = {
	/**
	 * 상점 아이디
	 *
	 * Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 현금영수증을 조회합니다.
	 */
	storeId?: string
	/**
	 * 조회 기준 시점 유형
	 *
	 * 값을 입력하지 않으면 ISSUED_AT으로 설정됩니다.
	 */
	timeRangeField?: CashReceiptTimeRangeField
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
	/** 고객사 결제 아이디 */
	paymentId?: string
	/** 테스트 결제 필터링 */
	isTest?: boolean
	/** 주문명 */
	orderName?: string
	/**
	 * 현금영수증 발급 상태 리스트
	 *
	 * 값을 입력하지 않으면 필터링이 적용되지 않습니다.
	 */
	statuses?: CashReceiptStatus[]
	/** 수동 발급 여부 */
	isManual?: boolean
	/** PG사 현금영수증 발급 번호 */
	pgReceiptId?: string
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
	/** 포트원 버전 */
	version?: PortOneVersion
}
