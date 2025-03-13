import type { PortOneClientInit } from "../client"
import { AuthClient } from "./auth/client"
import { PlatformClient } from "./platform/client"
import { IdentityVerificationClient } from "./identityVerification/client"
import { PaymentClient } from "./payment/client"
import { B2BClient } from "./b2B/client"
import { PgSpecificClient } from "./pgSpecific/client"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function PortOneClient(init: PortOneClientInit): PortOneClient {
	return {
		auth: AuthClient(init),
		platform: PlatformClient(init),
		identityVerification: IdentityVerificationClient(init),
		payment: PaymentClient(init),
		b2B: B2BClient(init),
		pgSpecific: PgSpecificClient(init),
	}
}
export type PortOneClient = {
	auth: AuthClient
	platform: PlatformClient
	identityVerification: IdentityVerificationClient
	payment: PaymentClient
	b2B: B2BClient
	pgSpecific: PgSpecificClient
}
