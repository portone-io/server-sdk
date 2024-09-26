import type { VerifiedIdentityVerification } from "#generated/identityVerification/VerifiedIdentityVerification"

/** 본인인증 확인 성공 응답 */
export type ConfirmIdentityVerificationResponse = {
	/** 완료된 본인인증 내역 */
	identityVerification: VerifiedIdentityVerification
}
