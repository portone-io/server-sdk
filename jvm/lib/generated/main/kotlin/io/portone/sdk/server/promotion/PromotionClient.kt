package io.portone.sdk.server

import io.ktor.client.HttpClient
import io.portone.sdk.server.Promotion
import io.portone.sdk.server.promotion.Promotion
import java.io.Closeable
import kotlin.String
import kotlinx.serialization.json.Json

public class PromotionClient(
  private val apiSecret: String,
  private val storeId: String,
  private val apiBase: String,
) : Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 프로모션 단건 조회
   *
   * 주어진 아이디에 대응되는 프로모션을 조회합니다.
   *
   * @param promotionId
   * 조회할 프로모션 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PromotionNotFoundException 프로모션이 존재하지 않는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPromotionSuspend")
  public suspend fun getPromotion(
    promotionId: string,
  ): Promotion {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("promotions", promotionId)
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
        json.decodeFromString<GetPromotionError>(httpBody)
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
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPromotion")
  public suspend fun getPromotionFuture(
    promotionId: string,
  ): CompletableFuture<Promotion> = GlobalScope.future { getPromotion(promotionId) }

  override fun close() {
    client.close()
  }
}
