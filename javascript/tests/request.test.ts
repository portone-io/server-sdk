import * as sdk from "@portone/server-sdk";
import {
	CancelPaymentError,
	GetPaymentError,
} from "@portone/server-sdk/payment";
import { afterEach, describe, expect, it, vi } from "vitest";

const client = sdk.PaymentClient({ secret: "test-secret" });
const payments = { items: [], page: { number: 0, size: 0, totalCount: 0 } };
const cancelledPayment = {
	status: "CANCELLED",
	id: "test-server-sdk",
	transactionId: "transaction-id",
	merchantId: "merchant-id",
	storeId: "store-id",
	channel: { type: "TEST", pgProvider: "INICIS", pgMerchantId: "merchant-id" },
	version: "V2",
	requestedAt: "2024-01-01T00:00:00Z",
	updatedAt: "2024-01-01T00:00:00Z",
	statusChangedAt: "2024-01-01T00:00:00Z",
	orderName: "Test order",
	amount: {
		total: 1,
		taxFree: 0,
		discount: 0,
		paid: 1,
		cancelled: 1,
		cancelledTaxFree: 0,
	},
	currency: "KRW",
	customer: {},
	origin: { platformType: "API", ipAddress: "127.0.0.1" },
	cancellations: [],
	cancelledAt: "2024-01-01T00:00:00Z",
};

function mockFetch(body: unknown, status = 200) {
	const fetchMock = vi
		.fn<typeof fetch>()
		.mockResolvedValue(new Response(JSON.stringify(body), { status }));
	vi.stubGlobal("fetch", fetchMock);
	return fetchMock;
}

function expectRequest(
	fetchMock: ReturnType<typeof mockFetch>,
	method: string,
	path: string,
	body?: unknown,
) {
	expect(fetchMock).toHaveBeenCalledOnce();
	const [url, init] = fetchMock.mock.calls[0];
	expect(url).toBeInstanceOf(URL);
	expect(`${(url as URL).pathname}${(url as URL).search}`).toBe(path);
	expect(init?.method).toBe(method);
	const headers = new Headers(init?.headers);
	expect(headers.get("Authorization")).toBe("PortOne test-secret");
	expect(headers.get("User-Agent")).toBeTruthy();
	if (body === undefined) expect(init?.body).toBeUndefined();
	else expect(JSON.parse(init?.body as string)).toEqual(body);
}

afterEach(() => vi.unstubAllGlobals());

describe("payment requests", () => {
	it.each([
		200, 502,
	])("propagates the JSON parser error for HTTP %i", async (status) => {
		const response = new Response(null, { status });
		const error = new SyntaxError("native parser diagnostic");
		vi.spyOn(response, "json").mockRejectedValue(error);
		vi.stubGlobal("fetch", vi.fn().mockResolvedValue(response));
		await expect(client.getPayments()).rejects.toBe(error);
	});
	it.each([
		"private-body",
		{ message: ["private-body"] },
	])("omits unexpected error data from the message", async (body) => {
		mockFetch(body, 502);
		await expect(client.getPayments()).rejects.toMatchObject({
			message: "",
			data: body,
		});
	});
	it("gets payments without parameters", async () => {
		const fetchMock = mockFetch(payments);
		await expect(client.getPayments()).resolves.toEqual(payments);
		expectRequest(fetchMock, "GET", "/payments?requestBody=%7B%7D");
	});
	it("gets payments with a page", async () => {
		const fetchMock = mockFetch(payments);
		await expect(
			client.getPayments({ page: { number: 3000 } }),
		).resolves.toEqual(payments);
		expectRequest(
			fetchMock,
			"GET",
			"/payments?requestBody=%7B%22page%22%3A%7B%22number%22%3A3000%7D%7D",
		);
	});
	it("gets a cancelled payment", async () => {
		const fetchMock = mockFetch(cancelledPayment);
		await expect(
			client.getPayment({ paymentId: "test-server-sdk" }),
		).resolves.toEqual(cancelledPayment);
		expectRequest(fetchMock, "GET", "/payments/test-server-sdk");
	});
	it("rejects dot segments before fetching", async () => {
		const fetchMock = mockFetch(cancelledPayment);
		const dots = [".", "%2e", "%2E"];
		for (const first of dots) {
			for (const second of ["", ...dots]) {
				await expect(
					client.getPayment({ paymentId: first + second }),
				).rejects.toThrow(RangeError);
			}
		}
		expect(fetchMock).not.toHaveBeenCalled();
	});
	it("preserves native coercion for JavaScript callers", async () => {
		const fetchMock = mockFetch(cancelledPayment);
		const stringifyId = vi.fn(() => "order/part");
		// @ts-expect-error Exercise an untyped JavaScript call.
		await client.getPayment({ paymentId: { toString: stringifyId } });
		expect(stringifyId).toHaveBeenCalledOnce();
		expectRequest(fetchMock, "GET", "/payments/order%2Fpart");
	});
	it.each([
		[" ", "/payments/%20"],
		["order.v2/part", "/payments/order.v2%2Fpart"],
		["...", "/payments/..."],
	])("encodes payment ID %s and returns its error", async (paymentId, path) => {
		const error = { type: "PAYMENT_NOT_FOUND", message: "Payment not found" };
		const fetchMock = mockFetch(error, 404);
		const result = client.getPayment({ paymentId });
		await expect(result).rejects.toBeInstanceOf(GetPaymentError);
		await expect(result).rejects.toMatchObject({ data: error });
		expectRequest(fetchMock, "GET", path);
	});
	it("returns a cancellation error", async () => {
		const error = {
			type: "PAYMENT_ALREADY_CANCELLED",
			message: "Payment already cancelled",
		};
		const fetchMock = mockFetch(error, 409);
		const result = client.cancelPayment({
			paymentId: "test-server-sdk",
			reason: "test",
			amount: 1,
		});
		await expect(result).rejects.toBeInstanceOf(CancelPaymentError);
		await expect(result).rejects.toMatchObject({ data: error });
		expectRequest(fetchMock, "POST", "/payments/test-server-sdk/cancel", {
			amount: 1,
			reason: "test",
		});
	});
	it("includes the client store ID in cancellation requests", async () => {
		const response = { cancellation: {} };
		const fetchMock = mockFetch(response);
		const storeClient = sdk.PaymentClient({
			secret: "test-secret",
			storeId: "store-id",
		});
		await expect(
			storeClient.cancelPayment({
				paymentId: "test-server-sdk",
				reason: "test",
			}),
		).resolves.toEqual(response);
		expectRequest(fetchMock, "POST", "/payments/test-server-sdk/cancel", {
			storeId: "store-id",
			reason: "test",
		});
	});
});
