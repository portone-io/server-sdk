package io.portone.sdk.server.reconciliation

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.plugins.HttpTimeout
import io.ktor.client.request.`get`
import io.ktor.client.request.accept
import io.ktor.client.request.headers
import io.ktor.http.ContentType
import io.ktor.http.HttpHeaders
import io.ktor.http.appendPathSegments
import io.ktor.http.userAgent
import io.portone.sdk.server.USER_AGENT
import io.portone.sdk.server.annotations.PortOneUnstable
import io.portone.sdk.server.common.DateRange
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetPaymentReconciliationSettlementVatReportError
import io.portone.sdk.server.errors.GetPaymentReconciliationSettlementVatReportException
import io.portone.sdk.server.errors.GetPaymentReconciliationTransactionVatReportError
import io.portone.sdk.server.errors.GetPaymentReconciliationTransactionVatReportException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.reconciliation.GetPaymentReconciliationSettlementVatReportBody
import io.portone.sdk.server.reconciliation.GetPaymentReconciliationSettlementVatReportResponse
import io.portone.sdk.server.reconciliation.GetPaymentReconciliationTransactionVatReportBody
import io.portone.sdk.server.reconciliation.GetPaymentReconciliationTransactionVatReportResponse
import io.portone.sdk.server.reconciliation.PaymentReconciliationSettlementSummaryFilterInput
import io.portone.sdk.server.reconciliation.PaymentReconciliationTransactionSummaryFilterInput
import java.io.Closeable
import java.util.concurrent.CompletableFuture
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json

/**
 * API Secret을 사용해 포트원 API 클라이언트를 생성합니다.
 *
 * @param apiSecret 포트원 API Secret입니다.
 * @param apiBase 포트원 REST API 주소입니다. 기본값은 `"https://api.portone.io"`입니다.
 * @param storeId 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.
 */
public class ReconciliationClient(
  private val apiSecret: String,
  private val apiBase: String = "https://api.portone.io",
  private val storeId: String? = null,
): Closeable {
  private val client: HttpClient = HttpClient(OkHttp) {
    install(HttpTimeout) {
      requestTimeoutMillis = 60_000
      connectTimeoutMillis = 60_000
      socketTimeoutMillis = 60_000
    }
  }

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 정산일 기준 부가세 내역 조회
   *
   * @param dateRange
   * 정산일 범위
   * @param filter
   *
   *
   * @throws GetPaymentReconciliationSettlementVatReportException
   */
  @PortOneUnstable
  @JvmName("getPaymentReconciliationSettlementVatReportSuspend")
  public suspend fun getPaymentReconciliationSettlementVatReport(
    dateRange: DateRange,
    filter: PaymentReconciliationSettlementSummaryFilterInput? = null,
  ): GetPaymentReconciliationSettlementVatReportResponse {
    val requestBody = GetPaymentReconciliationSettlementVatReportBody(
      dateRange = dateRange,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("payment-reconciliations", "settlements", "vat-report")
        this.parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPaymentReconciliationSettlementVatReportError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetPaymentReconciliationSettlementVatReportResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("getPaymentReconciliationSettlementVatReport")
  public fun getPaymentReconciliationSettlementVatReportFuture(
    dateRange: DateRange,
    filter: PaymentReconciliationSettlementSummaryFilterInput? = null,
  ): CompletableFuture<GetPaymentReconciliationSettlementVatReportResponse> = GlobalScope.future { getPaymentReconciliationSettlementVatReport(dateRange, filter) }


  /**
   * 거래일 기준 부가세 내역 조회
   *
   * @param dateRange
   * 거래일 범위
   * @param filter
   *
   *
   * @throws GetPaymentReconciliationTransactionVatReportException
   */
  @PortOneUnstable
  @JvmName("getPaymentReconciliationTransactionVatReportSuspend")
  public suspend fun getPaymentReconciliationTransactionVatReport(
    dateRange: DateRange,
    filter: PaymentReconciliationTransactionSummaryFilterInput? = null,
  ): GetPaymentReconciliationTransactionVatReportResponse {
    val requestBody = GetPaymentReconciliationTransactionVatReportBody(
      dateRange = dateRange,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("payment-reconciliations", "transactions", "vat-report")
        this.parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPaymentReconciliationTransactionVatReportError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetPaymentReconciliationTransactionVatReportResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("getPaymentReconciliationTransactionVatReport")
  public fun getPaymentReconciliationTransactionVatReportFuture(
    dateRange: DateRange,
    filter: PaymentReconciliationTransactionSummaryFilterInput? = null,
  ): CompletableFuture<GetPaymentReconciliationTransactionVatReportResponse> = GlobalScope.future { getPaymentReconciliationTransactionVatReport(dateRange, filter) }

  override fun close() {
    client.close()
  }
}
