import type { CreatePlatformPartnerBodyAccount } from "./../../platform/partner/CreatePlatformPartnerBodyAccount"
import type { CreatePlatformPartnerBodyContact } from "./../../platform/partner/CreatePlatformPartnerBodyContact"
import type { CreatePlatformPartnerBodyType } from "./../../platform/partner/CreatePlatformPartnerBodyType"
import type { PlatformProperties } from "./../../platform/PlatformProperties"
/** 파트너 생성을 위한 입력 정보 */
export type CreatePlatformPartnerBody = {
	/**
	 * 파트너에 부여할 고유 아이디
	 *
	 * 고객사 서버에 등록된 파트너 지칭 아이디와 동일하게 설정하는 것을 권장합니다. 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
	 */
	id?: string
	/** 파트너 법인명 혹은 이름 */
	name: string
	/** 파트너 담당자 연락 정보 */
	contact: CreatePlatformPartnerBodyContact
	/**
	 * 정산 계좌
	 *
	 * 파트너의 사업자등록번호가 존재하는 경우 명시합니다. 별도로 검증하지는 않으며, 번호와 기호 모두 입력 가능합니다.
	 */
	account: CreatePlatformPartnerBodyAccount
	/**
	 * 기본 계약 아이디
	 *
	 * 이미 존재하는 계약 아이디를 등록해야 합니다.
	 */
	defaultContractId: string
	/**
	 * 파트너에 대한 메모
	 *
	 * 총 256자까지 입력할 수 있습니다.
	 */
	memo?: string
	/**
	 * 파트너에 부여할 태그 리스트
	 *
	 * 최대 10개까지 입력할 수 있습니다.
	 */
	tags: string[]
	/**
	 * 파트너 유형별 추가 정보
	 *
	 * 사업자/원천징수 대상자 중 추가할 파트너의 유형에 따른 정보를 입력해야 합니다.
	 */
	type: CreatePlatformPartnerBodyType
	/** 사용자 정의 속성 */
	userDefinedProperties?: PlatformProperties
}
