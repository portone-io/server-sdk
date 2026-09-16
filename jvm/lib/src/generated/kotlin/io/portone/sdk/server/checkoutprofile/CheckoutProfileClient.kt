package io.portone.sdk.server.checkoutprofile

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
import io.portone.sdk.server.checkoutprofile.EvaluateCheckoutProfileResponse
import io.portone.sdk.server.common.Country
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.errors.EvaluateCheckoutProfileError
import io.portone.sdk.server.errors.EvaluateCheckoutProfileException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.ProfileSettingsNotFoundError
import io.portone.sdk.server.errors.ProfileSettingsNotFoundException
import io.portone.sdk.server.errors.UnknownException
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
public class CheckoutProfileClient(
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
   * 체크아웃 프로필에서 결제 수단 목록 조회
   *
   * 주어진 금액 및 국가에서 사용 가능한 결제 수단 목록을 반환
   *
   * @param profileKey
   * 프로필 키
   * @param country
   * 국가
   * @param currency
   * 통화
   * @param amount
   * 결제 금액
   *
   * @throws EvaluateCheckoutProfileException
   */
  @JvmName("evaluateCheckoutProfileSuspend")
  public suspend fun evaluateCheckoutProfile(
    profileKey: String,
    country: Country,
    currency: Currency,
    amount: Long,
  ): EvaluateCheckoutProfileResponse {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("checkout-profiles", "evaluate")
        this.parameters.append("profileKey", profileKey.toString())
        this.parameters.append("country", country.toString())
        this.parameters.append("currency", currency.toString())
        this.parameters.append("amount", amount.toString())
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
        json.decodeFromString<EvaluateCheckoutProfileError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is ProfileSettingsNotFoundError -> throw ProfileSettingsNotFoundException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<EvaluateCheckoutProfileResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("evaluateCheckoutProfile")
  public fun evaluateCheckoutProfileFuture(
    profileKey: String,
    country: Country,
    currency: Currency,
    amount: Long,
  ): CompletableFuture<EvaluateCheckoutProfileResponse> = GlobalScope.future { evaluateCheckoutProfile(profileKey, country, currency, amount) }

  override fun close() {
    client.close()
  }
}
