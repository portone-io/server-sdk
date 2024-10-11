package io.portone.sdk.server

import io.ktor.client.HttpClient
import io.portone.sdk.server.LoginViaApiSecretResponse
import io.portone.sdk.server.RefreshTokenResponse
import io.portone.sdk.server.auth.LoginViaApiSecretResponse
import io.portone.sdk.server.auth.RefreshTokenResponse
import java.io.Closeable
import kotlin.String
import kotlinx.serialization.json.Json

public class AuthClient(
  private val apiSecret: String,
  private val storeId: String,
  private val apiBase: String,
) : Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * API secret 를 사용한 토큰 발급
   *
   * API secret 를 통해 API 인증에 사용할 토큰을 가져옵니다.
   *
   * @param apiSecret
   * 발급받은 API secret
   *
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("loginViaApiSecretSuspend")
  public suspend fun loginViaApiSecret(
    apiSecret: string,
  ): LoginViaApiSecretResponse {
    val requestBody = LoginViaApiSecretBody(
      apiSecret = apiSecret,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("login", "api-secret")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<LoginViaApiSecretError>(httpBody)
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
      json.decodeFromString<LoginViaApiSecretResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("loginViaApiSecret")
  public suspend fun loginViaApiSecretFuture(
    apiSecret: string,
  ): CompletableFuture<LoginViaApiSecretResponse> = GlobalScope.future { loginViaApiSecret(apiSecret) }


  /**
   * 토큰 갱신
   *
   * 리프레시 토큰을 사용해 유효기간이 연장된 새로운 토큰을 재발급합니다.
   *
   * @param refreshToken
   * 리프레시 토큰
   *
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("refreshTokenSuspend")
  public suspend fun refreshToken(
    refreshToken: string,
  ): RefreshTokenResponse {
    val requestBody = RefreshTokenBody(
      refreshToken = refreshToken,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("token", "refresh")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<RefreshTokenError>(httpBody)
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
      json.decodeFromString<RefreshTokenResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("refreshToken")
  public suspend fun refreshTokenFuture(
    refreshToken: string,
  ): CompletableFuture<RefreshTokenResponse> = GlobalScope.future { refreshToken(refreshToken) }

  override fun close() {
    client.close()
  }
}
