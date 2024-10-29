package io.portone.sdk.server.identityverification

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
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
import io.portone.sdk.server.errors.ChannelNotFoundError
import io.portone.sdk.server.errors.ChannelNotFoundException
import io.portone.sdk.server.errors.ConfirmIdentityVerificationError
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetIdentityVerificationError
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
import io.portone.sdk.server.errors.SendIdentityVerificationError
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.identityverification.ConfirmIdentityVerificationBody
import io.portone.sdk.server.identityverification.ConfirmIdentityVerificationResponse
import io.portone.sdk.server.identityverification.IdentityVerification
import io.portone.sdk.server.identityverification.IdentityVerificationMethod
import io.portone.sdk.server.identityverification.IdentityVerificationOperator
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

public class IdentityVerificationClient internal constructor(
  private val apiSecret: String,
  private val apiBase: String,
  private val storeId: String?,
) {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 본인인증 단건 조회
   *
   * 주어진 아이디에 대응되는 본인인증 내역을 조회합니다.
   *
   * @param identityVerificationId
   * 조회할 본인인증 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws IdentityVerificationNotFoundException 요청된 본인인증 건이 존재하지 않는 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getIdentityVerificationSuspend")
  public suspend fun getIdentityVerification(
    identityVerificationId: String,
  ): IdentityVerification {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("identity-verifications", identityVerificationId.toString())
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
        json.decodeFromString<GetIdentityVerificationError>(httpBody)
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
   * @throws ChannelNotFoundException 요청된 채널이 존재하지 않는 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws IdentityVerificationAlreadySentException 본인인증 건이 이미 API로 요청된 상태인 경우
   * @throws IdentityVerificationAlreadyVerifiedException 본인인증 건이 이미 인증 완료된 상태인 경우
   * @throws IdentityVerificationNotFoundException 요청된 본인인증 건이 존재하지 않는 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws MaxTransactionCountReachedException 결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
   * @throws PgProviderException PG사에서 오류를 전달한 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
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
        appendPathSegments("identity-verifications", identityVerificationId.toString(), "send")
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
        json.decodeFromString<SendIdentityVerificationError>(httpBody)
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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws IdentityVerificationAlreadyVerifiedException 본인인증 건이 이미 인증 완료된 상태인 경우
   * @throws IdentityVerificationNotFoundException 요청된 본인인증 건이 존재하지 않는 경우
   * @throws IdentityVerificationNotSentException 본인인증 건이 API로 요청된 상태가 아닌 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PgProviderException PG사에서 오류를 전달한 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
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
        appendPathSegments("identity-verifications", identityVerificationId.toString(), "confirm")
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
        json.decodeFromString<ConfirmIdentityVerificationError>(httpBody)
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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws IdentityVerificationAlreadyVerifiedException 본인인증 건이 이미 인증 완료된 상태인 경우
   * @throws IdentityVerificationNotFoundException 요청된 본인인증 건이 존재하지 않는 경우
   * @throws IdentityVerificationNotSentException 본인인증 건이 API로 요청된 상태가 아닌 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PgProviderException PG사에서 오류를 전달한 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("resendIdentityVerificationSuspend")
  public suspend fun resendIdentityVerification(
    identityVerificationId: String,
  ): ResendIdentityVerificationResponse {
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("identity-verifications", identityVerificationId.toString(), "resend")
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
        json.decodeFromString<ResendIdentityVerificationError>(httpBody)
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

  internal fun close() {
    client.close()
  }
}
