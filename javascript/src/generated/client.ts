import type { PortOneClientInit } from "../client"
import { B2bClient } from "./b2b/client"
import { PlatformClient } from "./platform/client"
import { PaymentClient } from "./payment/client"
import { IdentityVerificationClient } from "./identityVerification/client"
import { PgSpecificClient } from "./pgSpecific/client"
import { AuthClient } from "./auth/client"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function PortOneClient(init: PortOneClientInit): PortOneClient {
	return {
		b2b: B2bClient(init),
		platform: PlatformClient(init),
		payment: PaymentClient(init),
		identityVerification: IdentityVerificationClient(init),
		pgSpecific: PgSpecificClient(init),
		auth: AuthClient(init),
	}
}
export type PortOneClient = {
	b2b: B2bClient
	platform: PlatformClient
	payment: PaymentClient
	identityVerification: IdentityVerificationClient
	pgSpecific: PgSpecificClient
	auth: AuthClient
}
