import type { PlatformProperties } from "#generated/platform/PlatformProperties"
import type { UpdatePlatformPartnerBodyAccount } from "#generated/platform/UpdatePlatformPartnerBodyAccount"
import type { UpdatePlatformPartnerBodyContact } from "#generated/platform/UpdatePlatformPartnerBodyContact"
import type { UpdatePlatformPartnerBodyType } from "#generated/platform/UpdatePlatformPartnerBodyType"

/**
 * 파트너 업데이트를 위한 입력 정보
 *
 * 값이 명시되지 않은 필드는 업데이트되지 않습니다.
 */
export type UpdatePlatformPartnerBody = {
	/** 파트너 법인명 혹은 이름 */
	name?: string
	/** 파트너 담당자 연락 정보 */
	contact?: UpdatePlatformPartnerBodyContact
	/** 정산 계좌 */
	account?: UpdatePlatformPartnerBodyAccount
	/** 파트너에 설정된 기본 계약 아이디 */
	defaultContractId?: string
	/** 파트너에 대한 메모 */
	memo?: string
	/** 파트너의 태그 리스트 */
	tags?: string[]
	/** 파트너 유형별 정보 */
	type?: UpdatePlatformPartnerBodyType
	/** 사용자 정의 속성 */
	userDefinedProperties?: PlatformProperties
}
