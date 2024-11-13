package io.portone.sdk.server.platform.partnersettlement

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
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetPlatformPartnerSettlementsError
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

public class PartnerSettlementClient internal constructor(
  private val apiSecret: String,
  private val apiBase: String,
  private val storeId: String?,
) {
  private val client: HttpClient = HttpClient(OkHttp)

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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
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
        json.decodeFromString<GetPlatformPartnerSettlementsError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
        else -> throw UnknownException("Unknown API error: $httpBody")
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

  internal fun close() {
    client.close()
  }
}
