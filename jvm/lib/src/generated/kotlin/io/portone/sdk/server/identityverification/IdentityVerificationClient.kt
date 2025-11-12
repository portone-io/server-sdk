package io.portone.sdk.server.identityverification

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
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.errors.ChannelNotFoundError
import io.portone.sdk.server.errors.ChannelNotFoundException
import io.portone.sdk.server.errors.ConfirmIdentityVerificationError
import io.portone.sdk.server.errors.ConfirmIdentityVerificationException
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetIdentityVerificationError
import io.portone.sdk.server.errors.GetIdentityVerificationException
import io.portone.sdk.server.errors.GetIdentityVerificationsError
import io.portone.sdk.server.errors.GetIdentityVerificationsException
import io.portone.sdk.server.errors.IdentityVerificationAlreadySentError
import io.portone.sdk.server.errors.IdentityVerificationAlreadySentException
import io.portone.sdk.server.errors.IdentityVerificationAlreadyVerifiedError
import io.portone.sdk.server.errors.IdentityVerificationAlreadyVerifiedException
import io.portone.sdk.server.errors.IdentityVerificationNotFoundError
import io.portone.sdk.server.errors.IdentityVerificationNotFoundException
import io.portone.sdk.server.errors.IdentityVerificationNotSentError
import io.portone.sdk.server.errors.IdentityVerificationNotSentException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.MaxTransactionCountReachedError
import io.portone.sdk.server.errors.MaxTransactionCountReachedException
import io.portone.sdk.server.errors.PgProviderError
import io.portone.sdk.server.errors.PgProviderException
import io.portone.sdk.server.errors.ResendIdentityVerificationError
import io.portone.sdk.server.errors.ResendIdentityVerificationException
import io.portone.sdk.server.errors.SendIdentityVerificationError
import io.portone.sdk.server.errors.SendIdentityVerificationException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.identityverification.ConfirmIdentityVerificationBody
import io.portone.sdk.server.identityverification.ConfirmIdentityVerificationResponse
import io.portone.sdk.server.identityverification.GetIdentityVerificationsBody
import io.portone.sdk.server.identityverification.GetIdentityVerificationsResponse
import io.portone.sdk.server.identityverification.IdentityVerification
import io.portone.sdk.server.identityverification.IdentityVerificationFilterInput
import io.portone.sdk.server.identityverification.IdentityVerificationMethod
import io.portone.sdk.server.identityverification.IdentityVerificationOperator
import io.portone.sdk.server.identityverification.IdentityVerificationSortInput
import io.portone.sdk.server.identityverification.ResendIdentityVerificationResponse
import io.portone.sdk.server.identityverification.SendIdentityVerificationBody
import io.portone.sdk.server.identityverification.SendIdentityVerificationBodyCustomer
import io.portone.sdk.server.identityverification.SendIdentityVerificationResponse
import java.io.Closeable
import java.util.concurrent.CompletableFuture
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
public class IdentityVerificationClient(
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
   * 본인인증 확인
   *
   * 요청된 본인인증에 대한 확인을 진행합니다.
   *
   * @param identityVerificationId
   * 본인인증 아이디
   * @param otp
   * OTP (One-Time Password)
   *
   * SMS 방식에서만 사용됩니다.
   *
   * @throws ConfirmIdentityVerificationException
   */
  @JvmName("confirmIdentityVerificationSuspend")
  public suspend fun confirmIdentityVerification(
    identityVerificationId: String,
    otp: String? = null,
  ): ConfirmIdentityVerificationResponse {
    val requestBody = ConfirmIdentityVerificationBody(
      storeId = storeId,
      otp = otp,
    )
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("identity-verifications", identityVerificationId.toString(), "confirm")
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
        json.decodeFromString<ConfirmIdentityVerificationError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is IdentityVerificationAlreadyVerifiedError -> throw IdentityVerificationAlreadyVerifiedException(httpBodyDecoded)
        is IdentityVerificationNotFoundError -> throw IdentityVerificationNotFoundException(httpBodyDecoded)
        is IdentityVerificationNotSentError -> throw IdentityVerificationNotSentException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ConfirmIdentityVerificationResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("confirmIdentityVerification")
  public fun confirmIdentityVerificationFuture(
    identityVerificationId: String,
    otp: String? = null,
  ): CompletableFuture<ConfirmIdentityVerificationResponse> = GlobalScope.future { confirmIdentityVerification(identityVerificationId, otp) }


  /**
   * SMS 본인인증 요청 재전송
   *
   * SMS 본인인증 요청을 재전송합니다.
   *
   * @param identityVerificationId
   * 본인인증 아이디
   *
   * @throws ResendIdentityVerificationException
   */
  @JvmName("resendIdentityVerificationSuspend")
  public suspend fun resendIdentityVerification(
    identityVerificationId: String,
  ): ResendIdentityVerificationResponse {
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("identity-verifications", identityVerificationId.toString(), "resend")
        if (storeId != null) this.parameters.append("storeId", storeId.toString())
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
        json.decodeFromString<ResendIdentityVerificationError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is IdentityVerificationAlreadyVerifiedError -> throw IdentityVerificationAlreadyVerifiedException(httpBodyDecoded)
        is IdentityVerificationNotFoundError -> throw IdentityVerificationNotFoundException(httpBodyDecoded)
        is IdentityVerificationNotSentError -> throw IdentityVerificationNotSentException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ResendIdentityVerificationResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("resendIdentityVerification")
  public fun resendIdentityVerificationFuture(
    identityVerificationId: String,
  ): CompletableFuture<ResendIdentityVerificationResponse> = GlobalScope.future { resendIdentityVerification(identityVerificationId) }


  /**
   * 본인인증 요청 전송
   *
   * SMS 또는 APP 방식을 이용하여 본인인증 요청을 전송합니다.
   *
   * @param identityVerificationId
   * 본인인증 아이디
   * @param channelKey
   * 채널 키
   * @param customer
   * 고객 정보
   * @param customData
   * 사용자 지정 데이터
   * @param bypass
   * PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)
   * @param operator
   * 통신사
   * @param method
   * 본인인증 방식
   *
   * @throws SendIdentityVerificationException
   */
  @JvmName("sendIdentityVerificationSuspend")
  public suspend fun sendIdentityVerification(
    identityVerificationId: String,
    channelKey: String,
    customer: SendIdentityVerificationBodyCustomer,
    customData: String? = null,
    bypass: JsonObject? = null,
    `operator`: IdentityVerificationOperator,
    method: IdentityVerificationMethod,
  ): SendIdentityVerificationResponse {
    val requestBody = SendIdentityVerificationBody(
      storeId = storeId,
      channelKey = channelKey,
      customer = customer,
      customData = customData,
      bypass = bypass,
      operator = operator,
      method = method,
    )
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("identity-verifications", identityVerificationId.toString(), "send")
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
        json.decodeFromString<SendIdentityVerificationError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ChannelNotFoundError -> throw ChannelNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is IdentityVerificationAlreadySentError -> throw IdentityVerificationAlreadySentException(httpBodyDecoded)
        is IdentityVerificationAlreadyVerifiedError -> throw IdentityVerificationAlreadyVerifiedException(httpBodyDecoded)
        is IdentityVerificationNotFoundError -> throw IdentityVerificationNotFoundException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is MaxTransactionCountReachedError -> throw MaxTransactionCountReachedException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<SendIdentityVerificationResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("sendIdentityVerification")
  public fun sendIdentityVerificationFuture(
    identityVerificationId: String,
    channelKey: String,
    customer: SendIdentityVerificationBodyCustomer,
    customData: String? = null,
    bypass: JsonObject? = null,
    `operator`: IdentityVerificationOperator,
    method: IdentityVerificationMethod,
  ): CompletableFuture<SendIdentityVerificationResponse> = GlobalScope.future { sendIdentityVerification(identityVerificationId, channelKey, customer, customData, bypass, operator, method) }


  /**
   * 본인인증 단건 조회
   *
   * 주어진 아이디에 대응되는 본인인증 내역을 조회합니다.
   *
   * @param identityVerificationId
   * 조회할 본인인증 아이디
   *
   * @throws GetIdentityVerificationException
   */
  @JvmName("getIdentityVerificationSuspend")
  public suspend fun getIdentityVerification(
    identityVerificationId: String,
  ): IdentityVerification {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("identity-verifications", identityVerificationId.toString())
        if (storeId != null) this.parameters.append("storeId", storeId.toString())
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
        json.decodeFromString<GetIdentityVerificationError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is IdentityVerificationNotFoundError -> throw IdentityVerificationNotFoundException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<IdentityVerification>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getIdentityVerification")
  public fun getIdentityVerificationFuture(
    identityVerificationId: String,
  ): CompletableFuture<IdentityVerification> = GlobalScope.future { getIdentityVerification(identityVerificationId) }


  /**
   * 본인인증 내역 다건 조회
   *
   * 주어진 조건에 맞는 본인인증 내역들을 페이지 기반으로 조회합니다.
   *
   * @param page
   * 요청할 페이지 정보
   *
   * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
   * @param sort
   * 정렬 조건
   *
   * 미 입력 시 sortBy: REQUESTED_AT, sortOrder: DESC 으로 기본값이 적용됩니다.
   * @param filter
   * 조회할 본인인증 내역 조건 필터
   *
   * @throws GetIdentityVerificationsException
   */
  @JvmName("getIdentityVerificationsSuspend")
  public suspend fun getIdentityVerifications(
    page: PageInput? = null,
    sort: IdentityVerificationSortInput? = null,
    filter: IdentityVerificationFilterInput? = null,
  ): GetIdentityVerificationsResponse {
    val requestBody = GetIdentityVerificationsBody(
      page = page,
      sort = sort,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("identity-verifications")
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
        json.decodeFromString<GetIdentityVerificationsError.Recognized>(httpBody)
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
      json.decodeFromString<GetIdentityVerificationsResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getIdentityVerifications")
  public fun getIdentityVerificationsFuture(
    page: PageInput? = null,
    sort: IdentityVerificationSortInput? = null,
    filter: IdentityVerificationFilterInput? = null,
  ): CompletableFuture<GetIdentityVerificationsResponse> = GlobalScope.future { getIdentityVerifications(page, sort, filter) }

  override fun close() {
    client.close()
  }
}
