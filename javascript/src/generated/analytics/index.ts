import type { AnalyticsAverageAmountChart } from "..//analytics/AnalyticsAverageAmountChart"
import type { AnalyticsCancellationRate } from "..//analytics/AnalyticsCancellationRate"
import type { AnalyticsCardChart } from "..//analytics/AnalyticsCardChart"
import type { AnalyticsCardCompanyChart } from "..//analytics/AnalyticsCardCompanyChart"
import type { AnalyticsEasyPayChart } from "..//analytics/AnalyticsEasyPayChart"
import type { AnalyticsEasyPayProviderChart } from "..//analytics/AnalyticsEasyPayProviderChart"
import type { AnalyticsOverseasPaymentUsage } from "..//analytics/AnalyticsOverseasPaymentUsage"
import type { AnalyticsPaymentChart } from "..//analytics/AnalyticsPaymentChart"
import type { AnalyticsPaymentChartInsight } from "..//analytics/AnalyticsPaymentChartInsight"
import type { AnalyticsPaymentMethodChart } from "..//analytics/AnalyticsPaymentMethodChart"
import type { AnalyticsPaymentMethodTrendChart } from "..//analytics/AnalyticsPaymentMethodTrendChart"
import type { AnalyticsPaymentStatusByPaymentClientChart } from "..//analytics/AnalyticsPaymentStatusByPaymentClientChart"
import type { AnalyticsPaymentStatusByPaymentMethodChart } from "..//analytics/AnalyticsPaymentStatusByPaymentMethodChart"
import type { AnalyticsPaymentStatusByPgCompanyChart } from "..//analytics/AnalyticsPaymentStatusByPgCompanyChart"
import type { AnalyticsPaymentStatusChart } from "..//analytics/AnalyticsPaymentStatusChart"
import type { AnalyticsPgCompanyChart } from "..//analytics/AnalyticsPgCompanyChart"
import type { AnalyticsPgCompanyTrendChart } from "..//analytics/AnalyticsPgCompanyTrendChart"
import type { AnalyticsTimeGranularity } from "..//analytics/AnalyticsTimeGranularity"
import type { CardCompany } from "..//analytics/CardCompany"
import type { Currency } from "..//common/Currency"
import type { EasyPayProvider } from "..//common/EasyPayProvider"
import type { GetAnalyticsCancellationRateError } from "..//analytics/GetAnalyticsCancellationRateError"
import type { GetAnalyticsCardChartError } from "..//analytics/GetAnalyticsCardChartError"
import type { GetAnalyticsCardCompanyChartError } from "..//analytics/GetAnalyticsCardCompanyChartError"
import type { GetAnalyticsEasyPayChartError } from "..//analytics/GetAnalyticsEasyPayChartError"
import type { GetAnalyticsEasyPayProviderChartError } from "..//analytics/GetAnalyticsEasyPayProviderChartError"
import type { GetAnalyticsOverseasPaymentUsageError } from "..//analytics/GetAnalyticsOverseasPaymentUsageError"
import type { GetAnalyticsPaymentChartError } from "..//analytics/GetAnalyticsPaymentChartError"
import type { GetAnalyticsPaymentChartInsightError } from "..//analytics/GetAnalyticsPaymentChartInsightError"
import type { GetAverageAmountChartError } from "..//analytics/GetAverageAmountChartError"
import type { GetPaymentMethodChartError } from "..//analytics/GetPaymentMethodChartError"
import type { GetPaymentMethodTrendChartError } from "..//analytics/GetPaymentMethodTrendChartError"
import type { GetPaymentStatusByPaymentClientChartError } from "..//analytics/GetPaymentStatusByPaymentClientChartError"
import type { GetPaymentStatusByPaymentMethodChartError } from "..//analytics/GetPaymentStatusByPaymentMethodChartError"
import type { GetPaymentStatusByPgCompanyChartError } from "..//analytics/GetPaymentStatusByPgCompanyChartError"
import type { GetPaymentStatusChartError } from "..//analytics/GetPaymentStatusChartError"
import type { GetPgCompanyChartError } from "..//analytics/GetPgCompanyChartError"
import type { GetPgCompanyTrendChartError } from "..//analytics/GetPgCompanyTrendChartError"
import type { PgCompany } from "..//common/PgCompany"
import * as Errors from "..//errors"
export type { AnalyticsAverageAmountChart } from "./AnalyticsAverageAmountChart"
export type { AnalyticsAverageAmountChartStat } from "./AnalyticsAverageAmountChartStat"
export type { AnalyticsAverageAmountChartSummary } from "./AnalyticsAverageAmountChartSummary"
export type { AnalyticsCancellationRate } from "./AnalyticsCancellationRate"
export type { AnalyticsCardChart } from "./AnalyticsCardChart"
export type { AnalyticsCardChartStat } from "./AnalyticsCardChartStat"
export type { AnalyticsCardCompanyChart } from "./AnalyticsCardCompanyChart"
export type { AnalyticsCardCompanyChartRemainderStat } from "./AnalyticsCardCompanyChartRemainderStat"
export type { AnalyticsCardCompanyChartStat } from "./AnalyticsCardCompanyChartStat"
export type { AnalyticsCardCompanyChartSummary } from "./AnalyticsCardCompanyChartSummary"
export type { AnalyticsEasyPayChart } from "./AnalyticsEasyPayChart"
export type { AnalyticsEasyPayChartStat } from "./AnalyticsEasyPayChartStat"
export type { AnalyticsEasyPayProviderChart } from "./AnalyticsEasyPayProviderChart"
export type { AnalyticsEasyPayProviderChartRemainderStat } from "./AnalyticsEasyPayProviderChartRemainderStat"
export type { AnalyticsEasyPayProviderChartStat } from "./AnalyticsEasyPayProviderChartStat"
export type { AnalyticsEasyPayProviderChartSummary } from "./AnalyticsEasyPayProviderChartSummary"
export type { AnalyticsOverseasPaymentUsage } from "./AnalyticsOverseasPaymentUsage"
export type { AnalyticsPaymentChart } from "./AnalyticsPaymentChart"
export type { AnalyticsPaymentChartInsight } from "./AnalyticsPaymentChartInsight"
export type { AnalyticsPaymentChartStat } from "./AnalyticsPaymentChartStat"
export type { AnalyticsPaymentMethodChart } from "./AnalyticsPaymentMethodChart"
export type { AnalyticsPaymentMethodChartStat } from "./AnalyticsPaymentMethodChartStat"
export type { AnalyticsPaymentMethodTrendChart } from "./AnalyticsPaymentMethodTrendChart"
export type { AnalyticsPaymentMethodTrendChartStat } from "./AnalyticsPaymentMethodTrendChartStat"
export type { AnalyticsPaymentStatusByPaymentClientChart } from "./AnalyticsPaymentStatusByPaymentClientChart"
export type { AnalyticsPaymentStatusByPaymentClientChartStat } from "./AnalyticsPaymentStatusByPaymentClientChartStat"
export type { AnalyticsPaymentStatusByPaymentMethodChart } from "./AnalyticsPaymentStatusByPaymentMethodChart"
export type { AnalyticsPaymentStatusByPaymentMethodChartStat } from "./AnalyticsPaymentStatusByPaymentMethodChartStat"
export type { AnalyticsPaymentStatusByPgCompanyChart } from "./AnalyticsPaymentStatusByPgCompanyChart"
export type { AnalyticsPaymentStatusByPgCompanyChartStat } from "./AnalyticsPaymentStatusByPgCompanyChartStat"
export type { AnalyticsPaymentStatusChart } from "./AnalyticsPaymentStatusChart"
export type { AnalyticsPaymentStatusChartStat } from "./AnalyticsPaymentStatusChartStat"
export type { AnalyticsPgCompanyChart } from "./AnalyticsPgCompanyChart"
export type { AnalyticsPgCompanyChartStat } from "./AnalyticsPgCompanyChartStat"
export type { AnalyticsPgCompanyTrendChart } from "./AnalyticsPgCompanyTrendChart"
export type { AnalyticsPgCompanyTrendChartStat } from "./AnalyticsPgCompanyTrendChartStat"
export type { AnalyticsTimeGranularity } from "./AnalyticsTimeGranularity"
export type { AnalyticsTimeGranularityDay } from "./AnalyticsTimeGranularityDay"
export type { AnalyticsTimeGranularityHour } from "./AnalyticsTimeGranularityHour"
export type { AnalyticsTimeGranularityMinute } from "./AnalyticsTimeGranularityMinute"
export type { AnalyticsTimeGranularityMonth } from "./AnalyticsTimeGranularityMonth"
export type { AnalyticsTimeGranularityWeek } from "./AnalyticsTimeGranularityWeek"
export type { CardCompany } from "./CardCompany"
export type { GetAnalyticsAverageAmountChartBody } from "./GetAnalyticsAverageAmountChartBody"
export type { GetAnalyticsCancellationRateBody } from "./GetAnalyticsCancellationRateBody"
export type { GetAnalyticsCardChartBody } from "./GetAnalyticsCardChartBody"
export type { GetAnalyticsCardCompanyChartBody } from "./GetAnalyticsCardCompanyChartBody"
export type { GetAnalyticsEasyPayChartBody } from "./GetAnalyticsEasyPayChartBody"
export type { GetAnalyticsEasyPayProviderChartBody } from "./GetAnalyticsEasyPayProviderChartBody"
export type { GetAnalyticsPaymentChartBody } from "./GetAnalyticsPaymentChartBody"
export type { GetAnalyticsPaymentChartInsightBody } from "./GetAnalyticsPaymentChartInsightBody"
export type { GetAnalyticsPaymentMethodChartBody } from "./GetAnalyticsPaymentMethodChartBody"
export type { GetAnalyticsPaymentMethodTrendChartBody } from "./GetAnalyticsPaymentMethodTrendChartBody"
export type { GetAnalyticsPaymentStatusByPaymentClientChartBody } from "./GetAnalyticsPaymentStatusByPaymentClientChartBody"
export type { GetAnalyticsPaymentStatusByPaymentMethodChartBody } from "./GetAnalyticsPaymentStatusByPaymentMethodChartBody"
export type { GetAnalyticsPaymentStatusByPgCompanyChartBody } from "./GetAnalyticsPaymentStatusByPgCompanyChartBody"
export type { GetAnalyticsPaymentStatusChartBody } from "./GetAnalyticsPaymentStatusChartBody"
export type { GetAnalyticsPgCompanyChartBody } from "./GetAnalyticsPgCompanyChartBody"
export type { GetAnalyticsPgCompanyTrendChartBody } from "./GetAnalyticsPgCompanyTrendChartBody"
/** @ignore */
export function AnalyticsClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): AnalyticsClient {
	return {
		getAnalyticsPaymentChart: async (
			from: string,
			until: string,
			currency: Currency,
			timeGranularity: AnalyticsTimeGranularity,
			excludeCancelled?: boolean,
		): Promise<AnalyticsPaymentChart> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
				excludeCancelled,
				timeGranularity,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/payment?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetAnalyticsPaymentChartError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getAnalyticsPaymentChartInsight: async (
			from: string,
			until: string,
			currency: Currency,
			timezoneHourOffset: number,
			excludeCancelled?: boolean,
		): Promise<AnalyticsPaymentChartInsight> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
				excludeCancelled,
				timezoneHourOffset,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/payment-insight?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetAnalyticsPaymentChartInsightError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getAverageAmountChart: async (
			from: string,
			until: string,
			currency: Currency,
			excludeCancelled: boolean,
			timeGranularity: AnalyticsTimeGranularity,
		): Promise<AnalyticsAverageAmountChart> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
				excludeCancelled,
				timeGranularity,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/average-amount?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetAverageAmountChartError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPaymentMethodChart: async (
			from: string,
			until: string,
			currency: Currency,
			excludeCancelled: boolean,
		): Promise<AnalyticsPaymentMethodChart> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
				excludeCancelled,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/payment-method?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPaymentMethodChartError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPaymentMethodTrendChart: async (
			from: string,
			until: string,
			currency: Currency,
			excludeCancelled: boolean,
			timeGranularity: AnalyticsTimeGranularity,
		): Promise<AnalyticsPaymentMethodTrendChart> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
				excludeCancelled,
				timeGranularity,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/payment-method-trend?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPaymentMethodTrendChartError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getAnalyticsCardChart: async (
			from: string,
			until: string,
			currency: Currency,
			excludeCancelled: boolean,
			timeGranularity: AnalyticsTimeGranularity,
		): Promise<AnalyticsCardChart> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
				excludeCancelled,
				timeGranularity,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/card?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetAnalyticsCardChartError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getAnalyticsCardCompanyChart: async (
			from: string,
			until: string,
			currency: Currency,
			excludeCancelled: boolean,
			timeGranularity: AnalyticsTimeGranularity,
			cardCompanies: CardCompany[],
			excludesFromRemainders: CardCompany[],
		): Promise<AnalyticsCardCompanyChart> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
				excludeCancelled,
				timeGranularity,
				cardCompanies,
				excludesFromRemainders,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/card-company?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetAnalyticsCardCompanyChartError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getAnalyticsEasyPayChart: async (
			from: string,
			until: string,
			currency: Currency,
			excludeCancelled: boolean,
			timeGranularity: AnalyticsTimeGranularity,
		): Promise<AnalyticsEasyPayChart> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
				excludeCancelled,
				timeGranularity,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/easy-pay?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetAnalyticsEasyPayChartError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getAnalyticsEasyPayProviderChart: async (
			from: string,
			until: string,
			currency: Currency,
			excludeCancelled: boolean,
			timeGranularity: AnalyticsTimeGranularity,
			easyPayProviders: EasyPayProvider[],
			excludesFromRemainders: EasyPayProvider[],
		): Promise<AnalyticsEasyPayProviderChart> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
				excludeCancelled,
				timeGranularity,
				easyPayProviders,
				excludesFromRemainders,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/easy-pay-provider?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetAnalyticsEasyPayProviderChartError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPgCompanyChart: async (
			from: string,
			until: string,
			currency: Currency,
			excludeCancelled: boolean,
		): Promise<AnalyticsPgCompanyChart> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
				excludeCancelled,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/pg-company?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPgCompanyChartError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPgCompanyTrendChart: async (
			from: string,
			until: string,
			currency: Currency,
			excludeCancelled: boolean,
			timeGranularity: AnalyticsTimeGranularity,
			pgCompanies: PgCompany[],
		): Promise<AnalyticsPgCompanyTrendChart> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
				excludeCancelled,
				timeGranularity,
				pgCompanies,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/pg-company-trend?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPgCompanyTrendChartError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getAnalyticsOverseasPaymentUsage: async (
		): Promise<AnalyticsOverseasPaymentUsage> => {
			const response = await fetch(
				new URL("/analytics/overseas-payment-usage", baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetAnalyticsOverseasPaymentUsageError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getAnalyticsCancellationRate: async (
			from: string,
			until: string,
			currency: Currency,
		): Promise<AnalyticsCancellationRate> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/cancellation-rate?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetAnalyticsCancellationRateError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPaymentStatusChart: async (
			from: string,
			until: string,
			currency: Currency,
		): Promise<AnalyticsPaymentStatusChart> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/payment-status?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPaymentStatusChartError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPaymentStatusByPaymentMethodChart: async (
			from: string,
			until: string,
			currency: Currency,
		): Promise<AnalyticsPaymentStatusByPaymentMethodChart> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/payment-status/by-method?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPaymentStatusByPaymentMethodChartError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPaymentStatusByPgCompanyChart: async (
			from: string,
			until: string,
			currency: Currency,
		): Promise<AnalyticsPaymentStatusByPgCompanyChart> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/payment-status/by-pg-company?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPaymentStatusByPgCompanyChartError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPaymentStatusByPaymentClientChart: async (
			from: string,
			until: string,
			currency: Currency,
		): Promise<AnalyticsPaymentStatusByPaymentClientChart> => {
			const requestBody = JSON.stringify({
				from,
				until,
				currency,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/analytics/charts/payment-status/by-payment-client?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPaymentStatusByPaymentClientChartError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
	}
}
export type AnalyticsClient = {
	/**
	 * 고객사의 결제 현황을 조회합니다.
	 *
	 * @param from
	 * 조회할 결제 현황의 시작 시간
	 * @param until
	 * 조회할 결제 현황의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 * @param excludeCancelled
	 * 결제취소건 제외 여부
	 *
	 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
	 * @param timeGranularity
	 * 결제 현황 조회 단위
	 *
	 * 시간별, 월별 단위만 지원됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getAnalyticsPaymentChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled?: boolean,
	) => Promise<AnalyticsPaymentChart>
	/**
	 * 고객사의 결제 현황 인사이트를 조회합니다.
	 *
	 * @param from
	 * 조회할 결제 현황의 시작 시간
	 * @param until
	 * 조회할 결제 현황의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 * @param excludeCancelled
	 * 결제취소건 제외 여부
	 *
	 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
	 * @param timezoneHourOffset
	 * 타임존 시간 오프셋
	 *
	 * 입력된 시간 오프셋 기준으로 일, 주, 월이 집계 됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getAnalyticsPaymentChartInsight: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 타임존 시간 오프셋
		 *
		 * 입력된 시간 오프셋 기준으로 일, 주, 월이 집계 됩니다.
		 * (int32)
		 */
		timezoneHourOffset: number,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled?: boolean,
	) => Promise<AnalyticsPaymentChartInsight>
	/**
	 * 고객사의 평균 거래액 현황을 조회합니다.
	 *
	 * @param from
	 * 조회할 평균 거래액 현황의 시작 시간
	 * @param until
	 * 조회할 평균 거래액 현황의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 * @param excludeCancelled
	 * 결제취소건 제외 여부
	 *
	 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
	 * @param timeGranularity
	 * 평균 거래액 현황 조회 단위
	 *
	 * 시간별, 월별 단위만 지원됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getAverageAmountChart: (
		/**
		 * 조회할 평균 거래액 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 평균 거래액 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 평균 거래액 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
	) => Promise<AnalyticsAverageAmountChart>
	/**
	 * 고객사의 결제수단 현황을 조회합니다.
	 *
	 * @param from
	 * 조회할 결제수단 현황의 시작 시간
	 * @param until
	 * 조회할 결제수단 현황의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 * @param excludeCancelled
	 * 결제취소건 제외 여부
	 *
	 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getPaymentMethodChart: (
		/**
		 * 조회할 결제수단 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제수단 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
	) => Promise<AnalyticsPaymentMethodChart>
	/**
	 * 고객사의 결제수단 트렌드를 조회합니다.
	 *
	 * @param from
	 * 조회할 결제수단 트렌드의 시작 시간
	 * @param until
	 * 조회할 결제수단 트렌드의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 * @param excludeCancelled
	 * 결제취소건 제외 여부
	 *
	 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
	 * @param timeGranularity
	 * 결제 결제수단 트렌드 조회 단위
	 *
	 * 시간별, 월별 단위만 지원됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getPaymentMethodTrendChart: (
		/**
		 * 조회할 결제수단 트렌드의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제수단 트렌드의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 결제 결제수단 트렌드 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
	) => Promise<AnalyticsPaymentMethodTrendChart>
	/**
	 * 고객사의 카드결제 현황을 조회합니다.
	 *
	 * @param from
	 * 조회할 카드결제 현황의 시작 시간
	 * @param until
	 * 조회할 카드결제 현황의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 * @param excludeCancelled
	 * 결제취소건 제외 여부
	 *
	 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
	 * @param timeGranularity
	 * 카드결제 현황 조회 단위
	 *
	 * 시간별, 월별 단위만 지원됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getAnalyticsCardChart: (
		/**
		 * 조회할 카드결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 카드결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 카드결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
	) => Promise<AnalyticsCardChart>
	/**
	 * 고객사의 카드사별 결제 현황을 조회합니다.
	 *
	 * @param from
	 * 조회할 카드사별 결제 현황의 시작 시간
	 * @param until
	 * 조회할 카드사별 결제 현황의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 * @param excludeCancelled
	 * 결제취소건 제외 여부
	 *
	 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
	 * @param timeGranularity
	 * 카드사별 결제 현황 조회 단위
	 *
	 * 시간별, 월별 단위만 지원됩니다.
	 * @param cardCompanies
	 * 조회할 카드사
	 * @param excludesFromRemainders
	 * 나머지 집계에 포함되지 않을 카드사
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getAnalyticsCardCompanyChart: (
		/**
		 * 조회할 카드사별 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 카드사별 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 카드사별 결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
		/** 조회할 카드사 */
		cardCompanies: CardCompany[],
		/** 나머지 집계에 포함되지 않을 카드사 */
		excludesFromRemainders: CardCompany[],
	) => Promise<AnalyticsCardCompanyChart>
	/**
	 * 고객사의 간편결제 현황을 조회합니다.
	 *
	 * @param from
	 * 조회할 간편결제 현황의 시작 시간
	 * @param until
	 * 조회할 간편결제 현황의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 * @param excludeCancelled
	 * 결제취소건 제외 여부
	 *
	 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
	 * @param timeGranularity
	 * 간편결제 현황 조회 단위
	 *
	 * 시간별, 월별 단위만 지원됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getAnalyticsEasyPayChart: (
		/**
		 * 조회할 간편결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 간편결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 간편결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
	) => Promise<AnalyticsEasyPayChart>
	/**
	 * 고객사의 간편결제사별 결제 현황을 조회합니다.
	 *
	 * @param from
	 * 조회할 간편결제사별 결제 현황의 시작 시간
	 * @param until
	 * 조회할 간편결제사별 결제 현황의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 * @param excludeCancelled
	 * 결제취소건 제외 여부
	 *
	 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
	 * @param timeGranularity
	 * 간편결제사별 결제 현황 조회 단위
	 *
	 * 시간별, 월별 단위만 지원됩니다.
	 * @param easyPayProviders
	 * 조회할 간편결제사
	 * @param excludesFromRemainders
	 * 나머지 집계에 포함되지 않을 간편결제사
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getAnalyticsEasyPayProviderChart: (
		/**
		 * 조회할 간편결제사별 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 간편결제사별 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 간편결제사별 결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
		/** 조회할 간편결제사 */
		easyPayProviders: EasyPayProvider[],
		/** 나머지 집계에 포함되지 않을 간편결제사 */
		excludesFromRemainders: EasyPayProvider[],
	) => Promise<AnalyticsEasyPayProviderChart>
	/**
	 * 고객사의 결제대행사 현황을 조회합니다.
	 *
	 * @param from
	 * 조회할 결제대행사 현황의 시작 시간
	 * @param until
	 * 조회할 결제대행사 현황의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 * @param excludeCancelled
	 * 결제취소건 제외 여부
	 *
	 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getPgCompanyChart: (
		/**
		 * 조회할 결제대행사 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제대행사 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
	) => Promise<AnalyticsPgCompanyChart>
	/**
	 * 고객사의 결제대행사별 거래 추이를 조회합니다.
	 *
	 * @param from
	 * 조회할 결제대행사별 거래 추이의 시작 시간
	 * @param until
	 * 조회할 결제대행사별 거래 추이의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 * @param excludeCancelled
	 * 결제취소건 제외 여부
	 *
	 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
	 * @param timeGranularity
	 * 결제 결제대행사별 거래 추이 조회 단위
	 *
	 * 시간별, 월별 단위만 지원됩니다.
	 * @param pgCompanies
	 * 조회할 결제대행사
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getPgCompanyTrendChart: (
		/**
		 * 조회할 결제대행사별 거래 추이의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제대행사별 거래 추이의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 결제 결제대행사별 거래 추이 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
		/** 조회할 결제대행사 */
		pgCompanies: PgCompany[],
	) => Promise<AnalyticsPgCompanyTrendChart>
	/**
	 * 고객사의 해외 결제 사용 여부를 조회합니다.
	 *
	 *
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getAnalyticsOverseasPaymentUsage: (
	) => Promise<AnalyticsOverseasPaymentUsage>
	/**
	 * 고객사의 환불율을 조회합니다.
	 *
	 * @param from
	 * 환불율 조회 기간의 시작 시간
	 * @param until
	 * 환불율 조회 기간의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getAnalyticsCancellationRate: (
		/**
		 * 환불율 조회 기간의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 환불율 조회 기간의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
	) => Promise<AnalyticsCancellationRate>
	/**
	 * 고객사의 결제상태 이력 집계를 조회합니다.
	 *
	 * @param from
	 * 조회할 결제 현황의 시작 시간
	 * @param until
	 * 조회할 결제 현황의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getPaymentStatusChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
	) => Promise<AnalyticsPaymentStatusChart>
	/**
	 * 고객사의 결제수단별 결제전환율을 조회합니다.
	 *
	 * @param from
	 * 조회할 결제 현황의 시작 시간
	 * @param until
	 * 조회할 결제 현황의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getPaymentStatusByPaymentMethodChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
	) => Promise<AnalyticsPaymentStatusByPaymentMethodChart>
	/**
	 * 고객사의 PG사별 결제전환율을 조회합니다.
	 *
	 * @param from
	 * 조회할 결제 현황의 시작 시간
	 * @param until
	 * 조회할 결제 현황의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getPaymentStatusByPgCompanyChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
	) => Promise<AnalyticsPaymentStatusByPgCompanyChart>
	/**
	 * 고객사의 결제환경별 결제전환율을 조회합니다.
	 *
	 * @param from
	 * 조회할 결제 현황의 시작 시간
	 * @param until
	 * 조회할 결제 현황의 끝 시간
	 * @param currency
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getPaymentStatusByPaymentClientChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
	) => Promise<AnalyticsPaymentStatusByPaymentClientChart>
}

