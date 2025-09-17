package io.portone.sdk.server.payment.billingkey

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.request.`get`
import io.ktor.client.request.accept
import io.ktor.client.request.delete
import io.ktor.client.request.headers
import io.ktor.client.request.post
import io.ktor.client.request.setBody
import io.ktor.http.ContentType
import io.ktor.http.HttpHeaders
import io.ktor.http.appendPathSegments
import io.ktor.http.contentType
import io.ktor.http.userAgent
import io.portone.sdk.server.USER_AGENT
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.CustomerInput
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.errors.BillingKeyAlreadyDeletedError
import io.portone.sdk.server.errors.BillingKeyAlreadyDeletedException
import io.portone.sdk.server.errors.BillingKeyAlreadyIssuedError
import io.portone.sdk.server.errors.BillingKeyAlreadyIssuedException
import io.portone.sdk.server.errors.BillingKeyNotFoundError
import io.portone.sdk.server.errors.BillingKeyNotFoundException
import io.portone.sdk.server.errors.BillingKeyNotIssuedError
import io.portone.sdk.server.errors.BillingKeyNotIssuedException
import io.portone.sdk.server.errors.ChannelNotFoundError
import io.portone.sdk.server.errors.ChannelNotFoundException
import io.portone.sdk.server.errors.ChannelSpecificError
import io.portone.sdk.server.errors.ChannelSpecificException
import io.portone.sdk.server.errors.ConfirmBillingKeyError
import io.portone.sdk.server.errors.ConfirmBillingKeyException
import io.portone.sdk.server.errors.ConfirmBillingKeyIssueAndPayError
import io.portone.sdk.server.errors.ConfirmBillingKeyIssueAndPayException
import io.portone.sdk.server.errors.DeleteBillingKeyError
import io.portone.sdk.server.errors.DeleteBillingKeyException
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetBillingKeyInfoError
import io.portone.sdk.server.errors.GetBillingKeyInfoException
import io.portone.sdk.server.errors.GetBillingKeyInfosError
import io.portone.sdk.server.errors.GetBillingKeyInfosException
import io.portone.sdk.server.errors.InformationMismatchError
import io.portone.sdk.server.errors.InformationMismatchException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.IssueBillingKeyError
import io.portone.sdk.server.errors.IssueBillingKeyException
import io.portone.sdk.server.errors.PaymentScheduleAlreadyExistsError
import io.portone.sdk.server.errors.PaymentScheduleAlreadyExistsException
import io.portone.sdk.server.errors.PgProviderError
import io.portone.sdk.server.errors.PgProviderException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.payment.billingkey.BillingKeyDeleteRequester
import io.portone.sdk.server.payment.billingkey.BillingKeyFilterInput
import io.portone.sdk.server.payment.billingkey.BillingKeyInfo
import io.portone.sdk.server.payment.billingkey.BillingKeySortInput
import io.portone.sdk.server.payment.billingkey.ConfirmBillingKeyBody
import io.portone.sdk.server.payment.billingkey.ConfirmBillingKeyIssueAndPayBody
import io.portone.sdk.server.payment.billingkey.ConfirmedBillingKeyIssueAndPaySummary
import io.portone.sdk.server.payment.billingkey.ConfirmedBillingKeySummary
import io.portone.sdk.server.payment.billingkey.DeleteBillingKeyResponse
import io.portone.sdk.server.payment.billingkey.GetBillingKeyInfosBody
import io.portone.sdk.server.payment.billingkey.GetBillingKeyInfosResponse
import io.portone.sdk.server.payment.billingkey.InstantBillingKeyPaymentMethodInput
import io.portone.sdk.server.payment.billingkey.IssueBillingKeyBody
import io.portone.sdk.server.payment.billingkey.IssueBillingKeyResponse
import java.io.Closeable
import java.util.concurrent.CompletableFuture
import kotlin.Array
import kotlin.String
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import kotlinx.serialization.json.JsonObject

/**
 * API Secret을 사용해 포트원 API 클라이언트를 생성합니다.
 *
 * @param apiSecret 포트원 API Secret입니다.
 * @param apiBase 포트원 REST API 주소입니다. 기본값은 `"https://api.portone.io"`입니다.
 * @param storeId 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.
 */
public class BillingKeyClient(
  private val apiSecret: String,
  private val apiBase: String = "https://api.portone.io",
  private val storeId: String? = null,
): Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 빌링키 다건 조회
   *
   * 주어진 조건에 맞는 빌링키들을 페이지 기반으로 조회합니다.
   *
   * @param page
   * 요청할 페이지 정보
   *
   * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
   * @param sort
   * 정렬 조건
   *
   * 미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
   * @param filter
   * 조회할 빌링키 조건 필터
   *
   * V1 빌링키 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.
   *
   * @throws GetBillingKeyInfosException
   */
  @JvmName("getBillingKeyInfosSuspend")
  public suspend fun getBillingKeyInfos(
    page: PageInput? = null,
    sort: BillingKeySortInput? = null,
    filter: BillingKeyFilterInput? = null,
  ): GetBillingKeyInfosResponse {
    val requestBody = GetBillingKeyInfosBody(
      page = page,
      sort = sort,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("billing-keys")
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
        json.decodeFromString<GetBillingKeyInfosError.Recognized>(httpBody)
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
      json.decodeFromString<GetBillingKeyInfosResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getBillingKeyInfos")
  public fun getBillingKeyInfosFuture(
    page: PageInput? = null,
    sort: BillingKeySortInput? = null,
    filter: BillingKeyFilterInput? = null,
  ): CompletableFuture<GetBillingKeyInfosResponse> = GlobalScope.future { getBillingKeyInfos(page, sort, filter) }


  /**
   * 빌링키 발급
   *
   * 빌링키 발급을 요청합니다.
   *
   * @param method
   * 빌링키 결제 수단 정보
   * @param channelKey
   * 채널 키
   *
   * 채널 키 또는 채널 그룹 ID 필수
   * @param channelGroupId
   * 채널 그룹 ID
   *
   * 채널 키 또는 채널 그룹 ID 필수
   * @param customer
   * 고객 정보
   * @param customData
   * 사용자 지정 데이터
   * @param bypass
   * PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)
   * @param noticeUrls
   * 웹훅 주소
   *
   * 빌링키 발급 시 요청을 받을 웹훅 주소입니다.
   * 상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
   * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
   *
   * @throws IssueBillingKeyException
   */
  @JvmName("issueBillingKeySuspend")
  public suspend fun issueBillingKey(
    method: InstantBillingKeyPaymentMethodInput,
    channelKey: String? = null,
    channelGroupId: String? = null,
    customer: CustomerInput? = null,
    customData: String? = null,
    bypass: JsonObject? = null,
    noticeUrls: List<String>? = null,
  ): IssueBillingKeyResponse {
    val requestBody = IssueBillingKeyBody(
      storeId = storeId,
      method = method,
      channelKey = channelKey,
      channelGroupId = channelGroupId,
      customer = customer,
      customData = customData,
      bypass = bypass,
      noticeUrls = noticeUrls,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("billing-keys")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<IssueBillingKeyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ChannelNotFoundError -> throw ChannelNotFoundException(httpBodyDecoded)
        is ChannelSpecificError -> throw ChannelSpecificException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<IssueBillingKeyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("issueBillingKey")
  public fun issueBillingKeyFuture(
    method: InstantBillingKeyPaymentMethodInput,
    channelKey: String? = null,
    channelGroupId: String? = null,
    customer: CustomerInput? = null,
    customData: String? = null,
    bypass: JsonObject? = null,
    noticeUrls: List<String>? = null,
  ): CompletableFuture<IssueBillingKeyResponse> = GlobalScope.future { issueBillingKey(method, channelKey, channelGroupId, customer, customData, bypass, noticeUrls) }


  /**
   * 빌링키 발급 수동 승인
   *
   * 수동 승인으로 설정된 빌링키 발급에 대해, 빌링키 발급을 완료 처리합니다.
   *
   * @param billingIssueToken
   * 빌링키 발급 토큰
   *
   * 빌링키 발급 요청 완료 시 발급된 토큰입니다.
   * @param isTest
   * 테스트 결제 여부
   *
   * 검증용 파라미터로, 결제 건 테스트 여부와 일치하지 않을 경우 오류가 반환됩니다.
   *
   * @throws ConfirmBillingKeyException
   */
  @JvmName("confirmBillingKeySuspend")
  public suspend fun confirmBillingKey(
    billingIssueToken: String,
    isTest: Boolean? = null,
  ): ConfirmedBillingKeySummary {
    val requestBody = ConfirmBillingKeyBody(
      storeId = storeId,
      billingIssueToken = billingIssueToken,
      isTest = isTest,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("billing-keys", "confirm")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<ConfirmBillingKeyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is BillingKeyAlreadyIssuedError -> throw BillingKeyAlreadyIssuedException(httpBodyDecoded)
        is BillingKeyNotFoundError -> throw BillingKeyNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InformationMismatchError -> throw InformationMismatchException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ConfirmedBillingKeySummary>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("confirmBillingKey")
  public fun confirmBillingKeyFuture(
    billingIssueToken: String,
    isTest: Boolean? = null,
  ): CompletableFuture<ConfirmedBillingKeySummary> = GlobalScope.future { confirmBillingKey(billingIssueToken, isTest) }


  /**
   * 빌링키 발급 및 초회 결제 수동 승인
   *
   * 수동 승인으로 설정된 빌링키 발급 및 초회 결제에 대해, 빌링키 발급과 결제를 완료 처리합니다.
   *
   * @param billingIssueToken
   * 빌링키 발급 토큰
   *
   * 빌링키 발급 및 초회 결제 요청 완료 시 발급된 토큰입니다.
   * @param paymentId
   * 결제 건 아이디
   *
   * 검증용 파라미터로, 결제 건 아이디와 일치하지 않을 경우 오류가 반환됩니다.
   * @param currency
   * 통화
   *
   * 검증용 파라미터로, 결제 건 화폐와 일치하지 않을 경우 오류가 반환됩니다.
   * @param totalAmount
   * 결제 금액
   *
   * 검증용 파라미터로, 결제 건 총 금액과 일치하지 않을 경우 오류가 반환됩니다.
   * @param taxFreeAmount
   * 면세 금액
   *
   * 검증용 파라미터로, 결제 건 면세 금액과 일치하지 않을 경우 오류가 반환됩니다.
   * @param isTest
   * 테스트 결제 여부
   *
   * 검증용 파라미터로, 결제 건 테스트 여부와 일치하지 않을 경우 오류가 반환됩니다.
   *
   * @throws ConfirmBillingKeyIssueAndPayException
   */
  @JvmName("confirmBillingKeyIssueAndPaySuspend")
  public suspend fun confirmBillingKeyIssueAndPay(
    billingIssueToken: String,
    paymentId: String? = null,
    currency: Currency? = null,
    totalAmount: Long? = null,
    taxFreeAmount: Long? = null,
    isTest: Boolean? = null,
  ): ConfirmedBillingKeyIssueAndPaySummary {
    val requestBody = ConfirmBillingKeyIssueAndPayBody(
      storeId = storeId,
      billingIssueToken = billingIssueToken,
      paymentId = paymentId,
      currency = currency,
      totalAmount = totalAmount,
      taxFreeAmount = taxFreeAmount,
      isTest = isTest,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("billing-keys", "confirm-issue-and-pay")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<ConfirmBillingKeyIssueAndPayError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is BillingKeyAlreadyIssuedError -> throw BillingKeyAlreadyIssuedException(httpBodyDecoded)
        is BillingKeyNotFoundError -> throw BillingKeyNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InformationMismatchError -> throw InformationMismatchException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ConfirmedBillingKeyIssueAndPaySummary>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("confirmBillingKeyIssueAndPay")
  public fun confirmBillingKeyIssueAndPayFuture(
    billingIssueToken: String,
    paymentId: String? = null,
    currency: Currency? = null,
    totalAmount: Long? = null,
    taxFreeAmount: Long? = null,
    isTest: Boolean? = null,
  ): CompletableFuture<ConfirmedBillingKeyIssueAndPaySummary> = GlobalScope.future { confirmBillingKeyIssueAndPay(billingIssueToken, paymentId, currency, totalAmount, taxFreeAmount, isTest) }


  /**
   * 빌링키 단건 조회
   *
   * 주어진 빌링키에 대응되는 빌링키 정보를 조회합니다.
   *
   * @param billingKey
   * 조회할 빌링키
   *
   * @throws GetBillingKeyInfoException
   */
  @JvmName("getBillingKeyInfoSuspend")
  public suspend fun getBillingKeyInfo(
    billingKey: String,
  ): BillingKeyInfo {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("billing-keys", billingKey.toString())
        if (storeId != null) parameters.append("storeId", storeId.toString())
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
        json.decodeFromString<GetBillingKeyInfoError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is BillingKeyNotFoundError -> throw BillingKeyNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<BillingKeyInfo>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getBillingKeyInfo")
  public fun getBillingKeyInfoFuture(
    billingKey: String,
  ): CompletableFuture<BillingKeyInfo> = GlobalScope.future { getBillingKeyInfo(billingKey) }


  /**
   * 빌링키 삭제
   *
   * 빌링키를 삭제합니다.
   *
   * @param billingKey
   * 삭제할 빌링키
   * @param reason
   * 사유
   *
   * 네이버페이: 자동결제 해지 사유입니다. 명시가 필요합니다.
   * @param requester
   * 요청 주체
   *
   * 네이버페이: 자동결제 해지 요청 주체입니다. 명시가 필요합니다.
   *
   * @throws DeleteBillingKeyException
   */
  @JvmName("deleteBillingKeySuspend")
  public suspend fun deleteBillingKey(
    billingKey: String,
    reason: String? = null,
    requester: BillingKeyDeleteRequester? = null,
  ): DeleteBillingKeyResponse {
    val httpResponse = client.delete(apiBase) {
      url {
        appendPathSegments("billing-keys", billingKey.toString())
        if (storeId != null) parameters.append("storeId", storeId.toString())
        if (reason != null) parameters.append("reason", reason.toString())
        if (requester != null) parameters.append("requester", requester.toString())
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
        json.decodeFromString<DeleteBillingKeyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is BillingKeyAlreadyDeletedError -> throw BillingKeyAlreadyDeletedException(httpBodyDecoded)
        is BillingKeyNotFoundError -> throw BillingKeyNotFoundException(httpBodyDecoded)
        is BillingKeyNotIssuedError -> throw BillingKeyNotIssuedException(httpBodyDecoded)
        is ChannelSpecificError -> throw ChannelSpecificException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PaymentScheduleAlreadyExistsError -> throw PaymentScheduleAlreadyExistsException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<DeleteBillingKeyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("deleteBillingKey")
  public fun deleteBillingKeyFuture(
    billingKey: String,
    reason: String? = null,
    requester: BillingKeyDeleteRequester? = null,
  ): CompletableFuture<DeleteBillingKeyResponse> = GlobalScope.future { deleteBillingKey(billingKey, reason, requester) }

  override fun close() {
    client.close()
  }
}
