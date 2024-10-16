package io.portone.sdk.server.pgspecific

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
import io.portone.sdk.server.errors.GetKakaopayPaymentOrderError
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.pgspecific.GetKakaopayPaymentOrderResponse
import java.io.Closeable
import java.util.concurrent.CompletableFuture
import kotlin.String
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.json.Json

public class PgSpecificClient internal constructor(
  private val apiSecret: String,
  private val apiBase: String,
  private val storeId: String?,
) {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 카카오페이 주문 조회 API
   *
   * 주어진 아이디에 대응되는 카카오페이 주문 건을 조회합니다.
   * 해당 API 사용이 필요한 경우 포트원 기술지원팀으로 문의 주시길 바랍니다.
   *
   * @param pgTxId
   * 카카오페이 주문 번호 (tid)
   * @param channelKey
   * 채널 키
   *
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getKakaopayPaymentOrderSuspend")
  public suspend fun getKakaopayPaymentOrder(
    pgTxId: String,
    channelKey: String,
  ): GetKakaopayPaymentOrderResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("kakaopay", "payment", "order")
        parameters.append("pgTxId", pgTxId.toString())
        parameters.append("channelKey", channelKey.toString())
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
        json.decodeFromString<GetKakaopayPaymentOrderError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetKakaopayPaymentOrderResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getKakaopayPaymentOrder")
  public suspend fun getKakaopayPaymentOrderFuture(
    pgTxId: String,
    channelKey: String,
  ): CompletableFuture<GetKakaopayPaymentOrderResponse> = GlobalScope.future { getKakaopayPaymentOrder(pgTxId, channelKey) }

  internal fun close() {
    client.close()
  }
}
