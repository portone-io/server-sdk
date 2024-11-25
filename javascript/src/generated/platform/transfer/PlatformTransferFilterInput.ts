import type { DateRange } from "./../../platform/DateRange"
import type { PaymentMethodType } from "./../../common/PaymentMethodType"
import type { PlatformTransferFilterInputKeyword } from "./../../platform/transfer/PlatformTransferFilterInputKeyword"
import type { PlatformTransferStatus } from "./../../platform/transfer/PlatformTransferStatus"
import type { PlatformTransferType } from "./../../platform/transfer/PlatformTransferType"
/**
 * 정산건 필터 입력 정보
 *
 * 정산 시작일 범위와 정산 일 범위는 둘 중 하나만 입력 가능합니다.
 */
export type PlatformTransferFilterInput = {
	/** 정산 시작일 범위 */
	settlementStartDateRange?: DateRange
	/** 정산 일 범위 */
	settlementDateRange?: DateRange
	/**
	 * 파트너 태그 리스트
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 태그를 하나 이상 가지는 파트너에 대한 정산건만 조회합니다.
	 */
	partnerTags?: string[]
	/**
	 * 계약 아이디 리스트
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 계약 아이디를 가지는 정산건만 조회합니다.
	 */
	contractIds?: string[]
	/**
	 * 할인 분담 정책 아이디 리스트
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 할인 분담 정책 아이디를 하나 이상 가지는 정산건만 조회합니다.
	 */
	discountSharePolicyIds?: string[]
	/**
	 * 추가 수수료 정책 아이디 리스트
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 추가 수수료 아이디를 하나 이상 가지는 정산건만 조회합니다.
	 */
	additionalFeePolicyIds?: string[]
	/**
	 * 결제 수단 리스트
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 결제 수단을 가지는 파트너만 조회합니다.
	 */
	paymentMethodTypes?: PaymentMethodType[]
	/**
	 * 채널 키 리스트
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 채널 키를 가지는 정산건만 조회합니다.
	 */
	channelKeys?: string[]
	/**
	 * 정산 방식 리스트
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 정산 방식의 정산건만 조회합니다.
	 */
	types?: PlatformTransferType[]
	/**
	 * 정산 상태 리스트
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 정산 상태인 정산건만 조회합니다.
	 */
	statuses?: PlatformTransferStatus[]
	/** 검색 키워드 */
	keyword?: PlatformTransferFilterInputKeyword
	/** 테스트 모드 여부 */
	isForTest?: boolean
}
