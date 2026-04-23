package io.portone.sdk.server.b2b.counterparty

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.plugins.HttpTimeout
import io.ktor.client.request.`get`
import io.ktor.client.request.accept
import io.ktor.client.request.delete
import io.ktor.client.request.headers
import io.ktor.client.request.patch
import io.ktor.client.request.post
import io.ktor.client.request.setBody
import io.ktor.http.ContentType
import io.ktor.http.HttpHeaders
import io.ktor.http.appendPathSegments
import io.ktor.http.contentType
import io.ktor.http.userAgent
import io.portone.sdk.server.USER_AGENT
import io.portone.sdk.server.b2b.counterparty.B2bCertificate
import io.portone.sdk.server.b2b.counterparty.B2bCounterparty
import io.portone.sdk.server.b2b.counterparty.B2bCounterpartyCreateOptions
import io.portone.sdk.server.b2b.counterparty.B2bCounterpartyFilter
import io.portone.sdk.server.b2b.counterparty.B2bCounterpartyInput
import io.portone.sdk.server.b2b.counterparty.CreateB2bCounterpartyBody
import io.portone.sdk.server.b2b.counterparty.CreateB2bCounterpartyResponse
import io.portone.sdk.server.b2b.counterparty.DeleteB2bCounterpartyBody
import io.portone.sdk.server.b2b.counterparty.DeleteB2bCounterpartyResponse
import io.portone.sdk.server.b2b.counterparty.GetB2bCounterpartiesBody
import io.portone.sdk.server.b2b.counterparty.GetB2bCounterpartiesResponse
import io.portone.sdk.server.b2b.counterparty.GetB2bCounterpartyCertificateRegistrationUrlResponse
import io.portone.sdk.server.b2b.counterparty.UpdateB2bCounterpartyBody
import io.portone.sdk.server.b2b.counterparty.UpdateB2bCounterpartyResponse
import io.portone.sdk.server.b2b.counterparty.ValidateB2bCounterpartyCertificateResponse
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.errors.B2bCertificateUnregisteredError
import io.portone.sdk.server.errors.B2bCertificateUnregisteredException
import io.portone.sdk.server.errors.B2bCounterpartyBrnInvalidError
import io.portone.sdk.server.errors.B2bCounterpartyBrnInvalidException
import io.portone.sdk.server.errors.B2bCounterpartyBrnModificationNotAllowedError
import io.portone.sdk.server.errors.B2bCounterpartyBrnModificationNotAllowedException
import io.portone.sdk.server.errors.B2bCounterpartyIdAlreadyExistsByPartnerError
import io.portone.sdk.server.errors.B2bCounterpartyIdAlreadyExistsByPartnerException
import io.portone.sdk.server.errors.B2bCounterpartyIdAlreadyExistsError
import io.portone.sdk.server.errors.B2bCounterpartyIdAlreadyExistsException
import io.portone.sdk.server.errors.B2bCounterpartyMissingRequiredFieldsError
import io.portone.sdk.server.errors.B2bCounterpartyMissingRequiredFieldsException
import io.portone.sdk.server.errors.B2bCounterpartyNotFoundError
import io.portone.sdk.server.errors.B2bCounterpartyNotFoundException
import io.portone.sdk.server.errors.B2bCounterpartyNtsConnectionFailedError
import io.portone.sdk.server.errors.B2bCounterpartyNtsConnectionFailedException
import io.portone.sdk.server.errors.B2bCounterpartyNtsNotConnectedError
import io.portone.sdk.server.errors.B2bCounterpartyNtsNotConnectedException
import io.portone.sdk.server.errors.B2bCounterpartyOngoingTaxInvoiceExistsError
import io.portone.sdk.server.errors.B2bCounterpartyOngoingTaxInvoiceExistsException
import io.portone.sdk.server.errors.B2bCounterpartyPartnerNotConnectableError
import io.portone.sdk.server.errors.B2bCounterpartyPartnerNotConnectableException
import io.portone.sdk.server.errors.B2bCounterpartyPartnerNotDeletableError
import io.portone.sdk.server.errors.B2bCounterpartyPartnerNotDeletableException
import io.portone.sdk.server.errors.B2bCounterpartyPartnerNotUpdatableError
import io.portone.sdk.server.errors.B2bCounterpartyPartnerNotUpdatableException
import io.portone.sdk.server.errors.B2bCounterpartySelfOriginBrnMismatchError
import io.portone.sdk.server.errors.B2bCounterpartySelfOriginBrnMismatchException
import io.portone.sdk.server.errors.B2bCounterpartyTooManyAdditionalContactsError
import io.portone.sdk.server.errors.B2bCounterpartyTooManyAdditionalContactsException
import io.portone.sdk.server.errors.B2bCounterpartyVerificationBrnMismatchError
import io.portone.sdk.server.errors.B2bCounterpartyVerificationBrnMismatchException
import io.portone.sdk.server.errors.B2bCounterpartyVerificationInvalidError
import io.portone.sdk.server.errors.B2bCounterpartyVerificationInvalidException
import io.portone.sdk.server.errors.B2bCounterpartyVerificationNotFoundError
import io.portone.sdk.server.errors.B2bCounterpartyVerificationNotFoundException
import io.portone.sdk.server.errors.B2bCounterpartyVerificationTypeMismatchError
import io.portone.sdk.server.errors.B2bCounterpartyVerificationTypeMismatchException
import io.portone.sdk.server.errors.B2bExternalServiceError
import io.portone.sdk.server.errors.B2bExternalServiceException
import io.portone.sdk.server.errors.B2bNotEnabledError
import io.portone.sdk.server.errors.B2bNotEnabledException
import io.portone.sdk.server.errors.CreateB2bCounterpartyError
import io.portone.sdk.server.errors.CreateB2bCounterpartyException
import io.portone.sdk.server.errors.DeleteB2bCounterpartyError
import io.portone.sdk.server.errors.DeleteB2bCounterpartyException
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetB2bCounterpartiesError
import io.portone.sdk.server.errors.GetB2bCounterpartiesException
import io.portone.sdk.server.errors.GetB2bCounterpartyCertificateError
import io.portone.sdk.server.errors.GetB2bCounterpartyCertificateException
import io.portone.sdk.server.errors.GetB2bCounterpartyCertificateRegistrationUrlError
import io.portone.sdk.server.errors.GetB2bCounterpartyCertificateRegistrationUrlException
import io.portone.sdk.server.errors.GetB2bCounterpartyError
import io.portone.sdk.server.errors.GetB2bCounterpartyException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.errors.UpdateB2bCounterpartyError
import io.portone.sdk.server.errors.UpdateB2bCounterpartyException
import io.portone.sdk.server.errors.ValidateB2bCounterpartyCertificateError
import io.portone.sdk.server.errors.ValidateB2bCounterpartyCertificateException
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
public class CounterpartyClient(
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
   * 사업자 인증서 등록 URL 조회
   *
   * 연동 사업자의 인증서를 등록하기 위한 URL을 조회합니다.
   *
   * @param brn
   * 사업자등록번호
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws GetB2bCounterpartyCertificateRegistrationUrlException
   */
  @JvmName("getB2bCounterpartyCertificateRegistrationUrlSuspend")
  public suspend fun getB2bCounterpartyCertificateRegistrationUrl(
    brn: String,
    test: Boolean? = null,
  ): GetB2bCounterpartyCertificateRegistrationUrlResponse {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("b2b", "counterparties", brn.toString(), "certificate", "registration-url")
        if (test != null) this.parameters.append("test", test.toString())
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
        json.decodeFromString<GetB2bCounterpartyCertificateRegistrationUrlError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bCounterpartyNotFoundError -> throw B2bCounterpartyNotFoundException(httpBodyDecoded)
        is B2bCounterpartyNtsNotConnectedError -> throw B2bCounterpartyNtsNotConnectedException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bCounterpartyCertificateRegistrationUrlResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bCounterpartyCertificateRegistrationUrl")
  public fun getB2bCounterpartyCertificateRegistrationUrlFuture(
    brn: String,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bCounterpartyCertificateRegistrationUrlResponse> = GlobalScope.future { getB2bCounterpartyCertificateRegistrationUrl(brn, test) }


  /**
   * 사업자 인증서 유효성 검증
   *
   * 연동 사업자가 등록한 인증서의 유효성을 검증합니다.
   *
   * @param brn
   * 사업자등록번호
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws ValidateB2bCounterpartyCertificateException
   */
  @JvmName("validateB2bCounterpartyCertificateSuspend")
  public suspend fun validateB2bCounterpartyCertificate(
    brn: String,
    test: Boolean? = null,
  ): ValidateB2bCounterpartyCertificateResponse {
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("b2b", "counterparties", brn.toString(), "certificate", "validate")
        if (test != null) this.parameters.append("test", test.toString())
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
        json.decodeFromString<ValidateB2bCounterpartyCertificateError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bCertificateUnregisteredError -> throw B2bCertificateUnregisteredException(httpBodyDecoded)
        is B2bCounterpartyNotFoundError -> throw B2bCounterpartyNotFoundException(httpBodyDecoded)
        is B2bCounterpartyNtsNotConnectedError -> throw B2bCounterpartyNtsNotConnectedException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ValidateB2bCounterpartyCertificateResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("validateB2bCounterpartyCertificate")
  public fun validateB2bCounterpartyCertificateFuture(
    brn: String,
    test: Boolean? = null,
  ): CompletableFuture<ValidateB2bCounterpartyCertificateResponse> = GlobalScope.future { validateB2bCounterpartyCertificate(brn, test) }


  /**
   * 인증서 조회
   *
   * 연동 사업자의 인증서를 조회합니다.
   *
   * @param brn
   * 사업자등록번호
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws GetB2bCounterpartyCertificateException
   */
  @JvmName("getB2bCounterpartyCertificateSuspend")
  public suspend fun getB2bCounterpartyCertificate(
    brn: String,
    test: Boolean? = null,
  ): B2bCertificate {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("b2b", "counterparties", brn.toString(), "certificate")
        if (test != null) this.parameters.append("test", test.toString())
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
        json.decodeFromString<GetB2bCounterpartyCertificateError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bCertificateUnregisteredError -> throw B2bCertificateUnregisteredException(httpBodyDecoded)
        is B2bCounterpartyNotFoundError -> throw B2bCounterpartyNotFoundException(httpBodyDecoded)
        is B2bCounterpartyNtsNotConnectedError -> throw B2bCounterpartyNtsNotConnectedException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bCertificate>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bCounterpartyCertificate")
  public fun getB2bCounterpartyCertificateFuture(
    brn: String,
    test: Boolean? = null,
  ): CompletableFuture<B2bCertificate> = GlobalScope.future { getB2bCounterpartyCertificate(brn, test) }


  /**
   * 거래처 조회
   *
   * 거래처를 조회합니다.
   *
   * @param counterpartyId
   * 거래처 ID
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws GetB2bCounterpartyException
   */
  @JvmName("getB2bCounterpartySuspend")
  public suspend fun getB2bCounterparty(
    counterpartyId: String,
    test: Boolean? = null,
  ): B2bCounterparty {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("b2b", "counterparties", counterpartyId.toString())
        if (test != null) this.parameters.append("test", test.toString())
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
        json.decodeFromString<GetB2bCounterpartyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bCounterpartyNotFoundError -> throw B2bCounterpartyNotFoundException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bCounterparty>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bCounterparty")
  public fun getB2bCounterpartyFuture(
    counterpartyId: String,
    test: Boolean? = null,
  ): CompletableFuture<B2bCounterparty> = GlobalScope.future { getB2bCounterparty(counterpartyId, test) }


  /**
   * 거래처 삭제
   *
   * 거래처를 삭제합니다.
   *
   * @param counterpartyId
   * 거래처 ID
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws DeleteB2bCounterpartyException
   */
  @JvmName("deleteB2bCounterpartySuspend")
  public suspend fun deleteB2bCounterparty(
    counterpartyId: String,
    test: Boolean? = null,
  ): DeleteB2bCounterpartyResponse {
    val requestBody = DeleteB2bCounterpartyBody(
    )
    val httpResponse = client.delete(apiBase) {
      url {
        this.appendPathSegments("b2b", "counterparties", counterpartyId.toString())
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
        json.decodeFromString<DeleteB2bCounterpartyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bCounterpartyNotFoundError -> throw B2bCounterpartyNotFoundException(httpBodyDecoded)
        is B2bCounterpartyOngoingTaxInvoiceExistsError -> throw B2bCounterpartyOngoingTaxInvoiceExistsException(httpBodyDecoded)
        is B2bCounterpartyPartnerNotDeletableError -> throw B2bCounterpartyPartnerNotDeletableException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<DeleteB2bCounterpartyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("deleteB2bCounterparty")
  public fun deleteB2bCounterpartyFuture(
    counterpartyId: String,
    test: Boolean? = null,
  ): CompletableFuture<DeleteB2bCounterpartyResponse> = GlobalScope.future { deleteB2bCounterparty(counterpartyId, test) }


  /**
   * 거래처 정보 수정
   *
   * 거래처 정보를 수정합니다.
   *
   * @param counterpartyId
   * 거래처 ID
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param counterparty
   * 거래처 정보
   * @param options
   * 확인 옵션
   *
   * 사업자 정보 및 휴폐업 상태 조회 옵션입니다.
   *
   * @throws UpdateB2bCounterpartyException
   */
  @JvmName("updateB2bCounterpartySuspend")
  public suspend fun updateB2bCounterparty(
    counterpartyId: String,
    test: Boolean? = null,
    counterparty: B2bCounterpartyInput,
    options: B2bCounterpartyCreateOptions? = null,
  ): UpdateB2bCounterpartyResponse {
    val requestBody = UpdateB2bCounterpartyBody(
      counterparty = counterparty,
      options = options,
    )
    val httpResponse = client.patch(apiBase) {
      url {
        this.appendPathSegments("b2b", "counterparties", counterpartyId.toString())
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
        json.decodeFromString<UpdateB2bCounterpartyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bCounterpartyBrnModificationNotAllowedError -> throw B2bCounterpartyBrnModificationNotAllowedException(httpBodyDecoded)
        is B2bCounterpartyMissingRequiredFieldsError -> throw B2bCounterpartyMissingRequiredFieldsException(httpBodyDecoded)
        is B2bCounterpartyNotFoundError -> throw B2bCounterpartyNotFoundException(httpBodyDecoded)
        is B2bCounterpartyPartnerNotUpdatableError -> throw B2bCounterpartyPartnerNotUpdatableException(httpBodyDecoded)
        is B2bCounterpartyTooManyAdditionalContactsError -> throw B2bCounterpartyTooManyAdditionalContactsException(httpBodyDecoded)
        is B2bCounterpartyVerificationBrnMismatchError -> throw B2bCounterpartyVerificationBrnMismatchException(httpBodyDecoded)
        is B2bCounterpartyVerificationInvalidError -> throw B2bCounterpartyVerificationInvalidException(httpBodyDecoded)
        is B2bCounterpartyVerificationNotFoundError -> throw B2bCounterpartyVerificationNotFoundException(httpBodyDecoded)
        is B2bCounterpartyVerificationTypeMismatchError -> throw B2bCounterpartyVerificationTypeMismatchException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdateB2bCounterpartyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updateB2bCounterparty")
  public fun updateB2bCounterpartyFuture(
    counterpartyId: String,
    test: Boolean? = null,
    counterparty: B2bCounterpartyInput,
    options: B2bCounterpartyCreateOptions? = null,
  ): CompletableFuture<UpdateB2bCounterpartyResponse> = GlobalScope.future { updateB2bCounterparty(counterpartyId, test, counterparty, options) }


  /**
   * 거래처 검색
   *
   * 거래처를 검색합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param page
   * 페이지 정보
   * @param filter
   * 검색 필터
   *
   * @throws GetB2bCounterpartiesException
   */
  @JvmName("getB2bCounterpartiesSuspend")
  public suspend fun getB2bCounterparties(
    test: Boolean? = null,
    page: PageInput? = null,
    filter: B2bCounterpartyFilter? = null,
  ): GetB2bCounterpartiesResponse {
    val requestBody = GetB2bCounterpartiesBody(
      page = page,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("b2b", "counterparties")
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
        json.decodeFromString<GetB2bCounterpartiesError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bCounterpartiesResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bCounterparties")
  public fun getB2bCounterpartiesFuture(
    test: Boolean? = null,
    page: PageInput? = null,
    filter: B2bCounterpartyFilter? = null,
  ): CompletableFuture<GetB2bCounterpartiesResponse> = GlobalScope.future { getB2bCounterparties(test, page, filter) }


  /**
   * 거래처 생성
   *
   * 거래처를 생성합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param counterpartyId
   * 거래처 아이디
   *
   * 입력하지 않으면 임의의 ID가 채번됩니다.
   * @param counterparty
   * 거래처 정보
   * @param options
   * 거래처 생성 옵션
   *
   * @throws CreateB2bCounterpartyException
   */
  @JvmName("createB2bCounterpartySuspend")
  public suspend fun createB2bCounterparty(
    test: Boolean? = null,
    counterpartyId: String? = null,
    counterparty: B2bCounterpartyInput,
    options: B2bCounterpartyCreateOptions? = null,
  ): CreateB2bCounterpartyResponse {
    val requestBody = CreateB2bCounterpartyBody(
      counterpartyId = counterpartyId,
      counterparty = counterparty,
      options = options,
    )
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("b2b", "counterparties")
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
        json.decodeFromString<CreateB2bCounterpartyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bCounterpartyBrnInvalidError -> throw B2bCounterpartyBrnInvalidException(httpBodyDecoded)
        is B2bCounterpartyIdAlreadyExistsError -> throw B2bCounterpartyIdAlreadyExistsException(httpBodyDecoded)
        is B2bCounterpartyIdAlreadyExistsByPartnerError -> throw B2bCounterpartyIdAlreadyExistsByPartnerException(httpBodyDecoded)
        is B2bCounterpartyMissingRequiredFieldsError -> throw B2bCounterpartyMissingRequiredFieldsException(httpBodyDecoded)
        is B2bCounterpartyNtsConnectionFailedError -> throw B2bCounterpartyNtsConnectionFailedException(httpBodyDecoded)
        is B2bCounterpartyPartnerNotConnectableError -> throw B2bCounterpartyPartnerNotConnectableException(httpBodyDecoded)
        is B2bCounterpartySelfOriginBrnMismatchError -> throw B2bCounterpartySelfOriginBrnMismatchException(httpBodyDecoded)
        is B2bCounterpartyTooManyAdditionalContactsError -> throw B2bCounterpartyTooManyAdditionalContactsException(httpBodyDecoded)
        is B2bCounterpartyVerificationBrnMismatchError -> throw B2bCounterpartyVerificationBrnMismatchException(httpBodyDecoded)
        is B2bCounterpartyVerificationInvalidError -> throw B2bCounterpartyVerificationInvalidException(httpBodyDecoded)
        is B2bCounterpartyVerificationNotFoundError -> throw B2bCounterpartyVerificationNotFoundException(httpBodyDecoded)
        is B2bCounterpartyVerificationTypeMismatchError -> throw B2bCounterpartyVerificationTypeMismatchException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreateB2bCounterpartyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createB2bCounterparty")
  public fun createB2bCounterpartyFuture(
    test: Boolean? = null,
    counterpartyId: String? = null,
    counterparty: B2bCounterpartyInput,
    options: B2bCounterpartyCreateOptions? = null,
  ): CompletableFuture<CreateB2bCounterpartyResponse> = GlobalScope.future { createB2bCounterparty(test, counterpartyId, counterparty, options) }

  override fun close() {
    client.close()
  }
}
