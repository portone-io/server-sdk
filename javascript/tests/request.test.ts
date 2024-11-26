import * as sdk from "@portone/server-sdk";
import {
	CancelPaymentError,
	GetPaymentError,
} from "@portone/server-sdk/payment";
import { describe, expect, it } from "vitest";

declare global {
	namespace NodeJS {
		interface ProcessEnv {
			PORTONE_API_SECRET: string;
		}
	}
}

const { PORTONE_API_SECRET } = process.env;

const client = sdk.PaymentClient({
	secret: PORTONE_API_SECRET,
});

describe("correct cases", () => {
	describe("payment.getPayments()", () => {
		it("without parameters", async () => {
			await expect(client.getPayments()).resolves.toMatchObject({
				items: expect.arrayContaining([]),
			});
		});
		it("with parameters", async () => {
			await expect(
				client.getPayments({ page: { number: 3000 } }),
			).resolves.toMatchObject({
				items: [],
			});
		});
	});
	describe("payment.getPayment()", () => {
		it("with parameters", async () => {
			await expect(
				client.getPayment({ paymentId: "test-server-sdk" }),
			).resolves.toMatchObject({});
		});
	});
});

describe("error cases", () => {
	describe("payment.getPayment()", () => {
		it("with invalid paymentId", async () => {
			await expect(() => client.getPayment({ paymentId: " " })).rejects.toThrow(
				GetPaymentError,
			);
		});
	});
	describe("payment.cancelPayment()", () => {
		it("with already cancelled paymentId", async () => {
			await expect(() =>
				client.cancelPayment({
					paymentId: "test-server-sdk",
					reason: "test",
					amount: 1,
				}),
			).rejects.toThrow(CancelPaymentError);
		});
	});
});
