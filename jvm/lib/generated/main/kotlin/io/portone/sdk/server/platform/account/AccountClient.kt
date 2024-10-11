package io.portone.sdk.server.account

import io.ktor.client.HttpClient
import io.portone.sdk.server.PlatformAccountHolder
import io.portone.sdk.server.common.Bank
import io.portone.sdk.server.platform.account.PlatformAccountHolder
import java.io.Closeable
import kotlin.String
import kotlinx.serialization.json.Json

public class AccountClient(
  private val apiSecret: String,
  private val storeId: String,
  private val apiBase: String,
) : Closeable {
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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformExternalApiFailedException 외부 api 오류
   * @throws PlatformExternalApiTemporarilyFailedException 외부 api의 일시적인 오류
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformNotSupportedBankException 지원하지 않는 은행인 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformAccountHolderSuspend")
  public suspend fun getPlatformAccountHolder(
    bank: Bank,
    accountNumber: string,
    birthdate: string? = null,
    businessRegistrationNumber: string? = null,
  ): PlatformAccountHolder {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "bank-accounts", bank, accountNumber, "holder")
        if (birthdate != null) parameters.append("birthdate", birthdate)
        if (businessRegistrationNumber != null) parameters.append("businessRegistrationNumber", businessRegistrationNumber)
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
        json.decodeFromString<GetPlatformAccountHolderError>(httpBody)
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
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformAccountHolder")
  public suspend fun getPlatformAccountHolderFuture(
    bank: Bank,
    accountNumber: string,
    birthdate: string? = null,
    businessRegistrationNumber: string? = null,
  ): CompletableFuture<PlatformAccountHolder> = GlobalScope.future { getPlatformAccountHolder(bank, accountNumber, birthdate, businessRegistrationNumber) }

  override fun close() {
    client.close()
  }
}
