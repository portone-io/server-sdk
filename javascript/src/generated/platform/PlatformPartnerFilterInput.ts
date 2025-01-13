import type { Bank } from "./../common/Bank"
import type { Currency } from "./../common/Currency"
import type { PlatformAccountStatus } from "./../platform/PlatformAccountStatus"
import type { PlatformPartnerBusinessStatus } from "./../platform/PlatformPartnerBusinessStatus"
import type { PlatformPartnerFilterInputKeyword } from "./../platform/PlatformPartnerFilterInputKeyword"
import type { PlatformPartnerMemberCompanyConnectionStatus } from "./../platform/PlatformPartnerMemberCompanyConnectionStatus"
import type { PlatformPartnerTaxationType } from "./../platform/PlatformPartnerTaxationType"
import type { PlatformPartnerTypeName } from "./../platform/PlatformPartnerTypeName"
/** 파트너 필터 입력 정보 */
export type PlatformPartnerFilterInput = {
	/**
	 * 보관 조회 여부
	 *
	 * true 이면 보관된 파트너를 조회하고, false 이면 보관되지 않은 파트너를 조회합니다. 기본값은 false 입니다.
	 */
	isArchived?: boolean
	/** 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 태그를 하나 이상 가지는 파트너만 조회합니다. */
	tags?: string[]
	/**
	 * 은행
	 *
	 * 하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 계좌 은행을 가진 파트너만 조회합니다.
	 */
	banks?: Bank[]
	/**
	 * 통화 단위
	 *
	 * 하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 계좌 통화를 가진 파트너만 조회합니다.
	 */
	accountCurrencies?: Currency[]
	/** 하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 아이디를 가진 파트너만 조회합니다. */
	ids?: string[]
	/** 하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 기본 계약 id를 가진 파트너만 조회합니다. */
	contractIds?: string[]
	/**
	 * 플랫폼 계좌 상태
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 계좌 상태를 가진 파트너만 조회합니다.
	 */
	accountStatuses?: PlatformAccountStatus[]
	/**
	 * 플랫폼 파트너 사업자 상태
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 사업자 상태를 가진 파트너만 조회합니다.
	 */
	businessStatuses?: PlatformPartnerBusinessStatus[]
	/**
	 * 플랫폼 파트너 유형 이름
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 사업자 유형을 가진 파트너만 조회합니다.
	 */
	types?: PlatformPartnerTypeName[]
	/**
	 * 플랫폼 파트너 과세 유형
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 과세 유형을 가진 파트너만 조회합니다.
	 */
	taxationTypes?: PlatformPartnerTaxationType[]
	/**
	 * 플랫폼 파트너 연동 사업자 연결 상태
	 *
	 * 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 연동 사업자 연결 상태를 가진 파트너만 조회합니다.
	 */
	memberCompanyConnectionStatuses?: PlatformPartnerMemberCompanyConnectionStatus[]
	/** 검색 키워드 */
	keyword?: PlatformPartnerFilterInputKeyword
}
