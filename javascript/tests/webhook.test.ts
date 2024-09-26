import * as sdk from "@portone/server-sdk";
import { describe, expect, it } from "vitest";

const secret = "pzQGE83cSIRKM4/WH5QY+g==";

const crypto = globalThis.crypto ?? (await import("node:crypto")).webcrypto;

const makeWebhook = async (timestamp = Date.now()) => {
	const timestampInSec = Math.floor(timestamp / 1000);
	const id = "dummy-webhook-id";
	const payload = JSON.stringify({ test: "test payload" });

	const encoder = new TextEncoder();
	const toSign = encoder.encode(`${id}.${timestampInSec}.${payload}`);
	const key = await crypto.subtle.importKey(
		"raw",
		Uint8Array.from(atob(secret), (c) => c.charCodeAt(0)),
		{ name: "HMAC", hash: "SHA-256" },
		false,
		["sign"],
	);
	const signature = await crypto.subtle.sign("HMAC", key, toSign);
	const signatureBase64 = btoa(
		String.fromCharCode(...new Uint8Array(signature)),
	);

	return {
		header: {
			"webhook-id": id,
			"webhook-signature": `v1,${signatureBase64}`,
			"webhook-timestamp": timestampInSec.toString(),
		} as Partial<sdk.Webhook.WebhookUnbrandedRequiredHeaders>,
		payload,
	};
};

it("should be exported", async () => {
	expect(sdk.Webhook).toBeDefined();
});

describe("correct cases", () => {
	describe("verify()", () => {
		it("valid signature is valid", async () => {
			const testWebhook = await makeWebhook();

			await expect(
				sdk.Webhook.verify(secret, testWebhook.payload, testWebhook.header),
			).resolves.toBeUndefined();
		});

		it("valid unbranded signature is valid", async () => {
			const testWebhook = await makeWebhook();
			const unbrandedHeaders: Record<string, string | undefined> = {
				"webhook-id": testWebhook.header["webhook-id"],
				"webhook-signature": testWebhook.header["webhook-signature"],
				"webhook-timestamp": testWebhook.header["webhook-timestamp"],
			};
			testWebhook.header = unbrandedHeaders;

			await expect(
				sdk.Webhook.verify(secret, testWebhook.payload, testWebhook.header),
			).resolves.toBeUndefined();
		});

		it("multiple signatures", async () => {
			const testWebhook = await makeWebhook();
			const sigs = [
				"v1,Ceo5qEr07ixe2NLpvHk3FH9bwy/WavXrAFQ/9tdO6mc=",
				"v2,Ceo5qEr07ixe2NLpvHk3FH9bwy/WavXrAFQ/9tdO6mc=",
				testWebhook.header["webhook-signature"], // valid signature
				"v1,Ceo5qEr07ixe2NLpvHk3FH9bwy/WavXrAFQ/9tdO6mc=",
			];
			testWebhook.header["webhook-signature"] = sigs.join(" ");

			await expect(
				sdk.Webhook.verify(secret, testWebhook.payload, testWebhook.header),
			).resolves.toBeUndefined();
		});

		it("handles both with and without signature prefix", async () => {
			const testPayload = await makeWebhook();

			await expect(
				sdk.Webhook.verify(secret, testPayload.payload, testPayload.header),
			).resolves.toBeUndefined();
			await expect(
				sdk.Webhook.verify(secret, testPayload.payload, testPayload.header),
			).resolves.toBeUndefined();
		});
	});
});

describe("error cases", () => {
	it("empty secret", async () => {
		const testWebhook = await makeWebhook();

		await expect(() =>
			sdk.Webhook.verify("", testWebhook.payload, testWebhook.header),
		).rejects.toThrow(sdk.Errors.InvalidInputError);
		await expect(() =>
			// biome-ignore lint/suspicious/noExplicitAny: testing runtime type check
			sdk.Webhook.verify(null as any, testWebhook.payload, testWebhook.header),
		).rejects.toThrow(sdk.Errors.InvalidInputError);
		await expect(() =>
			sdk.Webhook.verify(
				// biome-ignore lint/suspicious/noExplicitAny: testing runtime type check
				undefined as any,
				testWebhook.payload,
				testWebhook.header,
			),
		).rejects.toThrow(sdk.Errors.InvalidInputError);
	});

	it("missing id on header", async () => {
		const testWebhook = await makeWebhook();
		// biome-ignore lint/performance/noDelete: testing runtime validations
		delete testWebhook.header["webhook-id"];

		await expect(() =>
			sdk.Webhook.verify(secret, testWebhook.payload, testWebhook.header),
		).rejects.toThrowError(sdk.Errors.WebhookVerificationError);
	});

	it("missing timestamp on header", async () => {
		const testWebhook = await makeWebhook();
		// biome-ignore lint/performance/noDelete: testing runtime validations
		delete testWebhook.header["webhook-timestamp"];

		await expect(() =>
			sdk.Webhook.verify(secret, testWebhook.payload, testWebhook.header),
		).rejects.toThrowError(sdk.Errors.WebhookVerificationError);
	});

	it("invalid timestamp on header", async () => {
		const testWebhook = await makeWebhook();
		testWebhook.header["webhook-timestamp"] = "hello";

		await expect(() =>
			sdk.Webhook.verify(secret, testWebhook.payload, testWebhook.header),
		).rejects.toThrowError(sdk.Errors.WebhookVerificationError);
	});

	it("missing signature on header", async () => {
		const testWebhook = await makeWebhook();
		// biome-ignore lint/performance/noDelete: testing runtime validations
		delete testWebhook.header["webhook-signature"];

		await expect(() =>
			sdk.Webhook.verify(secret, testWebhook.payload, testWebhook.header),
		).rejects.toThrowError(sdk.Errors.WebhookVerificationError);
	});

	it("invalid signature on header", async () => {
		const testWebhook = await makeWebhook();
		testWebhook.header["webhook-signature"] = "v1,dawfeoifkpqwoekfpqoekf";

		await expect(() =>
			sdk.Webhook.verify(secret, testWebhook.payload, testWebhook.header),
		).rejects.toThrowError(sdk.Errors.WebhookVerificationError);
	});

	it("partial signature on header", async () => {
		const testWebhook = await makeWebhook();
		// biome-ignore lint/style/noNonNullAssertion: it is initially non-nullable
		testWebhook.header["webhook-signature"] = testWebhook.header[
			"webhook-signature"
		]!.slice(0, 8);

		await expect(() =>
			sdk.Webhook.verify(secret, testWebhook.payload, testWebhook.header),
		).rejects.toThrowError(sdk.Errors.WebhookVerificationError);

		testWebhook.header["webhook-signature"] = "v1,";

		await expect(() =>
			sdk.Webhook.verify(secret, testWebhook.payload, testWebhook.header),
		).rejects.toThrowError(sdk.Errors.WebhookVerificationError);
	});

	it("old timestamp", async () => {
		const testWebhook = await makeWebhook(Date.now() - 5 * 1000 * 1000 - 1000);

		await expect(() =>
			sdk.Webhook.verify(secret, testWebhook.payload, testWebhook.header),
		).rejects.toThrowError(sdk.Errors.WebhookVerificationError);
	});

	it("new timestamp", async () => {
		const testPayload = await makeWebhook(Date.now() + 5 * 1000 * 1000 + 1000);

		await expect(() =>
			sdk.Webhook.verify(secret, testPayload.payload, testPayload.header),
		).rejects.toThrowError(sdk.Errors.WebhookVerificationError);
	});
});
