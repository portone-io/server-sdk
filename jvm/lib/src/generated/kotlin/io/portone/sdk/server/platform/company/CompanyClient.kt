package io.portone.sdk.server.platform.company

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
import io.portone.sdk.server.errors.B2bExternalServiceError
import io.portone.sdk.server.errors.B2bExternalServiceException
import io.portone.sdk.server.errors.B2bNotEnabledError
import io.portone.sdk.server.errors.B2bNotEnabledException
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetB2bBusinessInfosError
import io.portone.sdk.server.errors.GetB2bBusinessInfosException
import io.portone.sdk.server.errors.GetPlatformCompanyStateError
import io.portone.sdk.server.errors.GetPlatformCompanyStateException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.PlatformCompanyNotFoundError
import io.portone.sdk.server.errors.PlatformCompanyNotFoundException
import io.portone.sdk.server.errors.PlatformExternalApiFailedError
import io.portone.sdk.server.errors.PlatformExternalApiFailedException
import io.portone.sdk.server.errors.PlatformNotEnabledError
import io.portone.sdk.server.errors.PlatformNotEnabledException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.platform.company.GetB2bBusinessInfosBody
import io.portone.sdk.server.platform.company.GetB2bBusinessInfosResponse
import io.portone.sdk.server.platform.company.GetPlatformCompanyStatePayload
import java.io.Closeable
import java.util.concurrent.CompletableFuture
import kotlin.Array
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
public class CompanyClient(
  private val apiSecret: String,
  private val apiBase: String = "https://api.portone.io",
  private val storeId: String? = null,
): Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 사업자등록 정보조회
   *
   * 요청된 사업자등록번호 리스트에 해당하는 사업자등록 정보를 조회합니다.
   * 해당 API 사용을 위해서는 별도 문의가 필요합니다.
   *
   * @param brnList
   * 조회할 사업자등록번호 리스트
   *
   * @throws GetB2bBusinessInfosException
   */
  @JvmName("getB2bBusinessInfosSuspend")
  public suspend fun getB2bBusinessInfos(
    brnList: List<String>,
  ): GetB2bBusinessInfosResponse {
    val requestBody = GetB2bBusinessInfosBody(
      brnList = brnList,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("b2b", "companies", "business-info")
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
        json.decodeFromString<GetB2bBusinessInfosError.Recognized>(httpBody)
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
      json.decodeFromString<GetB2bBusinessInfosResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bBusinessInfos")
  public fun getB2bBusinessInfosFuture(
    brnList: List<String>,
  ): CompletableFuture<GetB2bBusinessInfosResponse> = GlobalScope.future { getB2bBusinessInfos(brnList) }


  /**
   * 사업자 조회
   *
   * 사업자 정보를 조회합니다. 포트원 서비스에 연동 및 등록되지 않은 사업자도 조회 가능합니다.
   *
   * @param businessRegistrationNumber
   * 사업자등록번호
   *
   * @throws GetPlatformCompanyStateException
   */
  @JvmName("getPlatformCompanyStateSuspend")
  public suspend fun getPlatformCompanyState(
    businessRegistrationNumber: String,
  ): GetPlatformCompanyStatePayload {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "companies", businessRegistrationNumber.toString(), "state")
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
        json.decodeFromString<GetPlatformCompanyStateError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformCompanyNotFoundError -> throw PlatformCompanyNotFoundException(httpBodyDecoded)
        is PlatformExternalApiFailedError -> throw PlatformExternalApiFailedException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetPlatformCompanyStatePayload>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformCompanyState")
  public fun getPlatformCompanyStateFuture(
    businessRegistrationNumber: String,
  ): CompletableFuture<GetPlatformCompanyStatePayload> = GlobalScope.future { getPlatformCompanyState(businessRegistrationNumber) }

  override fun close() {
    client.close()
  }
}
