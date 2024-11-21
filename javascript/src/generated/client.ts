import type { PortOneClientInit } from "../client"
import { AuthClient } from "./auth/client"
import { PlatformClient } from "./platform/client"
import { IdentityVerificationClient } from "./identityVerification/client"
import { PaymentClient } from "./payment/client"
import { PgSpecificClient } from "./pgSpecific/client"
export function PortOneClient(init: PortOneClientInit): PortOneClient {
	return {
		auth: AuthClient(init),
		platform: PlatformClient(init),
		identityVerification: IdentityVerificationClient(init),
		payment: PaymentClient(init),
		pgSpecific: PgSpecificClient(init),
	}
}
export type PortOneClient = {
	auth: AuthClient
	platform: PlatformClient
	identityVerification: IdentityVerificationClient
	payment: PaymentClient
	pgSpecific: PgSpecificClient
}
