import type { FailedIdentityVerification } from "#generated/identityVerification/FailedIdentityVerification"
import type { ReadyIdentityVerification } from "#generated/identityVerification/ReadyIdentityVerification"
import type { VerifiedIdentityVerification } from "#generated/identityVerification/VerifiedIdentityVerification"

/** 본인인증 내역 */
export type IdentityVerification =
	/** 실패한 본인인증 내역 */
	| FailedIdentityVerification
	/** 준비 상태의 본인인증 내역 */
	| ReadyIdentityVerification
	/** 완료된 본인인증 내역 */
	| VerifiedIdentityVerification
