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
import io.portone.sdk.server.common.CustomerInput
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.errors.BillingKeyAlreadyDeletedError
import io.portone.sdk.server.errors.BillingKeyAlreadyDeletedException
import io.portone.sdk.server.errors.BillingKeyNotFoundError
import io.portone.sdk.server.errors.BillingKeyNotFoundException
import io.portone.sdk.server.errors.BillingKeyNotIssuedError
import io.portone.sdk.server.errors.BillingKeyNotIssuedException
import io.portone.sdk.server.errors.ChannelNotFoundError
import io.portone.sdk.server.errors.ChannelNotFoundException
import io.portone.sdk.server.errors.ChannelSpecificError
import io.portone.sdk.server.errors.ChannelSpecificException
import io.portone.sdk.server.errors.DeleteBillingKeyError
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetBillingKeyInfoError
import io.portone.sdk.server.errors.GetBillingKeyInfosError
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.IssueBillingKeyError
import io.portone.sdk.server.errors.PaymentScheduleAlreadyExistsError
import io.portone.sdk.server.errors.PaymentScheduleAlreadyExistsException
import io.portone.sdk.server.errors.PgProviderError
import io.portone.sdk.server.errors.PgProviderException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.payment.billingkey.BillingKeyFilterInput
import io.portone.sdk.server.payment.billingkey.BillingKeyInfo
import io.portone.sdk.server.payment.billingkey.BillingKeySortInput
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

public class BillingKeyClient(
  private val apiSecret: String,
  private val apiBase: String,
  private val storeId: String?,
) : Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 빌링키 단건 조회
   *
   * 주어진 빌링키에 대응되는 빌링키 정보를 조회합니다.
   *
   * @param billingKey
   * 조회할 빌링키
   *
   * @throws BillingKeyNotFoundException 빌링키가 존재하지 않는 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
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
        json.decodeFromString<GetBillingKeyInfoError>(httpBody)
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
  public suspend fun getBillingKeyInfoFuture(
    billingKey: String,
  ): CompletableFuture<BillingKeyInfo> = GlobalScope.future { getBillingKeyInfo(billingKey) }


  /**
   * 빌링키 삭제
   *
   * 빌링키를 삭제합니다.
   *
   * @param billingKey
   * 삭제할 빌링키
   *
   * @throws BillingKeyAlreadyDeletedException 빌링키가 이미 삭제된 경우
   * @throws BillingKeyNotFoundException 빌링키가 존재하지 않는 경우
   * @throws BillingKeyNotIssuedException BillingKeyNotIssuedError
   * @throws ChannelSpecificException 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PaymentScheduleAlreadyExistsException 결제 예약건이 이미 존재하는 경우
   * @throws PgProviderException PG사에서 오류를 전달한 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("deleteBillingKeySuspend")
  public suspend fun deleteBillingKey(
    billingKey: String,
  ): DeleteBillingKeyResponse {
    val httpResponse = client.delete(apiBase) {
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
        json.decodeFromString<DeleteBillingKeyError>(httpBody)
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
  public suspend fun deleteBillingKeyFuture(
    billingKey: String,
  ): CompletableFuture<DeleteBillingKeyResponse> = GlobalScope.future { deleteBillingKey(billingKey) }


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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
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
        json.decodeFromString<GetBillingKeyInfosError>(httpBody)
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
  public suspend fun getBillingKeyInfosFuture(
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
   * @throws ChannelNotFoundException 요청된 채널이 존재하지 않는 경우
   * @throws ChannelSpecificException 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PgProviderException PG사에서 오류를 전달한 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
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
        json.decodeFromString<IssueBillingKeyError>(httpBody)
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
  public suspend fun issueBillingKeyFuture(
    method: InstantBillingKeyPaymentMethodInput,
    channelKey: String? = null,
    channelGroupId: String? = null,
    customer: CustomerInput? = null,
    customData: String? = null,
    bypass: JsonObject? = null,
    noticeUrls: List<String>? = null,
  ): CompletableFuture<IssueBillingKeyResponse> = GlobalScope.future { issueBillingKey(method, channelKey, channelGroupId, customer, customData, bypass, noticeUrls) }

  override fun close() {
    client.close()
  }
}
