package io.portone.sdk.server.paymentsession

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.plugins.HttpTimeout
import io.ktor.client.request.`get`
import io.ktor.client.request.accept
import io.ktor.client.request.headers
import io.ktor.client.request.post
import io.ktor.client.request.setBody
import io.ktor.http.ContentType
import io.ktor.http.HttpHeaders
import io.ktor.http.appendPathSegments
import io.ktor.http.contentType
import io.ktor.http.userAgent
import io.portone.sdk.server.USER_AGENT
import io.portone.sdk.server.common.CheckoutPaymentMethod
import io.portone.sdk.server.common.Country
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.errors.ClosePaymentSessionError
import io.portone.sdk.server.errors.ClosePaymentSessionException
import io.portone.sdk.server.errors.CreatePaymentSessionError
import io.portone.sdk.server.errors.CreatePaymentSessionException
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetPaymentSessionError
import io.portone.sdk.server.errors.GetPaymentSessionException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.MaxTtlExceededError
import io.portone.sdk.server.errors.MaxTtlExceededException
import io.portone.sdk.server.errors.SessionExpiredError
import io.portone.sdk.server.errors.SessionExpiredException
import io.portone.sdk.server.errors.SessionNotFoundError
import io.portone.sdk.server.errors.SessionNotFoundException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.paymentsession.ClosePaymentSessionResponse
import io.portone.sdk.server.paymentsession.CreatePaymentSessionBody
import io.portone.sdk.server.paymentsession.CreatePaymentSessionResponse
import io.portone.sdk.server.paymentsession.PaymentSession
import io.portone.sdk.server.paymentsession.PaymentSessionAgreement
import io.portone.sdk.server.paymentsession.PaymentSessionColors
import io.portone.sdk.server.paymentsession.PaymentSessionProduct
import java.io.Closeable
import java.util.concurrent.CompletableFuture
import kotlin.String
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
public class PaymentSessionClient(
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
   * 결제 세션 생성
   *
   * 결제 세션을 생성합니다. 호스티드 체크아웃 페이지가 생성되어 URL이 반환됩니다.
   *
   * @param paymentId
   * 결제 건 아이디
   * @param profileKey
   * 프로필 키
   * @param paymentMethod
   * 결제 수단 지정
   *
   * 지정한 경우, 정보 추가 입력이 필요하지 않은 경우에 주문서를 건너뛰고 결제로 바로 이동합니다.
   * @param country
   * 국가
   * @param currency
   * 통화
   * @param totalAmount
   * 전체 결제 금액
   * @param orderName
   * 주문명
   * @param redirectUrl
   * 결제 완료 후 리다이렉트 URL
   *
   * 지정하지 않으면 기본 결과 페이지가 표시됩니다.
   * @param products
   * 주문 항목 목록
   * @param customerName
   * 구매자 이름
   * @param customerEmail
   * 구매자 이메일
   * @param storeName
   * 상점 이름
   *
   * 페이지 헤더 및 결제사 UI에 표시됩니다.
   * @param agreements
   * 사용자 지정 약관 목록
   *
   * 구매자가 모든 약관에 동의해야 결제 버튼이 활성화됩니다.
   * @param orderImageUrl
   * 주문 대표 이미지 URL
   * @param customData
   * 사용자 지정 데이터
   *
   * 결제 완료 후 결제 건 조회에서도 확인할 수 있습니다.
   * @param colors
   * 체크아웃 페이지 색 설정
   * @param ttlSeconds
   * 세션 TTL (초)
   *
   * @throws CreatePaymentSessionException
   */
  @JvmName("createPaymentSessionSuspend")
  public suspend fun createPaymentSession(
    paymentId: String,
    profileKey: String,
    paymentMethod: CheckoutPaymentMethod? = null,
    country: Country,
    currency: Currency,
    totalAmount: Long,
    orderName: String,
    redirectUrl: String? = null,
    products: List<PaymentSessionProduct>? = null,
    customerName: String? = null,
    customerEmail: String? = null,
    storeName: String? = null,
    agreements: List<PaymentSessionAgreement>? = null,
    orderImageUrl: String? = null,
    customData: String? = null,
    colors: PaymentSessionColors? = null,
    ttlSeconds: Long? = null,
  ): CreatePaymentSessionResponse {
    val requestBody = CreatePaymentSessionBody(
      storeId = storeId,
      paymentId = paymentId,
      profileKey = profileKey,
      paymentMethod = paymentMethod,
      country = country,
      currency = currency,
      totalAmount = totalAmount,
      orderName = orderName,
      redirectUrl = redirectUrl,
      products = products,
      customerName = customerName,
      customerEmail = customerEmail,
      storeName = storeName,
      agreements = agreements,
      orderImageUrl = orderImageUrl,
      customData = customData,
      colors = colors,
      ttlSeconds = ttlSeconds,
    )
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("payment-sessions")
      }
      headers {
        this.append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      this.contentType(ContentType.Application.Json)
      this.accept(ContentType.Application.Json)
      this.userAgent(USER_AGENT)
      this.setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<CreatePaymentSessionError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is MaxTtlExceededError -> throw MaxTtlExceededException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreatePaymentSessionResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPaymentSession")
  public fun createPaymentSessionFuture(
    paymentId: String,
    profileKey: String,
    paymentMethod: CheckoutPaymentMethod? = null,
    country: Country,
    currency: Currency,
    totalAmount: Long,
    orderName: String,
    redirectUrl: String? = null,
    products: List<PaymentSessionProduct>? = null,
    customerName: String? = null,
    customerEmail: String? = null,
    storeName: String? = null,
    agreements: List<PaymentSessionAgreement>? = null,
    orderImageUrl: String? = null,
    customData: String? = null,
    colors: PaymentSessionColors? = null,
    ttlSeconds: Long? = null,
  ): CompletableFuture<CreatePaymentSessionResponse> = GlobalScope.future { createPaymentSession(paymentId, profileKey, paymentMethod, country, currency, totalAmount, orderName, redirectUrl, products, customerName, customerEmail, storeName, agreements, orderImageUrl, customData, colors, ttlSeconds) }


  /**
   * 결제 세션 조회
   *
   * 결제 세션을 조회합니다. 인증 헤더 없이 웹 페이지에서도 접근 가능합니다.
   *
   * @param sessionId
   * 결제 세션 아이디
   *
   * @throws GetPaymentSessionException
   */
  @JvmName("getPaymentSessionSuspend")
  public suspend fun getPaymentSession(
    sessionId: String,
  ): PaymentSession {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("payment-sessions", sessionId.toString())
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
        json.decodeFromString<GetPaymentSessionError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is SessionExpiredError -> throw SessionExpiredException(httpBodyDecoded)
        is SessionNotFoundError -> throw SessionNotFoundException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PaymentSession>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPaymentSession")
  public fun getPaymentSessionFuture(
    sessionId: String,
  ): CompletableFuture<PaymentSession> = GlobalScope.future { getPaymentSession(sessionId) }


  /**
   * 결제 세션 종료
   *
   * 결제 세션을 즉시 만료시킵니다. 이후 해당 세션으로는 결제 페이지에 접근할 수 없습니다.
   *
   * @param sessionId
   * 결제 세션 아이디
   *
   * @throws ClosePaymentSessionException
   */
  @JvmName("closePaymentSessionSuspend")
  public suspend fun closePaymentSession(
    sessionId: String,
  ): ClosePaymentSessionResponse {
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("payment-sessions", sessionId.toString(), "close")
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
        json.decodeFromString<ClosePaymentSessionError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is SessionNotFoundError -> throw SessionNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ClosePaymentSessionResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("closePaymentSession")
  public fun closePaymentSessionFuture(
    sessionId: String,
  ): CompletableFuture<ClosePaymentSessionResponse> = GlobalScope.future { closePaymentSession(sessionId) }

  override fun close() {
    client.close()
  }
}
