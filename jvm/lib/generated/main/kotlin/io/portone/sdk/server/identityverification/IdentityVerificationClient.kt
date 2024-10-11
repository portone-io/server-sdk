package io.portone.sdk.server

import io.ktor.client.HttpClient
import io.portone.sdk.server.ConfirmIdentityVerificationResponse
import io.portone.sdk.server.IdentityVerification
import io.portone.sdk.server.ResendIdentityVerificationResponse
import io.portone.sdk.server.SendIdentityVerificationResponse
import io.portone.sdk.server.identityverification.ConfirmIdentityVerificationResponse
import io.portone.sdk.server.identityverification.IdentityVerification
import io.portone.sdk.server.identityverification.IdentityVerificationMethod
import io.portone.sdk.server.identityverification.IdentityVerificationOperator
import io.portone.sdk.server.identityverification.ResendIdentityVerificationResponse
import io.portone.sdk.server.identityverification.SendIdentityVerificationBodyCustomer
import io.portone.sdk.server.identityverification.SendIdentityVerificationResponse
import java.io.Closeable
import kotlin.String
import kotlinx.serialization.json.Json
import kotlinx.serialization.json.JsonObject

public class IdentityVerificationClient(
  private val apiSecret: String,
  private val storeId: String,
  private val apiBase: String,
) : Closeable {
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
    identityVerificationId: string,
  ): IdentityVerification {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("identity-verifications", identityVerificationId)
        if (storeId != null) parameters.append("storeId", storeId)
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
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getIdentityVerification")
  public suspend fun getIdentityVerificationFuture(
    identityVerificationId: string,
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
   * @throws PgProviderException PG사에서 오류를 전달한 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("sendIdentityVerificationSuspend")
  public suspend fun sendIdentityVerification(
    identityVerificationId: string,
    channelKey: string,
    customer: SendIdentityVerificationBodyCustomer,
    customData: string? = null,
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
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("identity-verifications", identityVerificationId, "send")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
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
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<SendIdentityVerificationResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("sendIdentityVerification")
  public suspend fun sendIdentityVerificationFuture(
    identityVerificationId: string,
    channelKey: string,
    customer: SendIdentityVerificationBodyCustomer,
    customData: string? = null,
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
    identityVerificationId: string,
    otp: string? = null,
  ): ConfirmIdentityVerificationResponse {
    val requestBody = ConfirmIdentityVerificationBody(
      storeId = storeId,
      otp = otp,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("identity-verifications", identityVerificationId, "confirm")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
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
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("confirmIdentityVerification")
  public suspend fun confirmIdentityVerificationFuture(
    identityVerificationId: string,
    otp: string? = null,
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
    identityVerificationId: string,
  ): ResendIdentityVerificationResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("identity-verifications", identityVerificationId, "resend")
        if (storeId != null) parameters.append("storeId", storeId)
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
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("resendIdentityVerification")
  public suspend fun resendIdentityVerificationFuture(
    identityVerificationId: string,
  ): CompletableFuture<ResendIdentityVerificationResponse> = GlobalScope.future { resendIdentityVerification(identityVerificationId) }

  override fun close() {
    client.close()
  }
}
