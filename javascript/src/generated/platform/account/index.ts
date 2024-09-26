export type * from "./GetPlatformAccountHolderError"
export type * from "./PlatformAccountHolder"
export type * from "./PlatformExternalApiFailedError"
export type * from "./PlatformExternalApiTemporarilyFailedError"
export type * from "./PlatformNotSupportedBankError"
import type { Bank } from "#generated/common/Bank"
import type { PlatformAccountHolder } from "#generated/platform/account/PlatformAccountHolder"

export type Operations = {
	/**
	 * 예금주 조회
	 *
	 * 계좌의 예금주를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformExternalApiFailedError} 외부 api 오류
	 * @throws {@link Errors.PlatformExternalApiTemporarilyFailedError} 외부 api의 일시적인 오류
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformNotSupportedBankError} 지원하지 않는 은행인 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformAccountHolder: (
		options: {
			/** 은행 */
			bank: Bank,
			/** '-'를 제외한 계좌 번호 */
			accountNumber: string,
			/**
			 * 생년월일
			 *
			 * 실명 조회를 위해 추가로 보낼 수 있습니다. birthdate과 businessRegistrationNumber 중 하나만 사용해야 합니다.
			 */
			birthdate?: string,
			/**
			 * 사업자등록번호
			 *
			 * 실명 조회를 위해 추가로 보낼 수 있습니다. birthdate과 businessRegistrationNumber 중 하나만 사용해야 합니다.
			 */
			businessRegistrationNumber?: string,
		}
	) => Promise<PlatformAccountHolder>
}
