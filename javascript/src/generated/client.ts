import * as Errors from "./errors"
import * as Analytics from "./analytics"
import * as Auth from "./auth"
import * as B2B from "./b2b"
import * as Common from "./common"
import * as IdentityVerification from "./identityVerification"
import * as Payment from "./payment"
import * as PgSpecific from "./pgSpecific"
import * as Platform from "./platform"

export type PortOneClientInit = {
  /**
	 * 포트원 API URL Origin
	 *
	 * 기본값은 `https://api.portone.io`입니다.
	 */
	baseUrl?: string;
	/**
	 * 상점 ID
	 */
	storeId?: string;
}

/**
 * API Secret을 사용해 포트원 API 클라이언트를 생성합니다.
 */
export function PortOneClient(
  /** 포트원 API Secret */
  secret: string,
  /** 포트원 API를 사용하기 위한 추가 정보 */
  init?: PortOneClientInit,
): PortOneClient {
	const baseUrl = init?.baseUrl ?? "https://api.portone.io"
	const storeId = init?.storeId
	const userAgent = "__USER_AGENT__"
	return {
		auth: Auth.AuthClient(secret, userAgent, baseUrl, storeId),
		platform: Platform.PlatformClient(secret, userAgent, baseUrl, storeId),
		identityVerification: IdentityVerification.IdentityVerificationClient(secret, userAgent, baseUrl, storeId),
		payment: Payment.PaymentClient(secret, userAgent, baseUrl, storeId),
		analytics: Analytics.AnalyticsClient(secret, userAgent, baseUrl, storeId),
		b2b: B2B.B2BClient(secret, userAgent, baseUrl, storeId),
		pgSpecific: PgSpecific.PgSpecificClient(secret, userAgent, baseUrl, storeId),
	}
}

export type PortOneClient = {
	auth: Auth.AuthClient
	platform: Platform.PlatformClient
	identityVerification: IdentityVerification.IdentityVerificationClient
	payment: Payment.PaymentClient
	analytics: Analytics.AnalyticsClient
	b2b: B2B.B2BClient
	pgSpecific: PgSpecific.PgSpecificClient
}
