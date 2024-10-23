package io.portone.sdk.server.b2b.contact

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.request.`get`
import io.ktor.client.request.accept
import io.ktor.client.request.headers
import io.ktor.client.request.patch
import io.ktor.client.request.setBody
import io.ktor.http.ContentType
import io.ktor.http.HttpHeaders
import io.ktor.http.appendPathSegments
import io.ktor.http.contentType
import io.ktor.http.userAgent
import io.portone.sdk.server.USER_AGENT
import io.portone.sdk.server.b2b.contact.GetB2bContactIdExistenceResponse
import io.portone.sdk.server.b2b.contact.UpdateB2bContactBody
import io.portone.sdk.server.b2b.contact.UpdateB2bContactResponse
import io.portone.sdk.server.common.B2bCompanyContact
import io.portone.sdk.server.errors.B2bContactNotFoundError
import io.portone.sdk.server.errors.B2bContactNotFoundException
import io.portone.sdk.server.errors.B2bExternalServiceError
import io.portone.sdk.server.errors.B2bExternalServiceException
import io.portone.sdk.server.errors.B2bMemberCompanyNotFoundError
import io.portone.sdk.server.errors.B2bMemberCompanyNotFoundException
import io.portone.sdk.server.errors.B2bNotEnabledError
import io.portone.sdk.server.errors.B2bNotEnabledException
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetB2bContactError
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.errors.UpdateB2bContactError
import io.portone.sdk.server.errors.getB2bContactIdExistenceError
import java.io.Closeable
import java.util.concurrent.CompletableFuture
import kotlin.String
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json

public class ContactClient internal constructor(
  private val apiSecret: String,
  private val apiBase: String,
  private val storeId: String?,
) {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 담당자 조회
   *
   * 연동 사업자에 등록된 담당자를 조회합니다.
   *
   * @param contactId
   * 담당자 ID
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bContactNotFoundException 담당자가 존재하지 않는 경우
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bMemberCompanyNotFoundException 연동 사업자가 존재하지 않는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bContactSuspend")
  public suspend fun getB2bContact(
    contactId: String,
    test: Boolean? = null,
  ): B2bCompanyContact {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b", "contacts", contactId.toString())
        if (test != null) parameters.append("test", test.toString())
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
        json.decodeFromString<GetB2bContactError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bContactNotFoundError -> throw B2bContactNotFoundException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bMemberCompanyNotFoundError -> throw B2bMemberCompanyNotFoundException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bCompanyContact>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bContact")
  public suspend fun getB2bContactFuture(
    contactId: String,
    test: Boolean? = null,
  ): CompletableFuture<B2bCompanyContact> = GlobalScope.future { getB2bContact(contactId, test) }


  /**
   * 담당자 정보 수정
   *
   * 담당자 정보를 수정합니다.
   *
   * @param contactId
   * 담당자 ID
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param password
   * 비밀번호
   * @param name
   * 담당자 성명
   * @param phoneNumber
   * 담당자 핸드폰 번호
   * @param email
   * 담당자 이메일
   *
   * @throws B2bContactNotFoundException 담당자가 존재하지 않는 경우
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bMemberCompanyNotFoundException 연동 사업자가 존재하지 않는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("updateB2bContactSuspend")
  public suspend fun updateB2bContact(
    contactId: String,
    test: Boolean? = null,
    password: String? = null,
    name: String? = null,
    phoneNumber: String? = null,
    email: String? = null,
  ): UpdateB2bContactResponse {
    val requestBody = UpdateB2bContactBody(
      password = password,
      name = name,
      phoneNumber = phoneNumber,
      email = email,
    )
    val httpResponse = client.patch(apiBase) {
      url {
        appendPathSegments("b2b", "contacts", contactId.toString())
        if (test != null) parameters.append("test", test.toString())
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
        json.decodeFromString<UpdateB2bContactError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bContactNotFoundError -> throw B2bContactNotFoundException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bMemberCompanyNotFoundError -> throw B2bMemberCompanyNotFoundException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdateB2bContactResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updateB2bContact")
  public suspend fun updateB2bContactFuture(
    contactId: String,
    test: Boolean? = null,
    password: String? = null,
    name: String? = null,
    phoneNumber: String? = null,
    email: String? = null,
  ): CompletableFuture<UpdateB2bContactResponse> = GlobalScope.future { updateB2bContact(contactId, test, password, name, phoneNumber, email) }


  /**
   * 담당자 ID 존재 여부 확인
   *
   * 담당자 ID가 이미 사용중인지 확인합니다.
   *
   * @param contactId
   * 담당자 ID
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bContactIdExistenceSuspend")
  public suspend fun getB2bContactIdExistence(
    contactId: String,
    test: Boolean? = null,
  ): GetB2bContactIdExistenceResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b", "contacts", contactId.toString(), "exists")
        if (test != null) parameters.append("test", test.toString())
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
        json.decodeFromString<getB2bContactIdExistenceError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bContactIdExistenceResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bContactIdExistence")
  public suspend fun getB2bContactIdExistenceFuture(
    contactId: String,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bContactIdExistenceResponse> = GlobalScope.future { getB2bContactIdExistence(contactId, test) }

  internal fun close() {
    client.close()
  }
}
