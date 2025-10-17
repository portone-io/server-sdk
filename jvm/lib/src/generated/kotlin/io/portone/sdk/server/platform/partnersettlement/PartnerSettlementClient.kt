package io.portone.sdk.server.platform.partnersettlement

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.plugins.HttpTimeout
import io.ktor.client.request.`get`
import io.ktor.client.request.accept
import io.ktor.client.request.headers
import io.ktor.http.ContentType
import io.ktor.http.HttpHeaders
import io.ktor.http.appendPathSegments
import io.ktor.http.userAgent
import io.portone.sdk.server.USER_AGENT
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetPlatformPartnerSettlementsError
import io.portone.sdk.server.errors.GetPlatformPartnerSettlementsException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.PlatformNotEnabledError
import io.portone.sdk.server.errors.PlatformNotEnabledException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.platform.partnersettlement.GetPlatformPartnerSettlementsBody
import io.portone.sdk.server.platform.partnersettlement.GetPlatformPartnerSettlementsResponse
import io.portone.sdk.server.platform.partnersettlement.PlatformPartnerSettlementFilterInput
import java.io.Closeable
import java.util.concurrent.CompletableFuture
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
public class PartnerSettlementClient(
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
   * 정산 내역 다건 조회
   *
   * 여러 정산 내역을 조회합니다.
   *
   * @param page
   * 요청할 페이지 정보
   * @param filter
   * 조회할 정산내역 조건 필터
   * @param isForTest
   *
   *
   * @throws GetPlatformPartnerSettlementsException
   */
  @JvmName("getPlatformPartnerSettlementsSuspend")
  public suspend fun getPlatformPartnerSettlements(
    page: PageInput? = null,
    filter: PlatformPartnerSettlementFilterInput,
    isForTest: Boolean,
  ): GetPlatformPartnerSettlementsResponse {
    val requestBody = GetPlatformPartnerSettlementsBody(
      page = page,
      filter = filter,
      isForTest = isForTest,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "partner-settlements")
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
        json.decodeFromString<GetPlatformPartnerSettlementsError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetPlatformPartnerSettlementsResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformPartnerSettlements")
  public fun getPlatformPartnerSettlementsFuture(
    page: PageInput? = null,
    filter: PlatformPartnerSettlementFilterInput,
    isForTest: Boolean,
  ): CompletableFuture<GetPlatformPartnerSettlementsResponse> = GlobalScope.future { getPlatformPartnerSettlements(page, filter, isForTest) }

  override fun close() {
    client.close()
  }
}
