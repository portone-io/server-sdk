export type * from "./ArchivePlatformAdditionalFeePolicyError"
export type * from "./ArchivePlatformAdditionalFeePolicyResponse"
export type * from "./ArchivePlatformContractError"
export type * from "./ArchivePlatformContractResponse"
export type * from "./ArchivePlatformDiscountSharePolicyError"
export type * from "./ArchivePlatformDiscountSharePolicyResponse"
export type * from "./CreatePlatformAdditionalFeePolicyBody"
export type * from "./CreatePlatformAdditionalFeePolicyError"
export type * from "./CreatePlatformAdditionalFeePolicyResponse"
export type * from "./CreatePlatformContractBody"
export type * from "./CreatePlatformContractError"
export type * from "./CreatePlatformContractResponse"
export type * from "./CreatePlatformDiscountSharePolicyBody"
export type * from "./CreatePlatformDiscountSharePolicyError"
export type * from "./CreatePlatformDiscountSharePolicyResponse"
export type * from "./GetPlatformAdditionalFeePoliciesBody"
export type * from "./GetPlatformAdditionalFeePoliciesError"
export type * from "./GetPlatformAdditionalFeePoliciesResponse"
export type * from "./GetPlatformAdditionalFeePolicyError"
export type * from "./GetPlatformContractError"
export type * from "./GetPlatformContractsBody"
export type * from "./GetPlatformContractsError"
export type * from "./GetPlatformContractsResponse"
export type * from "./GetPlatformDiscountSharePoliciesBody"
export type * from "./GetPlatformDiscountSharePoliciesError"
export type * from "./GetPlatformDiscountSharePoliciesResponse"
export type * from "./GetPlatformDiscountSharePolicyError"
export type * from "./PlatformAdditionalFeePolicyAlreadyExistsError"
export type * from "./PlatformAdditionalFeePolicyFilterInput"
export type * from "./PlatformAdditionalFeePolicyFilterInputKeyword"
export type * from "./PlatformArchivedDiscountSharePolicyError"
export type * from "./PlatformCannotArchiveScheduledAdditionalFeePolicyError"
export type * from "./PlatformCannotArchiveScheduledContractError"
export type * from "./PlatformCannotArchiveScheduledDiscountSharePolicyError"
export type * from "./PlatformContractAlreadyExistsError"
export type * from "./PlatformContractFilterInput"
export type * from "./PlatformContractFilterInputKeyword"
export type * from "./PlatformDiscountSharePolicyAlreadyExistsError"
export type * from "./PlatformDiscountSharePolicyFilterInput"
export type * from "./PlatformDiscountSharePolicyFilterInputKeyword"
export type * from "./PlatformSettlementCycleType"
export type * from "./RecoverPlatformAdditionalFeePolicyError"
export type * from "./RecoverPlatformAdditionalFeePolicyResponse"
export type * from "./RecoverPlatformContractError"
export type * from "./RecoverPlatformContractResponse"
export type * from "./RecoverPlatformDiscountSharePolicyError"
export type * from "./RecoverPlatformDiscountSharePolicyResponse"
export type * from "./UpdatePlatformAdditionalFeePolicyError"
export type * from "./UpdatePlatformAdditionalFeePolicyResponse"
export type * from "./UpdatePlatformContractError"
export type * from "./UpdatePlatformContractResponse"
export type * from "./UpdatePlatformDiscountSharePolicyError"
export type * from "./UpdatePlatformDiscountSharePolicyResponse"
import type { ArchivePlatformAdditionalFeePolicyResponse } from "#generated/platform/policy/ArchivePlatformAdditionalFeePolicyResponse"
import type { ArchivePlatformContractResponse } from "#generated/platform/policy/ArchivePlatformContractResponse"
import type { ArchivePlatformDiscountSharePolicyResponse } from "#generated/platform/policy/ArchivePlatformDiscountSharePolicyResponse"
import type { CreatePlatformAdditionalFeePolicyResponse } from "#generated/platform/policy/CreatePlatformAdditionalFeePolicyResponse"
import type { CreatePlatformContractResponse } from "#generated/platform/policy/CreatePlatformContractResponse"
import type { CreatePlatformDiscountSharePolicyResponse } from "#generated/platform/policy/CreatePlatformDiscountSharePolicyResponse"
import type { GetPlatformAdditionalFeePoliciesResponse } from "#generated/platform/policy/GetPlatformAdditionalFeePoliciesResponse"
import type { GetPlatformContractsResponse } from "#generated/platform/policy/GetPlatformContractsResponse"
import type { GetPlatformDiscountSharePoliciesResponse } from "#generated/platform/policy/GetPlatformDiscountSharePoliciesResponse"
import type { PageInput } from "#generated/common/PageInput"
import type { PlatformAdditionalFeePolicy } from "#generated/platform/PlatformAdditionalFeePolicy"
import type { PlatformAdditionalFeePolicyFilterInput } from "#generated/platform/policy/PlatformAdditionalFeePolicyFilterInput"
import type { PlatformContract } from "#generated/platform/PlatformContract"
import type { PlatformContractFilterInput } from "#generated/platform/policy/PlatformContractFilterInput"
import type { PlatformDiscountSharePolicy } from "#generated/platform/PlatformDiscountSharePolicy"
import type { PlatformDiscountSharePolicyFilterInput } from "#generated/platform/policy/PlatformDiscountSharePolicyFilterInput"
import type { PlatformFeeInput } from "#generated/platform/PlatformFeeInput"
import type { PlatformPayer } from "#generated/platform/PlatformPayer"
import type { PlatformSettlementCycleInput } from "#generated/platform/PlatformSettlementCycleInput"
import type { RecoverPlatformAdditionalFeePolicyResponse } from "#generated/platform/policy/RecoverPlatformAdditionalFeePolicyResponse"
import type { RecoverPlatformContractResponse } from "#generated/platform/policy/RecoverPlatformContractResponse"
import type { RecoverPlatformDiscountSharePolicyResponse } from "#generated/platform/policy/RecoverPlatformDiscountSharePolicyResponse"
import type { UpdatePlatformAdditionalFeePolicyResponse } from "#generated/platform/policy/UpdatePlatformAdditionalFeePolicyResponse"
import type { UpdatePlatformContractResponse } from "#generated/platform/policy/UpdatePlatformContractResponse"
import type { UpdatePlatformDiscountSharePolicyResponse } from "#generated/platform/policy/UpdatePlatformDiscountSharePolicyResponse"

export type Operations = {
	/**
	 * 할인 분담 정책 다건 조회
	 *
	 * 여러 할인 분담을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformDiscountSharePolicies: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: PageInput,
			/** 조회할 할인 분담 정책 조건 필터 */
			filter?: PlatformDiscountSharePolicyFilterInput,
		}
	) => Promise<GetPlatformDiscountSharePoliciesResponse>
	/**
	 * 할인 분담 정책 생성
	 *
	 * 새로운 할인 분담을 생성합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyAlreadyExistsError} PlatformDiscountSharePolicyAlreadyExistsError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createPlatformDiscountSharePolicy: (
		options: {
			/**
			 * 할인 분담에 부여할 고유 아이디
			 *
			 * 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
			 */
			id?: string,
			/** 할인 분담에 부여할 이름 */
			name: string,
			/**
			 * 파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
			 * (int32)
			 */
			partnerShareRate: number,
			/** 해당 할인 분담에 대한 메모 ex) 파트너 브랜드 쿠폰 */
			memo?: string,
		}
	) => Promise<CreatePlatformDiscountSharePolicyResponse>
	/**
	 * 할인 분담 정책 조회
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyNotFoundError} PlatformDiscountSharePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformDiscountSharePolicy: (
		/** 조회할 할인 분담 정책 아이디 */
		id: string,
	) => Promise<PlatformDiscountSharePolicy>
	/**
	 * 할인 분담 정책 수정
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 업데이트합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformArchivedDiscountSharePolicyError} 보관된 할인 분담 정책을 업데이트하려고 하는 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyNotFoundError} PlatformDiscountSharePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	updatePlatformDiscountSharePolicy: (
		options: {
			/** 업데이트할 할인 분담 정책 아이디 */
			id: string,
			/** 할인 분담 정책 이름 */
			name?: string,
			/**
			 * 할인 분담율
			 *
			 * 파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
			 * (int32)
			 */
			partnerShareRate?: number,
			/** 해당 할인 분담에 대한 메모 */
			memo?: string,
		}
	) => Promise<UpdatePlatformDiscountSharePolicyResponse>
	/**
	 * 할인 분담 정책 보관
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 보관합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformCannotArchiveScheduledDiscountSharePolicyError} 예약된 업데이트가 있는 할인 분담 정책을 보관하려고 하는 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyNotFoundError} PlatformDiscountSharePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	archivePlatformDiscountSharePolicy: (
		/** 할인 분담 아이디 */
		id: string,
	) => Promise<ArchivePlatformDiscountSharePolicyResponse>
	/**
	 * 할인 분담 정책 복원
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 복원합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyNotFoundError} PlatformDiscountSharePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	recoverPlatformDiscountSharePolicy: (
		/** 할인 분담 아이디 */
		id: string,
	) => Promise<RecoverPlatformDiscountSharePolicyResponse>
	/**
	 * 추가 수수료 정책 다건 조회
	 *
	 * 여러 추가 수수료 정책을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformAdditionalFeePolicies: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: PageInput,
			/** 조회할 추가 수수료 정책 조건 필터 */
			filter?: PlatformAdditionalFeePolicyFilterInput,
		}
	) => Promise<GetPlatformAdditionalFeePoliciesResponse>
	/**
	 * 추가 수수료 정책 생성
	 *
	 * 새로운 추가 수수료 정책을 생성합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePolicyAlreadyExistsError} PlatformAdditionalFeePolicyAlreadyExistsError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createPlatformAdditionalFeePolicy: (
		options: {
			/**
			 * 생성할 추가 수수료 정책 아이디
			 *
			 * 명시하지 않으면 id 가 임의로 생성됩니다.
			 */
			id?: string,
			/** 이름 */
			name: string,
			/** 수수료 정보 */
			fee: PlatformFeeInput,
			/** 메모 */
			memo?: string,
			/** 부가세 부담 주체 */
			vatPayer: PlatformPayer,
		}
	) => Promise<CreatePlatformAdditionalFeePolicyResponse>
	/**
	 * 추가 수수료 정책 조회
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePolicyNotFoundError} PlatformAdditionalFeePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformAdditionalFeePolicy: (
		/** 조회할 추가 수수료 정책 아이디 */
		id: string,
	) => Promise<PlatformAdditionalFeePolicy>
	/**
	 * 추가 수수료 정책 수정
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 업데이트합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePolicyNotFoundError} PlatformAdditionalFeePolicyNotFoundError
	 * @throws {@link Errors.PlatformArchivedAdditionalFeePolicyError} 보관된 추가 수수료 정책을 업데이트하려고 하는 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	updatePlatformAdditionalFeePolicy: (
		options: {
			/** 업데이트할 추가 수수료 정책 아이디 */
			id: string,
			/** 책정 수수료 */
			fee?: PlatformFeeInput,
			/** 추가 수수료 정책 이름 */
			name?: string,
			/** 해당 추가 수수료 정책에 대한 메모 */
			memo?: string,
			/** 부가세를 부담할 주체 */
			vatPayer?: PlatformPayer,
		}
	) => Promise<UpdatePlatformAdditionalFeePolicyResponse>
	/**
	 * 추가 수수료 정책 보관
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 보관합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePolicyNotFoundError} PlatformAdditionalFeePolicyNotFoundError
	 * @throws {@link Errors.PlatformCannotArchiveScheduledAdditionalFeePolicyError} 예약된 업데이트가 있는 추가 수수료 정책을 보관하려고 하는 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	archivePlatformAdditionalFeePolicy: (
		/** 추가 수수료 정책 아이디 */
		id: string,
	) => Promise<ArchivePlatformAdditionalFeePolicyResponse>
	/**
	 * 추가 수수료 정책 복원
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 복원합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePolicyNotFoundError} PlatformAdditionalFeePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	recoverPlatformAdditionalFeePolicy: (
		/** 추가 수수료 정책 아이디 */
		id: string,
	) => Promise<RecoverPlatformAdditionalFeePolicyResponse>
	/**
	 * 계약 다건 조회
	 *
	 * 여러 계약을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformContracts: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: PageInput,
			/** 조회할 계약 조건 필터 */
			filter?: PlatformContractFilterInput,
		}
	) => Promise<GetPlatformContractsResponse>
	/**
	 * 계약 생성
	 *
	 * 새로운 계약을 생성합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformContractAlreadyExistsError} PlatformContractAlreadyExistsError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createPlatformContract: (
		options: {
			/**
			 * 계약에 부여할 고유 아이디
			 *
			 * 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
			 */
			id?: string,
			/** 계약 이름 */
			name: string,
			/** 계약 내부 표기를 위한 메모 */
			memo?: string,
			/** 중개수수료 */
			platformFee: PlatformFeeInput,
			/** 정산 주기 */
			settlementCycle: PlatformSettlementCycleInput,
			/** 중개수수료에 대한 부가세 부담 주체 */
			platformFeeVatPayer: PlatformPayer,
			/** 정산 시 결제금액 부가세 감액 여부 */
			subtractPaymentVatAmount: boolean,
		}
	) => Promise<CreatePlatformContractResponse>
	/**
	 * 계약 조회
	 *
	 * 주어진 아이디에 대응되는 계약을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformContract: (
		/** 조회할 계약 아이디 */
		id: string,
	) => Promise<PlatformContract>
	/**
	 * 계약 수정
	 *
	 * 주어진 아이디에 대응되는 계약을 업데이트합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformArchivedContractError} 보관된 계약을 업데이트하려고 하는 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	updatePlatformContract: (
		options: {
			/** 업데이트할 계약 아이디 */
			id: string,
			/** 계약 이름 */
			name?: string,
			/** 계약 내부 표기를 위한 메모 */
			memo?: string,
			/** 중개수수료 */
			platformFee?: PlatformFeeInput,
			/** 정산 주기 */
			settlementCycle?: PlatformSettlementCycleInput,
			/** 중개수수료에 대한 부가세 부담 주체 */
			platformFeeVatPayer?: PlatformPayer,
			/** 정산 시 결제금액 부가세 감액 여부 */
			subtractPaymentVatAmount?: boolean,
		}
	) => Promise<UpdatePlatformContractResponse>
	/**
	 * 계약 보관
	 *
	 * 주어진 아이디에 대응되는 계약을 보관합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformCannotArchiveScheduledContractError} 예약된 업데이트가 있는 계약을 보관하려고 하는 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	archivePlatformContract: (
		/** 계약 아이디 */
		id: string,
	) => Promise<ArchivePlatformContractResponse>
	/**
	 * 계약 복원
	 *
	 * 주어진 아이디에 대응되는 계약을 복원합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	recoverPlatformContract: (
		/** 계약 아이디 */
		id: string,
	) => Promise<RecoverPlatformContractResponse>
}
