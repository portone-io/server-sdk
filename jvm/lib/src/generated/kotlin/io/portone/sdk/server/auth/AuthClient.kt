package io.portone.sdk.server.auth

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.plugins.HttpTimeout
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
import io.portone.sdk.server.auth.LoginViaApiSecretBody
import io.portone.sdk.server.auth.LoginViaApiSecretResponse
import io.portone.sdk.server.auth.RefreshTokenBody
import io.portone.sdk.server.auth.RefreshTokenResponse
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.LoginViaApiSecretError
import io.portone.sdk.server.errors.LoginViaApiSecretException
import io.portone.sdk.server.errors.RefreshTokenError
import io.portone.sdk.server.errors.RefreshTokenException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import java.io.Closeable
import java.util.concurrent.CompletableFuture
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
public class AuthClient(
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
   * API secret 를 사용한 토큰 발급
   *
   * API secret 를 통해 API 인증에 사용할 토큰을 가져옵니다.
   *
   * @param apiSecret
   * 발급받은 API secret
   *
   * @throws LoginViaApiSecretException
   */
  @JvmName("loginViaApiSecretSuspend")
  public suspend fun loginViaApiSecret(
    apiSecret: String,
  ): LoginViaApiSecretResponse {
    val requestBody = LoginViaApiSecretBody(
      apiSecret = apiSecret,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("login", "api-secret")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<LoginViaApiSecretError.Recognized>(httpBody)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("loginViaApiSecret")
  public fun loginViaApiSecretFuture(
    apiSecret: String,
  ): CompletableFuture<LoginViaApiSecretResponse> = GlobalScope.future { loginViaApiSecret(apiSecret) }


  /**
   * 토큰 갱신
   *
   * 리프레시 토큰을 사용해 유효기간이 연장된 새로운 토큰을 재발급합니다.
   *
   * @param refreshToken
   * 리프레시 토큰
   *
   * @throws RefreshTokenException
   */
  @JvmName("refreshTokenSuspend")
  public suspend fun refreshToken(
    refreshToken: String,
  ): RefreshTokenResponse {
    val requestBody = RefreshTokenBody(
      refreshToken = refreshToken,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("token", "refresh")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      accept(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<RefreshTokenError.Recognized>(httpBody)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("refreshToken")
  public fun refreshTokenFuture(
    refreshToken: String,
  ): CompletableFuture<RefreshTokenResponse> = GlobalScope.future { refreshToken(refreshToken) }

  override fun close() {
    client.close()
  }
}
