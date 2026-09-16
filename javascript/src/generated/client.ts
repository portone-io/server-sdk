import type { PortOneClientInit } from "../client"
import { B2bClient } from "./b2b/client"
import { PlatformClient } from "./platform/client"
import { PaymentClient } from "./payment/client"
import { CheckoutProfileClient } from "./checkoutProfile/client"
import { IdentityVerificationClient } from "./identityVerification/client"
import { PgSpecificClient } from "./pgSpecific/client"
import { AuthClient } from "./auth/client"
import { ReconciliationClient } from "./reconciliation/client"
import { PaymentSessionClient } from "./paymentSession/client"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function PortOneClient(init: PortOneClientInit): PortOneClient {
	return {
		b2b: B2bClient(init),
		platform: PlatformClient(init),
		payment: PaymentClient(init),
		checkoutProfile: CheckoutProfileClient(init),
		identityVerification: IdentityVerificationClient(init),
		pgSpecific: PgSpecificClient(init),
		auth: AuthClient(init),
		reconciliation: ReconciliationClient(init),
		paymentSession: PaymentSessionClient(init),
	}
}
export type PortOneClient = {
	b2b: B2bClient
	platform: PlatformClient
	payment: PaymentClient
	checkoutProfile: CheckoutProfileClient
	identityVerification: IdentityVerificationClient
	pgSpecific: PgSpecificClient
	auth: AuthClient
	reconciliation: ReconciliationClient
	paymentSession: PaymentSessionClient
}
