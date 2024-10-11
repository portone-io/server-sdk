package io.portone.sdk.server.bulkpayout

import io.ktor.client.HttpClient
import io.portone.sdk.server.GetPlatformBulkPayoutsResponse
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.bulkpayout.GetPlatformBulkPayoutsResponse
import io.portone.sdk.server.platform.bulkpayout.PlatformBulkPayoutFilterInput
import java.io.Closeable
import kotlinx.serialization.json.Json

public class BulkPayoutClient(
  private val apiSecret: String,
  private val storeId: String,
  private val apiBase: String,
) : Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 일괄 지급 내역 다건 조회
   *
   * 성공 응답으로 조회된 일괄 지급 내역 리스트와 페이지 정보 및 상태 별 개수 정보를 반환합니다.
   *
   * @param isForTest
   *
   * @param page
   *
   * @param filter
   *
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformBulkPayoutsSuspend")
  public suspend fun getPlatformBulkPayouts(
    isForTest: Boolean? = null,
    page: PageInput? = null,
    filter: PlatformBulkPayoutFilterInput? = null,
  ): GetPlatformBulkPayoutsResponse {
    val requestBody = GetPlatformBulkPayoutsBody(
      isForTest = isForTest,
      page = page,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "bulk-payouts")
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
        json.decodeFromString<GetPlatformBulkPayoutsError>(httpBody)
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
      json.decodeFromString<GetPlatformBulkPayoutsResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformBulkPayouts")
  public suspend fun getPlatformBulkPayoutsFuture(
    isForTest: Boolean? = null,
    page: PageInput? = null,
    filter: PlatformBulkPayoutFilterInput? = null,
  ): CompletableFuture<GetPlatformBulkPayoutsResponse> = GlobalScope.future { getPlatformBulkPayouts(isForTest, page, filter) }

  override fun close() {
    client.close()
  }
}