package io.portone.sdk.server.platform.account

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
import io.portone.sdk.server.common.Bank
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetPlatformAccountHolderError
import io.portone.sdk.server.errors.GetPlatformAccountHolderException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.PlatformExternalApiFailedError
import io.portone.sdk.server.errors.PlatformExternalApiFailedException
import io.portone.sdk.server.errors.PlatformExternalApiTemporarilyFailedError
import io.portone.sdk.server.errors.PlatformExternalApiTemporarilyFailedException
import io.portone.sdk.server.errors.PlatformNotEnabledError
import io.portone.sdk.server.errors.PlatformNotEnabledException
import io.portone.sdk.server.errors.PlatformNotSupportedBankError
import io.portone.sdk.server.errors.PlatformNotSupportedBankException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.platform.account.PlatformAccountHolder
import java.io.Closeable
import java.util.concurrent.CompletableFuture
import kotlin.String
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.json.Json

/**
 * API Secret을 사용해 포트원 API 클라이언트를 생성합니다.
 */
public class AccountClient(
  private val apiSecret: String,
  private val apiBase: String = "https://api.portone.io",
  private val storeId: String? = null,
): Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 예금주 조회
   *
   * 계좌의 예금주를 조회합니다.
   *
   * @param bank
   * 은행
   * @param accountNumber
   * '-'를 제외한 계좌 번호
   * @param birthdate
   * 생년월일
   *
   * 실명 조회를 위해 추가로 보낼 수 있습니다. birthdate과 businessRegistrationNumber 중 하나만 사용해야 합니다.
   * @param businessRegistrationNumber
   * 사업자등록번호
   *
   * 실명 조회를 위해 추가로 보낼 수 있습니다. birthdate과 businessRegistrationNumber 중 하나만 사용해야 합니다.
   *
   * @throws GetPlatformAccountHolderException
   */
  @JvmName("getPlatformAccountHolderSuspend")
  public suspend fun getPlatformAccountHolder(
    bank: Bank,
    accountNumber: String,
    birthdate: String? = null,
    businessRegistrationNumber: String? = null,
  ): PlatformAccountHolder {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "bank-accounts", bank.toString(), accountNumber.toString(), "holder")
        if (birthdate != null) parameters.append("birthdate", birthdate.toString())
        if (businessRegistrationNumber != null) parameters.append("businessRegistrationNumber", businessRegistrationNumber.toString())
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
        json.decodeFromString<GetPlatformAccountHolderError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformExternalApiFailedError -> throw PlatformExternalApiFailedException(httpBodyDecoded)
        is PlatformExternalApiTemporarilyFailedError -> throw PlatformExternalApiTemporarilyFailedException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformNotSupportedBankError -> throw PlatformNotSupportedBankException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PlatformAccountHolder>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformAccountHolder")
  public fun getPlatformAccountHolderFuture(
    bank: Bank,
    accountNumber: String,
    birthdate: String? = null,
    businessRegistrationNumber: String? = null,
  ): CompletableFuture<PlatformAccountHolder> = GlobalScope.future { getPlatformAccountHolder(bank, accountNumber, birthdate, businessRegistrationNumber) }

  override fun close() {
    client.close()
  }
}
