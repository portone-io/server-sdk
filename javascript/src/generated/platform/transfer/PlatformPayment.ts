import type { PlatformExternalPayment } from "./../../platform/transfer/PlatformExternalPayment"
import type { PlatformPortOnePayment } from "./../../platform/transfer/PlatformPortOnePayment"

/** 결제 정보 */
export type PlatformPayment =
	/** 외부 결제 정보 */
	| PlatformExternalPayment
	/** 포트원 결제 정보 */
	| PlatformPortOnePayment
