package io.portone.sdk.server.payment.promotion

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
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetPromotionError
import io.portone.sdk.server.errors.GetPromotionException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.PromotionNotFoundError
import io.portone.sdk.server.errors.PromotionNotFoundException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.payment.promotion.Promotion
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
public class PromotionClient(
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
   * 프로모션 단건 조회
   *
   * 주어진 아이디에 대응되는 프로모션을 조회합니다.
   *
   * @param promotionId
   * 조회할 프로모션 아이디
   *
   * @throws GetPromotionException
   */
  @JvmName("getPromotionSuspend")
  public suspend fun getPromotion(
    promotionId: String,
  ): Promotion {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("promotions", promotionId.toString())
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
        json.decodeFromString<GetPromotionError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PromotionNotFoundError -> throw PromotionNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<Promotion>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPromotion")
  public fun getPromotionFuture(
    promotionId: String,
  ): CompletableFuture<Promotion> = GlobalScope.future { getPromotion(promotionId) }

  override fun close() {
    client.close()
  }
}
