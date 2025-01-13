export * from "./generated/webhook";
import { PortOneError } from "./PortOneError";
import type { Webhook } from "./generated/webhook";
import { timingSafeEqual } from "./utils/timingSafeEqual";
import { tryCatch } from "./utils/try";

const WEBHOOK_TOLERANCE_IN_SECONDS = 5 * 60; // 5분

/**
 * SDK에 전달한 사용자 입력이 잘못되었을 경우에 발생하는 에러입니다.
 *
 * 해당 에러는 대부분 사용자의 실수로 발생합니다.
 * 에러가 발생하는 경우, 에러가 발생한 함수의 문서를 참고하여
 * 문제를 수정해주시기 바랍니다.
 */
export class InvalidInputError extends PortOneError {
	/** @ignore */
	constructor(message: string) {
		super(message);
		Object.setPrototypeOf(this, InvalidInputError.prototype);
		this.name = "InvalidInputError";
	}
}

/**
 * 웹훅 검증이 실패했을 때 발생하는 에러입니다.
 *
 * `reason` 필드를 통해 상세한 실패 원인을 확인할 수 있습니다.
 */
export class WebhookVerificationError extends PortOneError {
	/**
	 * 웹훅 검증이 실패한 상세 사유을 나타냅니다.
	 */
	readonly reason: WebhookVerificationFailureReason;

	/**
	 * 웹훅 검증 실패 사유로부터 에러 메시지를 생성합니다.
	 *
	 * @param reason 에러 메시지를 생성할 실패 사유
	 * @returns 에러 메시지
	 */
	static getMessage(reason: WebhookVerificationFailureReason): string {
		switch (reason) {
			case "MISSING_REQUIRED_HEADERS":
				return "필수 헤더가 누락되었습니다.";
			case "NO_MATCHING_SIGNATURE":
				return "올바른 웹훅 시그니처를 찾을 수 없습니다.";
			case "INVALID_SIGNATURE":
				return "웹훅 시그니처가 유효하지 않습니다.";
			case "TIMESTAMP_TOO_OLD":
				return "웹훅 시그니처의 타임스탬프가 만료 기한을 초과했습니다.";
			case "TIMESTAMP_TOO_NEW":
				return "웹훅 시그니처의 타임스탬프가 미래 시간으로 설정되어 있습니다.";
		}
	}

	/** @ignore */
	constructor(
		reason: WebhookVerificationFailureReason,
		options?: ErrorOptions,
	) {
		super(WebhookVerificationError.getMessage(reason), options);
		Object.setPrototypeOf(this, WebhookVerificationError.prototype);
		this.name = "WebhookVerificationError";
		this.reason = reason;
	}
}

/**
 * 웹훅 검증 실패 사유입니다.
 *
 * `WebhookVerificationError.getMessage()`에 전달하여 에러 메시지를 얻을 수 있습니다.
 */
export type WebhookVerificationFailureReason =
	| "MISSING_REQUIRED_HEADERS"
	| "NO_MATCHING_SIGNATURE"
	| "INVALID_SIGNATURE"
	| "TIMESTAMP_TOO_OLD"
	| "TIMESTAMP_TOO_NEW";

/**
 * 웹훅 요청에 필수적으로 포함되는 헤더들입니다.
 */
export interface WebhookUnbrandedRequiredHeaders {
	"webhook-id": string;
	"webhook-timestamp": string;
	"webhook-signature": string;
}

/**
 * 웹훅 인스턴스에서 사용할 옵션입니다.
 */
export interface WebhookOptions {
	/**
	 * 웹훅 시크릿의 포맷입니다.
	 *
	 * - `"raw"`인 경우, `secret` 파라미터의 값을 그대로 사용합니다.
	 * - 지정하지 않을 경우, `secret` 파라미터의 값을 base64 문자열로 간주합니다.
	 */
	format?: "raw";
}

const prefix = "whsec_";

/**
 * returns the value only when there is only one string entry with the name (case-insensitive)
 */
function findHeaderValue(headers: unknown, name: string): string | undefined {
	if (typeof headers !== "object" || headers === null) return undefined;

	const nameLowerCase = name.toLowerCase();

	let found: string | undefined = undefined;
	for (const [key, value] of Object.entries(headers)) {
		if (key.toLowerCase() === nameLowerCase) {
			for (const v of Array.isArray(value) ? value : [value]) {
				if (v == null) continue; // ignore null or undefined
				if (typeof v !== "string") return undefined; // non-string values are illegal
				if (found !== undefined) return undefined; // having duplicate entries is illegal
				found = v;
			}
		}
	}
	return found;
}

/**
 * 웹훅 페이로드를 검증합니다.
 *
 * @param secret 웹훅 시크릿
 * @param payload 웹훅 페이로드
 * @param headers 웹훅 요청 시 포함된 헤더
 * @returns 검증 후 디코딩된 웹훅 페이로드를 반환하는 Promise
 * @throws {@link InvalidInputError} 웹훅 시크릿 혹은 본문이 유효하지 않은 형식일 때 발생합니다.
 * @throws {@link WebhookVerificationError} 웹훅 검증에 실패했을 때 발생합니다.
 */
export async function verify(
	secret: string | Uint8Array,
	payload: string,
	headers:
		| WebhookUnbrandedRequiredHeaders
		| Record<string, string | string[] | undefined>,
): Promise<Webhook> {
	if (typeof payload !== "string")
		throw new InvalidInputError(
			"`payload` 파라미터의 타입이 string이 아닙니다.",
		);

	const msgId = findHeaderValue(headers, "webhook-id");
	const msgSignature = findHeaderValue(headers, "webhook-signature");
	const msgTimestamp = findHeaderValue(headers, "webhook-timestamp");

	if (!msgId || !msgSignature || !msgTimestamp) {
		throw new WebhookVerificationError("MISSING_REQUIRED_HEADERS");
	}

	verifyTimestamp(msgTimestamp);

	const expectedSignature = await sign(secret, msgId, msgTimestamp, payload);

	for (const versionedSignature of msgSignature.split(" ")) {
		const split = versionedSignature.split(",", 3);
		if (split.length < 2) continue;
		const [version, signature] = split;

		if (version !== "v1") continue;

		const signatureDecoded = tryCatch(
			() => Uint8Array.from(atob(signature), (c) => c.charCodeAt(0)),
			() => undefined,
		);
		if (signatureDecoded === undefined) continue;

		if (timingSafeEqual(signatureDecoded, expectedSignature)) {
			return JSON.parse(payload);
		}
	}
	throw new WebhookVerificationError("NO_MATCHING_SIGNATURE");
}

/**
 * 웹훅 페이로드를 서명하여 웹훅 본문을 생성합니다.
 *
 * @param msgId 웹훅 본문에 지정할 고유 ID
 * @param msgTimestamp 웹훅 생성 시도 시각
 * @param payload 웹훅 페이로드
 * @returns 서명된 웹훅 본문을 반환하는 Promise
 * @throws {@link InvalidInputError} 입력받은 웹훅 페이로드가 유효하지 않을 때 발생합니다.
 */
async function sign(
	secret: string | Uint8Array,
	msgId: string,
	msgTimestamp: string,
	payload: string,
): Promise<ArrayBuffer> {
	const cryptoKey = await getCryptoKeyFromSecret(secret);
	const encoder = new TextEncoder();
	const toSign = encoder.encode(`${msgId}.${msgTimestamp}.${payload}`);

	return await crypto.subtle.sign("HMAC", cryptoKey, toSign);
}

const secrets = new Map<string | Uint8Array, CryptoKey>();

/**
 * 웹훅 시크릿 입력으로부터 CryptoKey를 가져옵니다.
 *
 * @throws {@link InvalidInputError} 입력받은 웹훅 시크릿이 유효하지 않을 때 발생합니다.
 */
async function getCryptoKeyFromSecret(secret: string | Uint8Array) {
	const cryptoKeyCached = secrets.get(secret); // cache based on argument
	if (cryptoKeyCached !== undefined) return cryptoKeyCached;

	let rawSecret: Uint8Array;
	if (secret instanceof Uint8Array) {
		rawSecret = secret;
	} else if (typeof secret === "string") {
		const secretBase64 = secret.startsWith(prefix)
			? secret.substring(prefix.length)
			: secret;
		rawSecret = tryCatch(
			() => Uint8Array.from(atob(secretBase64), (c) => c.charCodeAt(0)),
			() => {
				throw new InvalidInputError(
					"`secret` 파라미터가 올바른 Base64 문자열이 아닙니다.",
				);
			},
		);
	} else {
		throw new InvalidInputError("`secret` 파라미터의 타입이 잘못되었습니다.");
	}

	if (rawSecret.length === 0) {
		throw new InvalidInputError("시크릿은 비어 있을 수 없습니다.");
	}

	const cryptoKey = await crypto.subtle.importKey(
		"raw",
		rawSecret,
		{ name: "HMAC", hash: "SHA-256" },
		false,
		["sign"],
	);

	secrets.set(secret, cryptoKey);

	return cryptoKey;
}

/**
 * 웹훅의 타임스탬프 정보를 검증합니다.
 *
 * @throws {@link WebhookVerificationError} 타임스탬프가 유효하지 않을 때 발생합니다.
 */
function verifyTimestamp(timestampHeader: string): void {
	const now = Math.floor(Date.now() / 1000);
	const timestamp = Number.parseInt(timestampHeader, 10);
	if (Number.isNaN(timestamp)) {
		throw new WebhookVerificationError("INVALID_SIGNATURE");
	}

	if (now - timestamp > WEBHOOK_TOLERANCE_IN_SECONDS) {
		throw new WebhookVerificationError("TIMESTAMP_TOO_OLD");
	}
	if (timestamp > now + WEBHOOK_TOLERANCE_IN_SECONDS) {
		throw new WebhookVerificationError("TIMESTAMP_TOO_NEW");
	}
}
