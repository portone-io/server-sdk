package io.portone.sdk.server.platform.company

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
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
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
import io.portone.sdk.server.platform.company.GetPlatformCompanyStatePayload
import java.io.Closeable
import java.util.concurrent.CompletableFuture
import kotlin.String
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.json.Json

public class CompanyClient(
  private val apiSecret: String,
  private val apiBase: String = "https://api.portone.io",
  private val storeId: String? = null,
): Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

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
