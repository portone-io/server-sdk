import type { B2bCounterpartyBusinessStatus } from "./../../b2b/counterparty/B2bCounterpartyBusinessStatus"
import type { B2bCounterpartyContact } from "./../../b2b/counterparty/B2bCounterpartyContact"
import type { B2bCounterpartyVerification } from "./../../b2b/counterparty/B2bCounterpartyVerification"
import type { B2bNtsConnectionStatus } from "./../../b2b/counterparty/B2bNtsConnectionStatus"
/**
 * 거래처
 *
 * B2B 거래처 정보입니다.
 */
export type B2bCounterparty = {
	/** 거래처 고유 아이디 */
	id: string
	graphqlId: string
	/** 테스트 모드 여부 */
	isForTest: boolean
	/**
	 * 사업자등록번호
	 *
	 * `-` 없이 숫자로만 구성됩니다.
	 */
	brn: string
	/** 상호명 */
	companyName: string
	/** 대표자 성명 */
	representativeName: string
	/** 주소 */
	address?: string
	/** 업태 */
	businessType?: string
	/** 업종 */
	businessClass?: string
	/** 담당자 정보 */
	contact: B2bCounterpartyContact
	/**
	 * 추가 담당자 목록
	 *
	 * 최대 5명까지 등록할 수 있습니다.
	 */
	additionalContacts: B2bCounterpartyContact[]
	/** 메모 */
	memo?: string
	/** 국세청 연동 상태 */
	ntsConnectionStatus: B2bNtsConnectionStatus
	/**
	 * 국세청 연동 시각
	 * (RFC 3339 date-time)
	 */
	ntsConnectedAt?: string
	/** 국세청 연동 실패 사유 */
	ntsConnectionFailedReason?: string
	/**
	 * 파트너 연동 ID
	 *
	 * 파트너 연동 거래처인 경우에만 존재합니다.
	 */
	partnerId?: string
	/** 휴폐업 상태 */
	businessStatus?: B2bCounterpartyBusinessStatus
	/**
	 * 휴폐업 상태 확인 시각
	 * (RFC 3339 date-time)
	 */
	businessStatusCheckedAt?: string
	/** 휴폐업 상태 검증 정보 */
	businessStatusVerification?: B2bCounterpartyVerification
	/** 사업자 정보 검증 정보 */
	businessInfoVerification?: B2bCounterpartyVerification
	/**
	 * 적용 시각
	 * (RFC 3339 date-time)
	 */
	appliedAt?: string
}
