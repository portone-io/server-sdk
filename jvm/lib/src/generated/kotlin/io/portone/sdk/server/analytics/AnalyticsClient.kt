package io.portone.sdk.server.analytics

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.request.`get`
import io.ktor.client.request.accept
import io.ktor.client.request.headers
import io.ktor.http.ContentType
import io.ktor.http.HttpHeaders
import io.ktor.http.appendPathSegments
import io.ktor.http.userAgent
import io.portone.sdk.server.USER_AGENT
import io.portone.sdk.server.analytics.AnalyticsAverageAmountChart
import io.portone.sdk.server.analytics.AnalyticsCancellationRate
import io.portone.sdk.server.analytics.AnalyticsCardChart
import io.portone.sdk.server.analytics.AnalyticsCardCompanyChart
import io.portone.sdk.server.analytics.AnalyticsEasyPayChart
import io.portone.sdk.server.analytics.AnalyticsEasyPayProviderChart
import io.portone.sdk.server.analytics.AnalyticsOverseasPaymentUsage
import io.portone.sdk.server.analytics.AnalyticsPaymentChart
import io.portone.sdk.server.analytics.AnalyticsPaymentChartInsight
import io.portone.sdk.server.analytics.AnalyticsPaymentMethodChart
import io.portone.sdk.server.analytics.AnalyticsPaymentMethodTrendChart
import io.portone.sdk.server.analytics.AnalyticsPaymentStatusByPaymentClientChart
import io.portone.sdk.server.analytics.AnalyticsPaymentStatusByPaymentMethodChart
import io.portone.sdk.server.analytics.AnalyticsPaymentStatusByPgCompanyChart
import io.portone.sdk.server.analytics.AnalyticsPaymentStatusChart
import io.portone.sdk.server.analytics.AnalyticsPgCompanyChart
import io.portone.sdk.server.analytics.AnalyticsPgCompanyTrendChart
import io.portone.sdk.server.analytics.AnalyticsTimeGranularity
import io.portone.sdk.server.analytics.CardCompany
import io.portone.sdk.server.analytics.GetAnalyticsAverageAmountChartBody
import io.portone.sdk.server.analytics.GetAnalyticsCancellationRateBody
import io.portone.sdk.server.analytics.GetAnalyticsCardChartBody
import io.portone.sdk.server.analytics.GetAnalyticsCardCompanyChartBody
import io.portone.sdk.server.analytics.GetAnalyticsEasyPayChartBody
import io.portone.sdk.server.analytics.GetAnalyticsEasyPayProviderChartBody
import io.portone.sdk.server.analytics.GetAnalyticsPaymentChartBody
import io.portone.sdk.server.analytics.GetAnalyticsPaymentChartInsightBody
import io.portone.sdk.server.analytics.GetAnalyticsPaymentMethodChartBody
import io.portone.sdk.server.analytics.GetAnalyticsPaymentMethodTrendChartBody
import io.portone.sdk.server.analytics.GetAnalyticsPaymentStatusByPaymentClientChartBody
import io.portone.sdk.server.analytics.GetAnalyticsPaymentStatusByPaymentMethodChartBody
import io.portone.sdk.server.analytics.GetAnalyticsPaymentStatusByPgCompanyChartBody
import io.portone.sdk.server.analytics.GetAnalyticsPaymentStatusChartBody
import io.portone.sdk.server.analytics.GetAnalyticsPgCompanyChartBody
import io.portone.sdk.server.analytics.GetAnalyticsPgCompanyTrendChartBody
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.EasyPayProvider
import io.portone.sdk.server.common.PgCompany
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetAnalyticsCancellationRateError
import io.portone.sdk.server.errors.GetAnalyticsCardChartError
import io.portone.sdk.server.errors.GetAnalyticsCardCompanyChartError
import io.portone.sdk.server.errors.GetAnalyticsEasyPayChartError
import io.portone.sdk.server.errors.GetAnalyticsEasyPayProviderChartError
import io.portone.sdk.server.errors.GetAnalyticsOverseasPaymentUsageError
import io.portone.sdk.server.errors.GetAnalyticsPaymentChartError
import io.portone.sdk.server.errors.GetAnalyticsPaymentChartInsightError
import io.portone.sdk.server.errors.GetAverageAmountChartError
import io.portone.sdk.server.errors.GetPaymentMethodChartError
import io.portone.sdk.server.errors.GetPaymentMethodTrendChartError
import io.portone.sdk.server.errors.GetPaymentStatusByPaymentClientChartError
import io.portone.sdk.server.errors.GetPaymentStatusByPaymentMethodChartError
import io.portone.sdk.server.errors.GetPaymentStatusByPgCompanyChartError
import io.portone.sdk.server.errors.GetPaymentStatusChartError
import io.portone.sdk.server.errors.GetPgCompanyChartError
import io.portone.sdk.server.errors.GetPgCompanyTrendChartError
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import java.io.Closeable
import java.time.Instant
import java.util.concurrent.CompletableFuture
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json

public class AnalyticsClient internal constructor(
  private val apiSecret: String,
  private val apiBase: String,
  private val storeId: String?,
) {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getAnalyticsPaymentChartSuspend")
  public suspend fun getAnalyticsPaymentChart(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean? = null,
    timeGranularity: AnalyticsTimeGranularity,
  ): AnalyticsPaymentChart {
    val requestBody = GetAnalyticsPaymentChartBody(
      from = from,
      until = until,
      currency = currency,
      excludeCancelled = excludeCancelled,
      timeGranularity = timeGranularity,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "payment")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetAnalyticsPaymentChartError>(httpBody)
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
      json.decodeFromString<AnalyticsPaymentChart>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getAnalyticsPaymentChart")
  public suspend fun getAnalyticsPaymentChartFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean? = null,
    timeGranularity: AnalyticsTimeGranularity,
  ): CompletableFuture<AnalyticsPaymentChart> = GlobalScope.future { getAnalyticsPaymentChart(from, until, currency, excludeCancelled, timeGranularity) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getAnalyticsPaymentChartInsightSuspend")
  public suspend fun getAnalyticsPaymentChartInsight(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean? = null,
    timezoneHourOffset: Int,
  ): AnalyticsPaymentChartInsight {
    val requestBody = GetAnalyticsPaymentChartInsightBody(
      from = from,
      until = until,
      currency = currency,
      excludeCancelled = excludeCancelled,
      timezoneHourOffset = timezoneHourOffset,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "payment-insight")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetAnalyticsPaymentChartInsightError>(httpBody)
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
      json.decodeFromString<AnalyticsPaymentChartInsight>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getAnalyticsPaymentChartInsight")
  public suspend fun getAnalyticsPaymentChartInsightFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean? = null,
    timezoneHourOffset: Int,
  ): CompletableFuture<AnalyticsPaymentChartInsight> = GlobalScope.future { getAnalyticsPaymentChartInsight(from, until, currency, excludeCancelled, timezoneHourOffset) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getAverageAmountChartSuspend")
  public suspend fun getAverageAmountChart(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
    timeGranularity: AnalyticsTimeGranularity,
  ): AnalyticsAverageAmountChart {
    val requestBody = GetAnalyticsAverageAmountChartBody(
      from = from,
      until = until,
      currency = currency,
      excludeCancelled = excludeCancelled,
      timeGranularity = timeGranularity,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "average-amount")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetAverageAmountChartError>(httpBody)
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
      json.decodeFromString<AnalyticsAverageAmountChart>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getAverageAmountChart")
  public suspend fun getAverageAmountChartFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
    timeGranularity: AnalyticsTimeGranularity,
  ): CompletableFuture<AnalyticsAverageAmountChart> = GlobalScope.future { getAverageAmountChart(from, until, currency, excludeCancelled, timeGranularity) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPaymentMethodChartSuspend")
  public suspend fun getPaymentMethodChart(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
  ): AnalyticsPaymentMethodChart {
    val requestBody = GetAnalyticsPaymentMethodChartBody(
      from = from,
      until = until,
      currency = currency,
      excludeCancelled = excludeCancelled,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "payment-method")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPaymentMethodChartError>(httpBody)
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
      json.decodeFromString<AnalyticsPaymentMethodChart>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPaymentMethodChart")
  public suspend fun getPaymentMethodChartFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
  ): CompletableFuture<AnalyticsPaymentMethodChart> = GlobalScope.future { getPaymentMethodChart(from, until, currency, excludeCancelled) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPaymentMethodTrendChartSuspend")
  public suspend fun getPaymentMethodTrendChart(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
    timeGranularity: AnalyticsTimeGranularity,
  ): AnalyticsPaymentMethodTrendChart {
    val requestBody = GetAnalyticsPaymentMethodTrendChartBody(
      from = from,
      until = until,
      currency = currency,
      excludeCancelled = excludeCancelled,
      timeGranularity = timeGranularity,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "payment-method-trend")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPaymentMethodTrendChartError>(httpBody)
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
      json.decodeFromString<AnalyticsPaymentMethodTrendChart>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPaymentMethodTrendChart")
  public suspend fun getPaymentMethodTrendChartFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
    timeGranularity: AnalyticsTimeGranularity,
  ): CompletableFuture<AnalyticsPaymentMethodTrendChart> = GlobalScope.future { getPaymentMethodTrendChart(from, until, currency, excludeCancelled, timeGranularity) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getAnalyticsCardChartSuspend")
  public suspend fun getAnalyticsCardChart(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
    timeGranularity: AnalyticsTimeGranularity,
  ): AnalyticsCardChart {
    val requestBody = GetAnalyticsCardChartBody(
      from = from,
      until = until,
      currency = currency,
      excludeCancelled = excludeCancelled,
      timeGranularity = timeGranularity,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "card")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetAnalyticsCardChartError>(httpBody)
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
      json.decodeFromString<AnalyticsCardChart>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getAnalyticsCardChart")
  public suspend fun getAnalyticsCardChartFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
    timeGranularity: AnalyticsTimeGranularity,
  ): CompletableFuture<AnalyticsCardChart> = GlobalScope.future { getAnalyticsCardChart(from, until, currency, excludeCancelled, timeGranularity) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getAnalyticsCardCompanyChartSuspend")
  public suspend fun getAnalyticsCardCompanyChart(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
    timeGranularity: AnalyticsTimeGranularity,
    cardCompanies: List<CardCompany>,
    excludesFromRemainders: List<CardCompany>,
  ): AnalyticsCardCompanyChart {
    val requestBody = GetAnalyticsCardCompanyChartBody(
      from = from,
      until = until,
      currency = currency,
      excludeCancelled = excludeCancelled,
      timeGranularity = timeGranularity,
      cardCompanies = cardCompanies,
      excludesFromRemainders = excludesFromRemainders,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "card-company")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetAnalyticsCardCompanyChartError>(httpBody)
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
      json.decodeFromString<AnalyticsCardCompanyChart>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getAnalyticsCardCompanyChart")
  public suspend fun getAnalyticsCardCompanyChartFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
    timeGranularity: AnalyticsTimeGranularity,
    cardCompanies: List<CardCompany>,
    excludesFromRemainders: List<CardCompany>,
  ): CompletableFuture<AnalyticsCardCompanyChart> = GlobalScope.future { getAnalyticsCardCompanyChart(from, until, currency, excludeCancelled, timeGranularity, cardCompanies, excludesFromRemainders) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getAnalyticsEasyPayChartSuspend")
  public suspend fun getAnalyticsEasyPayChart(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
    timeGranularity: AnalyticsTimeGranularity,
  ): AnalyticsEasyPayChart {
    val requestBody = GetAnalyticsEasyPayChartBody(
      from = from,
      until = until,
      currency = currency,
      excludeCancelled = excludeCancelled,
      timeGranularity = timeGranularity,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "easy-pay")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetAnalyticsEasyPayChartError>(httpBody)
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
      json.decodeFromString<AnalyticsEasyPayChart>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getAnalyticsEasyPayChart")
  public suspend fun getAnalyticsEasyPayChartFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
    timeGranularity: AnalyticsTimeGranularity,
  ): CompletableFuture<AnalyticsEasyPayChart> = GlobalScope.future { getAnalyticsEasyPayChart(from, until, currency, excludeCancelled, timeGranularity) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getAnalyticsEasyPayProviderChartSuspend")
  public suspend fun getAnalyticsEasyPayProviderChart(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
    timeGranularity: AnalyticsTimeGranularity,
    easyPayProviders: List<EasyPayProvider>,
    excludesFromRemainders: List<EasyPayProvider>,
  ): AnalyticsEasyPayProviderChart {
    val requestBody = GetAnalyticsEasyPayProviderChartBody(
      from = from,
      until = until,
      currency = currency,
      excludeCancelled = excludeCancelled,
      timeGranularity = timeGranularity,
      easyPayProviders = easyPayProviders,
      excludesFromRemainders = excludesFromRemainders,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "easy-pay-provider")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetAnalyticsEasyPayProviderChartError>(httpBody)
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
      json.decodeFromString<AnalyticsEasyPayProviderChart>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getAnalyticsEasyPayProviderChart")
  public suspend fun getAnalyticsEasyPayProviderChartFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
    timeGranularity: AnalyticsTimeGranularity,
    easyPayProviders: List<EasyPayProvider>,
    excludesFromRemainders: List<EasyPayProvider>,
  ): CompletableFuture<AnalyticsEasyPayProviderChart> = GlobalScope.future { getAnalyticsEasyPayProviderChart(from, until, currency, excludeCancelled, timeGranularity, easyPayProviders, excludesFromRemainders) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPgCompanyChartSuspend")
  public suspend fun getPgCompanyChart(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
  ): AnalyticsPgCompanyChart {
    val requestBody = GetAnalyticsPgCompanyChartBody(
      from = from,
      until = until,
      currency = currency,
      excludeCancelled = excludeCancelled,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "pg-company")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPgCompanyChartError>(httpBody)
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
      json.decodeFromString<AnalyticsPgCompanyChart>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPgCompanyChart")
  public suspend fun getPgCompanyChartFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
  ): CompletableFuture<AnalyticsPgCompanyChart> = GlobalScope.future { getPgCompanyChart(from, until, currency, excludeCancelled) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPgCompanyTrendChartSuspend")
  public suspend fun getPgCompanyTrendChart(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
    timeGranularity: AnalyticsTimeGranularity,
    pgCompanies: List<PgCompany>,
  ): AnalyticsPgCompanyTrendChart {
    val requestBody = GetAnalyticsPgCompanyTrendChartBody(
      from = from,
      until = until,
      currency = currency,
      excludeCancelled = excludeCancelled,
      timeGranularity = timeGranularity,
      pgCompanies = pgCompanies,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "pg-company-trend")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPgCompanyTrendChartError>(httpBody)
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
      json.decodeFromString<AnalyticsPgCompanyTrendChart>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPgCompanyTrendChart")
  public suspend fun getPgCompanyTrendChartFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
    excludeCancelled: Boolean,
    timeGranularity: AnalyticsTimeGranularity,
    pgCompanies: List<PgCompany>,
  ): CompletableFuture<AnalyticsPgCompanyTrendChart> = GlobalScope.future { getPgCompanyTrendChart(from, until, currency, excludeCancelled, timeGranularity, pgCompanies) }


  /**
   * 고객사의 해외 결제 사용 여부를 조회합니다.
   *
   *
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getAnalyticsOverseasPaymentUsageSuspend")
  public suspend fun getAnalyticsOverseasPaymentUsage(
  ): AnalyticsOverseasPaymentUsage {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "overseas-payment-usage")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetAnalyticsOverseasPaymentUsageError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<AnalyticsOverseasPaymentUsage>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getAnalyticsOverseasPaymentUsage")
  public suspend fun getAnalyticsOverseasPaymentUsageFuture(
  ): CompletableFuture<AnalyticsOverseasPaymentUsage> = GlobalScope.future { getAnalyticsOverseasPaymentUsage() }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getAnalyticsCancellationRateSuspend")
  public suspend fun getAnalyticsCancellationRate(
    `from`: Instant,
    until: Instant,
    currency: Currency,
  ): AnalyticsCancellationRate {
    val requestBody = GetAnalyticsCancellationRateBody(
      from = from,
      until = until,
      currency = currency,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "cancellation-rate")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetAnalyticsCancellationRateError>(httpBody)
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
      json.decodeFromString<AnalyticsCancellationRate>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getAnalyticsCancellationRate")
  public suspend fun getAnalyticsCancellationRateFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
  ): CompletableFuture<AnalyticsCancellationRate> = GlobalScope.future { getAnalyticsCancellationRate(from, until, currency) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPaymentStatusChartSuspend")
  public suspend fun getPaymentStatusChart(
    `from`: Instant,
    until: Instant,
    currency: Currency,
  ): AnalyticsPaymentStatusChart {
    val requestBody = GetAnalyticsPaymentStatusChartBody(
      from = from,
      until = until,
      currency = currency,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "payment-status")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPaymentStatusChartError>(httpBody)
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
      json.decodeFromString<AnalyticsPaymentStatusChart>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPaymentStatusChart")
  public suspend fun getPaymentStatusChartFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
  ): CompletableFuture<AnalyticsPaymentStatusChart> = GlobalScope.future { getPaymentStatusChart(from, until, currency) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPaymentStatusByPaymentMethodChartSuspend")
  public suspend fun getPaymentStatusByPaymentMethodChart(
    `from`: Instant,
    until: Instant,
    currency: Currency,
  ): AnalyticsPaymentStatusByPaymentMethodChart {
    val requestBody = GetAnalyticsPaymentStatusByPaymentMethodChartBody(
      from = from,
      until = until,
      currency = currency,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "payment-status", "by-method")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPaymentStatusByPaymentMethodChartError>(httpBody)
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
      json.decodeFromString<AnalyticsPaymentStatusByPaymentMethodChart>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPaymentStatusByPaymentMethodChart")
  public suspend fun getPaymentStatusByPaymentMethodChartFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
  ): CompletableFuture<AnalyticsPaymentStatusByPaymentMethodChart> = GlobalScope.future { getPaymentStatusByPaymentMethodChart(from, until, currency) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPaymentStatusByPgCompanyChartSuspend")
  public suspend fun getPaymentStatusByPgCompanyChart(
    `from`: Instant,
    until: Instant,
    currency: Currency,
  ): AnalyticsPaymentStatusByPgCompanyChart {
    val requestBody = GetAnalyticsPaymentStatusByPgCompanyChartBody(
      from = from,
      until = until,
      currency = currency,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "payment-status", "by-pg-company")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPaymentStatusByPgCompanyChartError>(httpBody)
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
      json.decodeFromString<AnalyticsPaymentStatusByPgCompanyChart>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPaymentStatusByPgCompanyChart")
  public suspend fun getPaymentStatusByPgCompanyChartFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
  ): CompletableFuture<AnalyticsPaymentStatusByPgCompanyChart> = GlobalScope.future { getPaymentStatusByPgCompanyChart(from, until, currency) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPaymentStatusByPaymentClientChartSuspend")
  public suspend fun getPaymentStatusByPaymentClientChart(
    `from`: Instant,
    until: Instant,
    currency: Currency,
  ): AnalyticsPaymentStatusByPaymentClientChart {
    val requestBody = GetAnalyticsPaymentStatusByPaymentClientChartBody(
      from = from,
      until = until,
      currency = currency,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("analytics", "charts", "payment-status", "by-payment-client")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<GetPaymentStatusByPaymentClientChartError>(httpBody)
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
      json.decodeFromString<AnalyticsPaymentStatusByPaymentClientChart>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPaymentStatusByPaymentClientChart")
  public suspend fun getPaymentStatusByPaymentClientChartFuture(
    `from`: Instant,
    until: Instant,
    currency: Currency,
  ): CompletableFuture<AnalyticsPaymentStatusByPaymentClientChart> = GlobalScope.future { getPaymentStatusByPaymentClientChart(from, until, currency) }

  internal fun close() {
    client.close()
  }
}
