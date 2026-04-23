package io.portone.sdk.server.platform.payout

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
import io.portone.sdk.server.annotations.PortOneUnstable
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.errors.CompletePlatformPayoutByPartnerSettlementIdsError
import io.portone.sdk.server.errors.CompletePlatformPayoutByPartnerSettlementIdsException
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetPlatformPayoutsError
import io.portone.sdk.server.errors.GetPlatformPayoutsException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.PlatformBulkPayoutIdAlreadyExistsError
import io.portone.sdk.server.errors.PlatformBulkPayoutIdAlreadyExistsException
import io.portone.sdk.server.errors.PlatformDuplicatedPartnerSettlementIdsError
import io.portone.sdk.server.errors.PlatformDuplicatedPartnerSettlementIdsException
import io.portone.sdk.server.errors.PlatformNegativePayoutAmountPartnersError
import io.portone.sdk.server.errors.PlatformNegativePayoutAmountPartnersException
import io.portone.sdk.server.errors.PlatformNoSelectedPartnerSettlementsError
import io.portone.sdk.server.errors.PlatformNoSelectedPartnerSettlementsException
import io.portone.sdk.server.errors.PlatformNonPayablePartnerSettlementsError
import io.portone.sdk.server.errors.PlatformNonPayablePartnerSettlementsException
import io.portone.sdk.server.errors.PlatformNotEnabledError
import io.portone.sdk.server.errors.PlatformNotEnabledException
import io.portone.sdk.server.errors.PlatformPartnerSettlementsNotFoundError
import io.portone.sdk.server.errors.PlatformPartnerSettlementsNotFoundException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.platform.payout.CompletePlatformPayoutByPartnerSettlementIdsBody
import io.portone.sdk.server.platform.payout.CompletePlatformPayoutByPartnerSettlementIdsResponse
import io.portone.sdk.server.platform.payout.GetPlatformPayoutsBody
import io.portone.sdk.server.platform.payout.GetPlatformPayoutsResponse
import io.portone.sdk.server.platform.payout.PlatformPayoutFilterInput
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
public class PayoutClient(
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
   * 일괄 지급 완료 처리
   *
   * 선택한 정산내역 아이디들로 일괄 지급을 완료 처리 합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param bulkPayoutId
   *
   * @param name
   *
   * @param partnerSettlementIds
   *
   * @param completedAt
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   * @param isForTest
   * Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
   * Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws CompletePlatformPayoutByPartnerSettlementIdsException
   */
  @PortOneUnstable
  @JvmName("completePlatformPayoutByPartnerSettlementIdsSuspend")
  public suspend fun completePlatformPayoutByPartnerSettlementIds(
    test: Boolean? = null,
    bulkPayoutId: String,
    name: String? = null,
    partnerSettlementIds: List<String>,
    completedAt: String? = null,
    isForTest: Boolean? = null,
  ): CompletePlatformPayoutByPartnerSettlementIdsResponse {
    val requestBody = CompletePlatformPayoutByPartnerSettlementIdsBody(
      bulkPayoutId = bulkPayoutId,
      name = name,
      partnerSettlementIds = partnerSettlementIds,
      completedAt = completedAt,
      isForTest = isForTest,
    )
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "partner-settlements", "complete-payout")
        if (test != null) this.parameters.append("test", test.toString())
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
        json.decodeFromString<CompletePlatformPayoutByPartnerSettlementIdsError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformBulkPayoutIdAlreadyExistsError -> throw PlatformBulkPayoutIdAlreadyExistsException(httpBodyDecoded)
        is PlatformNegativePayoutAmountPartnersError -> throw PlatformNegativePayoutAmountPartnersException(httpBodyDecoded)
        is PlatformDuplicatedPartnerSettlementIdsError -> throw PlatformDuplicatedPartnerSettlementIdsException(httpBodyDecoded)
        is PlatformNonPayablePartnerSettlementsError -> throw PlatformNonPayablePartnerSettlementsException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformNoSelectedPartnerSettlementsError -> throw PlatformNoSelectedPartnerSettlementsException(httpBodyDecoded)
        is PlatformPartnerSettlementsNotFoundError -> throw PlatformPartnerSettlementsNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CompletePlatformPayoutByPartnerSettlementIdsResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @PortOneUnstable
  @JvmName("completePlatformPayoutByPartnerSettlementIds")
  public fun completePlatformPayoutByPartnerSettlementIdsFuture(
    test: Boolean? = null,
    bulkPayoutId: String,
    name: String? = null,
    partnerSettlementIds: List<String>,
    completedAt: String? = null,
    isForTest: Boolean? = null,
  ): CompletableFuture<CompletePlatformPayoutByPartnerSettlementIdsResponse> = GlobalScope.future { completePlatformPayoutByPartnerSettlementIds(test, bulkPayoutId, name, partnerSettlementIds, completedAt, isForTest) }


  /**
   * 지급 내역 다건 조회
   *
   * 여러 지급 내역을 조회합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param isForTest
   * Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
   * Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param page
   *
   * @param filter
   *
   *
   * @throws GetPlatformPayoutsException
   */
  @JvmName("getPlatformPayoutsSuspend")
  public suspend fun getPlatformPayouts(
    test: Boolean? = null,
    isForTest: Boolean? = null,
    page: PageInput? = null,
    filter: PlatformPayoutFilterInput? = null,
  ): GetPlatformPayoutsResponse {
    val requestBody = GetPlatformPayoutsBody(
      isForTest = isForTest,
      page = page,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("platform", "payouts")
        if (test != null) this.parameters.append("test", test.toString())
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
        json.decodeFromString<GetPlatformPayoutsError.Recognized>(httpBody)
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
      json.decodeFromString<GetPlatformPayoutsResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformPayouts")
  public fun getPlatformPayoutsFuture(
    test: Boolean? = null,
    isForTest: Boolean? = null,
    page: PageInput? = null,
    filter: PlatformPayoutFilterInput? = null,
  ): CompletableFuture<GetPlatformPayoutsResponse> = GlobalScope.future { getPlatformPayouts(test, isForTest, page, filter) }

  override fun close() {
    client.close()
  }
}
