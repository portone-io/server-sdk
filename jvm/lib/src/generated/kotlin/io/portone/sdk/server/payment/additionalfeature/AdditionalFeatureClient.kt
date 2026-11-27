package io.portone.sdk.server.payment.additionalfeature

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
import io.portone.sdk.server.errors.ChannelNotFoundError
import io.portone.sdk.server.errors.ChannelNotFoundException
import io.portone.sdk.server.errors.GetPgCardPromotionsError
import io.portone.sdk.server.errors.GetPgCardPromotionsException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.PgProviderError
import io.portone.sdk.server.errors.PgProviderException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.payment.additionalfeature.GetPgCardPromotionsResponse
import io.portone.sdk.server.payment.additionalfeature.PgPromotionCardCompany
import java.io.Closeable
import java.util.concurrent.CompletableFuture
import kotlin.String
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.json.Json

/**
 * API Secret을 사용해 포트원 API 클라이언트를 생성합니다.
 *
 * @param apiSecret 포트원 API Secret입니다.
 * @param apiBase 포트원 REST API 주소입니다. 기본값은 `"https://api.portone.io"`입니다.
 * @param storeId 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.
 */
public class AdditionalFeatureClient(
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
   * PG사 카드 프로모션 조회 API
   *
   * 주어진 채널에 대해 PG사에서 제공하는 카드 프로모션 목록을 조회합니다.
   * 해당 API는 현재 특정 PG사(KCP_V2)에 대해서만 지원되며, 지원 여부는 포트원 기술지원팀에 문의 부탁드립니다.
   *
   * @param channelKey
   * 채널 키
   *
   * 조회하고자 하는 채널의 키
   * @param amount
   * 결제 금액
   *
   * 결제 금액입니다. 해당 결제 금액 기준 이용 가능한 프로모션 목록이 조회됩니다.
   * @param cardCompany
   * 카드사 필터
   *
   * 조회할 카드사입니다. 값을 입력하지 않으면 카드사 필터링이 적용되지 않습니다.
   *
   * @throws GetPgCardPromotionsException
   */
  @JvmName("getPgCardPromotionsSuspend")
  public suspend fun getPgCardPromotions(
    channelKey: String,
    amount: Long,
    cardCompany: PgPromotionCardCompany? = null,
  ): GetPgCardPromotionsResponse {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("payment-gateways", "card-promotion")
        this.parameters.append("channelKey", channelKey.toString())
        this.parameters.append("amount", amount.toString())
        if (cardCompany != null) this.parameters.append("cardCompany", cardCompany.toString())
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
        json.decodeFromString<GetPgCardPromotionsError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ChannelNotFoundError -> throw ChannelNotFoundException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetPgCardPromotionsResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPgCardPromotions")
  public fun getPgCardPromotionsFuture(
    channelKey: String,
    amount: Long,
    cardCompany: PgPromotionCardCompany? = null,
  ): CompletableFuture<GetPgCardPromotionsResponse> = GlobalScope.future { getPgCardPromotions(channelKey, amount, cardCompany) }

  override fun close() {
    client.close()
  }
}
