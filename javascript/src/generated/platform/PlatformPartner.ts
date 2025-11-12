import type { PlatformAccount } from "./../platform/PlatformAccount"
import type { PlatformContact } from "./../platform/PlatformContact"
import type { PlatformPartnerStatus } from "./../platform/PlatformPartnerStatus"
import type { PlatformPartnerType } from "./../platform/PlatformPartnerType"
import type { PlatformProperties } from "./../platform/PlatformProperties"
/**
 * 파트너
 *
 * 파트너는 고객사가 정산해주어야 할 대상입니다.
 * 기본 사업자 정보와 정산정보, 그리고 적용될 계약의 정보를 등록 및 관리할 수 있습니다.
 */
export type PlatformPartner = {
	/** 파트너 고유 아이디 */
	id: string
	graphqlId: string
	/** 파트너 법인명 혹은 이름 */
	name: string
	/** 파트너 담당자 연락 정보 */
	contact: PlatformContact
	/** 정산 계좌 */
	account: PlatformAccount
	/** 파트너의 상태 */
	status: PlatformPartnerStatus
	/** 파트너에 설정된 기본 계약 아이디 */
	defaultContractId: string
	/** 파트너에 대한 메모 */
	memo?: string
	/** 파트너의 태그 리스트 */
	tags: string[]
	/** 파트너 유형별 정보 */
	type: PlatformPartnerType
	/** 보관 여부 */
	isArchived: boolean
	/**
	 * 변경 적용 시점
	 * (RFC 3339 date-time)
	 */
	appliedAt: string
	/** 사용자 정의 속성 */
	userDefinedProperties: PlatformProperties
	isForTest: boolean
}
