import type { Unrecognized } from "./../../utils/unrecognized"
import type { FailedIdentityVerification } from "./../identityVerification/FailedIdentityVerification"
import type { ReadyIdentityVerification } from "./../identityVerification/ReadyIdentityVerification"
import type { VerifiedIdentityVerification } from "./../identityVerification/VerifiedIdentityVerification"
/** 본인인증 내역 */
export type IdentityVerification =
	/** 실패한 본인인증 내역 */
	| FailedIdentityVerification
	/** 준비 상태의 본인인증 내역 */
	| ReadyIdentityVerification
	/** 완료된 본인인증 내역 */
	| VerifiedIdentityVerification
	| { readonly status: Unrecognized }

export function isUnrecognizedIdentityVerification(entity: IdentityVerification): entity is { readonly status: Unrecognized } {
	return entity.status !== "FAILED"
		&& entity.status !== "READY"
		&& entity.status !== "VERIFIED"
}
