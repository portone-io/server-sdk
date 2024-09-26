/**
 * 파트너 검색 키워드 입력 정보
 *
 * 검색 키워드 적용을 위한 옵션으로, 명시된 키워드를 포함하는 파트너만 조회합니다. 하나의 하위 필드에만 값을 명시하여 요청합니다.
 */
export type PlatformPartnerFilterInputKeyword = {
	/** 해당 값이 포함된 id 를 가진 파트너만 조회합니다. */
	id?: string
	/** 해당 값이 포함된 이름 을 가진 파트너만 조회합니다. */
	name?: string
	/** 해당 값이 포함된 이메일 주소를 가진 파트너만 조회합니다. */
	email?: string
	/** 해당 값이 포함된 사업자등록번호를 가진 파트너만 조회합니다. */
	businessRegistrationNumber?: string
	/** 해당 값이 포함된 기본 계약 아이디를 가진 파트너만 조회합니다. */
	defaultContractId?: string
	/** 해당 값이 포함된 메모를 가진 파트너만 조회합니다. */
	memo?: string
	/** 해당 값이 포함된 계좌번호를 가진 파트너만 조회합니다. */
	accountNumber?: string
	/** 해당 값이 포함된 계좌 예금주명을 가진 파트너만 조회합니다. */
	accountHolder?: string
}
