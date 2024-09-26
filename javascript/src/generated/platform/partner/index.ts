export type * from "./ArchivePlatformPartnerError"
export type * from "./ArchivePlatformPartnerResponse"
export type * from "./CreatePlatformPartnerBody"
export type * from "./CreatePlatformPartnerBodyAccount"
export type * from "./CreatePlatformPartnerBodyContact"
export type * from "./CreatePlatformPartnerBodyType"
export type * from "./CreatePlatformPartnerBodyTypeBusiness"
export type * from "./CreatePlatformPartnerBodyTypeNonWhtPayer"
export type * from "./CreatePlatformPartnerBodyTypeWhtPayer"
export type * from "./CreatePlatformPartnerError"
export type * from "./CreatePlatformPartnerResponse"
export type * from "./CreatePlatformPartnersBody"
export type * from "./CreatePlatformPartnersError"
export type * from "./CreatePlatformPartnersResponse"
export type * from "./GetPlatformPartnerError"
export type * from "./GetPlatformPartnersBody"
export type * from "./GetPlatformPartnersError"
export type * from "./GetPlatformPartnersResponse"
export type * from "./PlatformCannotArchiveScheduledPartnerError"
export type * from "./PlatformContractsNotFoundError"
export type * from "./PlatformPartnerIdAlreadyExistsError"
export type * from "./PlatformPartnerIdsAlreadyExistError"
export type * from "./PlatformPartnerIdsDuplicatedError"
export type * from "./RecoverPlatformPartnerError"
export type * from "./RecoverPlatformPartnerResponse"
export type * from "./UpdatePlatformPartnerError"
export type * from "./UpdatePlatformPartnerResponse"
import type { ArchivePlatformPartnerResponse } from "#generated/platform/partner/ArchivePlatformPartnerResponse"
import type { CreatePlatformPartnerBody } from "#generated/platform/partner/CreatePlatformPartnerBody"
import type { CreatePlatformPartnerBodyAccount } from "#generated/platform/partner/CreatePlatformPartnerBodyAccount"
import type { CreatePlatformPartnerBodyContact } from "#generated/platform/partner/CreatePlatformPartnerBodyContact"
import type { CreatePlatformPartnerBodyType } from "#generated/platform/partner/CreatePlatformPartnerBodyType"
import type { CreatePlatformPartnerResponse } from "#generated/platform/partner/CreatePlatformPartnerResponse"
import type { CreatePlatformPartnersResponse } from "#generated/platform/partner/CreatePlatformPartnersResponse"
import type { GetPlatformPartnersResponse } from "#generated/platform/partner/GetPlatformPartnersResponse"
import type { PageInput } from "#generated/common/PageInput"
import type { PlatformPartner } from "#generated/platform/PlatformPartner"
import type { PlatformPartnerFilterInput } from "#generated/platform/PlatformPartnerFilterInput"
import type { PlatformProperties } from "#generated/platform/PlatformProperties"
import type { RecoverPlatformPartnerResponse } from "#generated/platform/partner/RecoverPlatformPartnerResponse"
import type { UpdatePlatformPartnerBodyAccount } from "#generated/platform/UpdatePlatformPartnerBodyAccount"
import type { UpdatePlatformPartnerBodyContact } from "#generated/platform/UpdatePlatformPartnerBodyContact"
import type { UpdatePlatformPartnerBodyType } from "#generated/platform/UpdatePlatformPartnerBodyType"
import type { UpdatePlatformPartnerResponse } from "#generated/platform/partner/UpdatePlatformPartnerResponse"

export type Operations = {
	/**
	 * 파트너 다건 조회
	 *
	 * 여러 파트너를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformPartners: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: PageInput,
			/** 조회할 파트너 조건 필터 */
			filter?: PlatformPartnerFilterInput,
		}
	) => Promise<GetPlatformPartnersResponse>
	/**
	 * 파트너 생성
	 *
	 * 새로운 파트너를 생성합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAccountVerificationAlreadyUsedError} 파트너 계좌 검증 아이디를 이미 사용한 경우
	 * @throws {@link Errors.PlatformAccountVerificationFailedError} 파트너 계좌 인증이 실패한 경우
	 * @throws {@link Errors.PlatformAccountVerificationNotFoundError} 파트너 계좌 검증 아이디를 찾을 수 없는 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformCurrencyNotSupportedError} 지원 되지 않는 통화를 선택한 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerIdAlreadyExistsError} PlatformPartnerIdAlreadyExistsError
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createPlatformPartner: (
		options: {
			/**
			 * 파트너에 부여할 고유 아이디
			 *
			 * 고객사 서버에 등록된 파트너 지칭 아이디와 동일하게 설정하는 것을 권장합니다. 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
			 */
			id?: string,
			/** 파트너 법인명 혹은 이름 */
			name: string,
			/** 파트너 담당자 연락 정보 */
			contact: CreatePlatformPartnerBodyContact,
			/**
			 * 정산 계좌
			 *
			 * 파트너의 사업자등록번호가 존재하는 경우 명시합니다. 별도로 검증하지는 않으며, 번호와 기호 모두 입력 가능합니다.
			 */
			account: CreatePlatformPartnerBodyAccount,
			/**
			 * 기본 계약 아이디
			 *
			 * 이미 존재하는 계약 아이디를 등록해야 합니다.
			 */
			defaultContractId: string,
			/**
			 * 파트너에 대한 메모
			 *
			 * 총 256자까지 입력할 수 있습니다.
			 */
			memo?: string,
			/**
			 * 파트너에 부여할 태그 리스트
			 *
			 * 최대 10개까지 입력할 수 있습니다.
			 */
			tags: string[],
			/**
			 * 파트너 유형별 추가 정보
			 *
			 * 사업자/원천징수 대상자 중 추가할 파트너의 유형에 따른 정보를 입력해야 합니다.
			 */
			type: CreatePlatformPartnerBodyType,
			/** 사용자 정의 속성 */
			userDefinedProperties?: PlatformProperties,
		}
	) => Promise<CreatePlatformPartnerResponse>
	/**
	 * 파트너 조회
	 *
	 * 파트너 객체를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformPartner: (
		/** 조회하고 싶은 파트너 아이디 */
		id: string,
	) => Promise<PlatformPartner>
	/**
	 * 파트너 수정
	 *
	 * 주어진 아이디에 대응되는 파트너 정보를 업데이트합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAccountVerificationAlreadyUsedError} 파트너 계좌 검증 아이디를 이미 사용한 경우
	 * @throws {@link Errors.PlatformAccountVerificationFailedError} 파트너 계좌 인증이 실패한 경우
	 * @throws {@link Errors.PlatformAccountVerificationNotFoundError} 파트너 계좌 검증 아이디를 찾을 수 없는 경우
	 * @throws {@link Errors.PlatformArchivedPartnerError} 보관된 파트너를 업데이트하려고 하는 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformInsufficientDataToChangePartnerTypeError} 파트너 타입 수정에 필요한 데이터가 부족한 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	updatePlatformPartner: (
		options: {
			/** 업데이트할 파트너 아이디 */
			id: string,
			/** 파트너 법인명 혹은 이름 */
			name?: string,
			/** 파트너 담당자 연락 정보 */
			contact?: UpdatePlatformPartnerBodyContact,
			/** 정산 계좌 */
			account?: UpdatePlatformPartnerBodyAccount,
			/** 파트너에 설정된 기본 계약 아이디 */
			defaultContractId?: string,
			/** 파트너에 대한 메모 */
			memo?: string,
			/** 파트너의 태그 리스트 */
			tags?: string[],
			/** 파트너 유형별 정보 */
			type?: UpdatePlatformPartnerBodyType,
			/** 사용자 정의 속성 */
			userDefinedProperties?: PlatformProperties,
		}
	) => Promise<UpdatePlatformPartnerResponse>
	/**
	 * 파트너 다건 생성
	 *
	 * 새로운 파트너를 다건 생성합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformContractsNotFoundError} PlatformContractsNotFoundError
	 * @throws {@link Errors.PlatformCurrencyNotSupportedError} 지원 되지 않는 통화를 선택한 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerIdsAlreadyExistError} PlatformPartnerIdsAlreadyExistError
	 * @throws {@link Errors.PlatformPartnerIdsDuplicatedError} PlatformPartnerIdsDuplicatedError
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createPlatformPartners: (
		/** 생성할 파트너 리스트 정보 */
		partners: CreatePlatformPartnerBody[],
	) => Promise<CreatePlatformPartnersResponse>
	/**
	 * 파트너 복원
	 *
	 * 주어진 아이디에 대응되는 파트너를 보관합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformCannotArchiveScheduledPartnerError} 예약된 업데이트가 있는 파트너를 보관하려고 하는 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	archivePlatformPartner: (
		/** 파트너 아이디 */
		id: string,
	) => Promise<ArchivePlatformPartnerResponse>
	/**
	 * 파트너 복원
	 *
	 * 주어진 아이디에 대응되는 파트너를 복원합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	recoverPlatformPartner: (
		/** 파트너 아이디 */
		id: string,
	) => Promise<RecoverPlatformPartnerResponse>
}
