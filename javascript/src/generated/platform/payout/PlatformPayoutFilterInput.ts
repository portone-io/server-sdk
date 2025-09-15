import type { Bank } from "./../../common/Bank"
import type { Currency } from "./../../common/Currency"
import type { PlatformPartnerTaxationType } from "./../../platform/PlatformPartnerTaxationType"
import type { PlatformPartnerTypeName } from "./../../platform/PlatformPartnerTypeName"
import type { PlatformPayoutFilterInputCriteria } from "./../../platform/payout/PlatformPayoutFilterInputCriteria"
import type { PlatformPayoutSettlementStatementStatus } from "./../../platform/payout/PlatformPayoutSettlementStatementStatus"
import type { PlatformPayoutStatus } from "./../../platform/payout/PlatformPayoutStatus"
import type { PlatformPayoutTaxInvoiceStatus } from "./../../platform/payout/PlatformPayoutTaxInvoiceStatus"
/** 지급 내역 필터 입력 정보 */
export type PlatformPayoutFilterInput = {
	/**
	 * 지급 상태
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 지급 상태를 가진 지급 내역을 조회합니다.
	 */
	statuses?: PlatformPayoutStatus[]
	/**
	 * 파트너 아이디
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 파트너 아이디를 가진 지급 내역을 조회합니다.
	 */
	partnerIds?: string[]
	/** 조회 기준 */
	criteria: PlatformPayoutFilterInputCriteria
	/**
	 * 지급 계좌 은행
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 지급 계좌 은행을 가진 지급 내역을 조회합니다.
	 */
	payoutAccountBanks?: Bank[]
	/**
	 * 파트너 태그
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 파트너 태그를 하나 이상 가진 지급 내역을 조회합니다.
	 */
	partnerTags?: string[]
	/**
	 * 지급 통화
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 지급 통화를 가진 지급 내역을 조회합니다.
	 */
	payoutCurrencies?: Currency[]
	/**
	 * 지급 아이디
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 지급 아이디를 가진 지급 내역을 조회합니다.
	 */
	payoutIds?: string[]
	/**
	 * 세금계산서 상태
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 세금계산서 상태를 가진 지급 내역을 조회합니다.
	 */
	taxInvoiceStatuses?: PlatformPayoutTaxInvoiceStatus[]
	/**
	 * 파트너 유형
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 파트너 유형을 가진 지급 내역을 조회합니다.
	 */
	partnerTypes?: PlatformPartnerTypeName[]
	/**
	 * 파트너 과세 유형
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 파트너 과세 유형을 가진 지급 내역을 조회합니다.
	 */
	partnerTaxationTypes?: PlatformPartnerTaxationType[]
	/**
	 * 정산 내역서 상태
	 *
	 * 값이 존재하는 경우 해당 리스트에 포함되는 정산 내역서 상태를 가진 지급 내역을 조회합니다.
	 */
	settlementStatementStatuses?: PlatformPayoutSettlementStatementStatus[]
}
