import * as sdk from "@portone/server-sdk";
import { describe, expect, it } from "vitest";
import {
	PaymentAlreadyCancelledError,
	PaymentNotFoundError,
} from "../src/generated/errors";

declare global {
	namespace NodeJS {
		interface ProcessEnv {
			PORTONE_API_SECRET: string;
		}
	}
}

const { PORTONE_API_SECRET } = process.env;

const client = sdk.PortOneClient(PORTONE_API_SECRET);

describe("correct cases", () => {
	describe("payment.getPayments()", () => {
		it("without parameters", async () => {
			await expect(client.payment.getPayments()).resolves.toMatchObject({
				items: expect.arrayContaining([]),
			});
		});
		it("with parameters", async () => {
			await expect(
				client.payment.getPayments({ page: { number: 3000 } }),
			).resolves.toMatchObject({
				items: [],
			});
		});
	});
	describe("payment.getPayment()", () => {
		it("with parameters", async () => {
			await expect(
				client.payment.getPayment("test-server-sdk"),
			).resolves.toMatchObject({});
		});
	});
});

describe("error cases", () => {
	describe("payment.getPayment()", () => {
		it("with invalid paymentId", async () => {
			await expect(() => client.payment.getPayment(" ")).rejects.toThrow(
				PaymentNotFoundError,
			);
		});
	});
	describe("payment.cancelPayment()", () => {
		it("with already cancelled paymentId", async () => {
			await expect(() =>
				client.payment.cancelPayment({
					paymentId: "test-server-sdk",
					reason: "test",
					amount: 1,
				}),
			).rejects.toThrow(PaymentAlreadyCancelledError);
		});
	});
});
