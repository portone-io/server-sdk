package io.portone.sdk.server.b2b.membercompany

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.request.`get`
import io.ktor.client.request.accept
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
import io.portone.sdk.server.b2b.membercompany.B2bCertificate
import io.portone.sdk.server.b2b.membercompany.B2bCompanyContactInput
import io.portone.sdk.server.b2b.membercompany.B2bCompanyState
import io.portone.sdk.server.b2b.membercompany.B2bMemberCompany
import io.portone.sdk.server.b2b.membercompany.B2bMemberCompanyInput
import io.portone.sdk.server.b2b.membercompany.GetB2bBankAccountHolderResponse
import io.portone.sdk.server.b2b.membercompany.GetB2bCertificateRegistrationUrlResponse
import io.portone.sdk.server.b2b.membercompany.Input
import io.portone.sdk.server.b2b.membercompany.RegisterB2bMemberCompanyBody
import io.portone.sdk.server.b2b.membercompany.RegisterB2bMemberCompanyResponse
import io.portone.sdk.server.b2b.membercompany.UpdateB2bMemberCompanyBody
import io.portone.sdk.server.b2b.membercompany.UpdateB2bMemberCompanyResponse
import io.portone.sdk.server.b2b.membercompany.ValidateB2bCertificateResponse
import io.portone.sdk.server.common.Bank
import io.portone.sdk.server.errors.B2bBankAccountNotFoundError
import io.portone.sdk.server.errors.B2bBankAccountNotFoundException
import io.portone.sdk.server.errors.B2bCertificateUnregisteredError
import io.portone.sdk.server.errors.B2bCertificateUnregisteredException
import io.portone.sdk.server.errors.B2bCompanyAlreadyRegisteredError
import io.portone.sdk.server.errors.B2bCompanyAlreadyRegisteredException
import io.portone.sdk.server.errors.B2bCompanyNotFoundError
import io.portone.sdk.server.errors.B2bCompanyNotFoundException
import io.portone.sdk.server.errors.B2bExternalServiceError
import io.portone.sdk.server.errors.B2bExternalServiceException
import io.portone.sdk.server.errors.B2bFinancialSystemCommunicationError
import io.portone.sdk.server.errors.B2bFinancialSystemCommunicationException
import io.portone.sdk.server.errors.B2bFinancialSystemFailureError
import io.portone.sdk.server.errors.B2bFinancialSystemFailureException
import io.portone.sdk.server.errors.B2bFinancialSystemUnderMaintenanceError
import io.portone.sdk.server.errors.B2bFinancialSystemUnderMaintenanceException
import io.portone.sdk.server.errors.B2bForeignExchangeAccountError
import io.portone.sdk.server.errors.B2bForeignExchangeAccountException
import io.portone.sdk.server.errors.B2bHometaxUnderMaintenanceError
import io.portone.sdk.server.errors.B2bHometaxUnderMaintenanceException
import io.portone.sdk.server.errors.B2bIdAlreadyExistsError
import io.portone.sdk.server.errors.B2bIdAlreadyExistsException
import io.portone.sdk.server.errors.B2bMemberCompanyNotFoundError
import io.portone.sdk.server.errors.B2bMemberCompanyNotFoundException
import io.portone.sdk.server.errors.B2bNotEnabledError
import io.portone.sdk.server.errors.B2bNotEnabledException
import io.portone.sdk.server.errors.B2bRegularMaintenanceTimeError
import io.portone.sdk.server.errors.B2bRegularMaintenanceTimeException
import io.portone.sdk.server.errors.B2bSuspendedAccountError
import io.portone.sdk.server.errors.B2bSuspendedAccountException
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetB2bAccountHolderError
import io.portone.sdk.server.errors.GetB2bCertificateError
import io.portone.sdk.server.errors.GetB2bCertificateRegistrationUrlError
import io.portone.sdk.server.errors.GetB2bCompanyStateError
import io.portone.sdk.server.errors.GetB2bMemberCompanyError
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.RegisterB2bMemberCompanyError
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.errors.UpdateB2bMemberCompanyError
import io.portone.sdk.server.errors.ValidateB2bCertificateError
import java.io.Closeable
import java.util.concurrent.CompletableFuture
import kotlin.String
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json

public class MemberCompanyClient internal constructor(
  private val apiSecret: String,
  private val apiBase: String,
  private val storeId: String?,
) {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 연동 사업자 조회
   *
   * 포트원 B2B 서비스에 연동된 사업자를 조회합니다.
   *
   * @param brn
   * 사업자등록번호
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bMemberCompanyNotFoundException 연동 사업자가 존재하지 않는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bMemberCompanySuspend")
  public suspend fun getB2bMemberCompany(
    brn: String,
    test: Boolean? = null,
  ): B2bMemberCompany {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b", "member-companies", brn.toString())
        if (test != null) parameters.append("test", test.toString())
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
        json.decodeFromString<GetB2bMemberCompanyError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bMemberCompanyNotFoundError -> throw B2bMemberCompanyNotFoundException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bMemberCompany>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bMemberCompany")
  public suspend fun getB2bMemberCompanyFuture(
    brn: String,
    test: Boolean? = null,
  ): CompletableFuture<B2bMemberCompany> = GlobalScope.future { getB2bMemberCompany(brn, test) }


  /**
   * 연동 사업자 정보 수정
   *
   * 연동 사업자 정보를 수정합니다.
   *
   * @param brn
   * 사업자등록번호
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param companyName
   * 회사명
   * @param representativeName
   * 대표자 성명
   * @param address
   * 회사 주소
   * @param businessType
   * 업태
   * @param businessClass
   * 업종
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bMemberCompanyNotFoundException 연동 사업자가 존재하지 않는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("updateB2bMemberCompanySuspend")
  public suspend fun updateB2bMemberCompany(
    brn: String,
    test: Boolean? = null,
    companyName: String? = null,
    representativeName: String? = null,
    address: String? = null,
    businessType: String? = null,
    businessClass: String? = null,
  ): UpdateB2bMemberCompanyResponse {
    val requestBody = UpdateB2bMemberCompanyBody(
      companyName = companyName,
      representativeName = representativeName,
      address = address,
      businessType = businessType,
      businessClass = businessClass,
    )
    val httpResponse = client.patch(apiBase) {
      url {
        appendPathSegments("b2b", "member-companies", brn.toString())
        if (test != null) parameters.append("test", test.toString())
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
        json.decodeFromString<UpdateB2bMemberCompanyError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bMemberCompanyNotFoundError -> throw B2bMemberCompanyNotFoundException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdateB2bMemberCompanyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updateB2bMemberCompany")
  public suspend fun updateB2bMemberCompanyFuture(
    brn: String,
    test: Boolean? = null,
    companyName: String? = null,
    representativeName: String? = null,
    address: String? = null,
    businessType: String? = null,
    businessClass: String? = null,
  ): CompletableFuture<UpdateB2bMemberCompanyResponse> = GlobalScope.future { updateB2bMemberCompany(brn, test, companyName, representativeName, address, businessType, businessClass) }


  /**
   * 사업자 연동
   *
   * 포트원 B2B 서비스에 사업자를 연동합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param company
   * 사업자 정보
   * @param contact
   * 담당자 정보
   *
   * @throws B2bCompanyAlreadyRegisteredException 사업자가 이미 연동되어 있는 경우
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bIdAlreadyExistsException ID가 이미 사용중인 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("registerB2bMemberCompanySuspend")
  public suspend fun registerB2bMemberCompany(
    test: Boolean? = null,
    company: B2bMemberCompanyInput,
    contact: B2bCompanyContactInput,
  ): RegisterB2bMemberCompanyResponse {
    val requestBody = RegisterB2bMemberCompanyBody(
      company = company,
      contact = contact,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("b2b", "member-companies")
        if (test != null) parameters.append("test", test.toString())
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
        json.decodeFromString<RegisterB2bMemberCompanyError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bCompanyAlreadyRegisteredError -> throw B2bCompanyAlreadyRegisteredException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bIdAlreadyExistsError -> throw B2bIdAlreadyExistsException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<RegisterB2bMemberCompanyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("registerB2bMemberCompany")
  public suspend fun registerB2bMemberCompanyFuture(
    test: Boolean? = null,
    company: B2bMemberCompanyInput,
    contact: B2bCompanyContactInput,
  ): CompletableFuture<RegisterB2bMemberCompanyResponse> = GlobalScope.future { registerB2bMemberCompany(test, company, contact) }


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
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bMemberCompanyNotFoundException 연동 사업자가 존재하지 않는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bCertificateRegistrationUrlSuspend")
  public suspend fun getB2bCertificateRegistrationUrl(
    brn: String,
    test: Boolean? = null,
  ): GetB2bCertificateRegistrationUrlResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b", "member-companies", brn.toString(), "certificate", "registration-url")
        if (test != null) parameters.append("test", test.toString())
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
        json.decodeFromString<GetB2bCertificateRegistrationUrlError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bMemberCompanyNotFoundError -> throw B2bMemberCompanyNotFoundException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bCertificateRegistrationUrlResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bCertificateRegistrationUrl")
  public suspend fun getB2bCertificateRegistrationUrlFuture(
    brn: String,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bCertificateRegistrationUrlResponse> = GlobalScope.future { getB2bCertificateRegistrationUrl(brn, test) }


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
   * @throws B2bCertificateUnregisteredException 인증서가 등록되어 있지 않은 경우
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bMemberCompanyNotFoundException 연동 사업자가 존재하지 않는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("validateB2bCertificateSuspend")
  public suspend fun validateB2bCertificate(
    brn: String,
    test: Boolean? = null,
  ): ValidateB2bCertificateResponse {
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("b2b", "member-companies", brn.toString(), "certificate", "validate")
        if (test != null) parameters.append("test", test.toString())
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
        json.decodeFromString<ValidateB2bCertificateError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bCertificateUnregisteredError -> throw B2bCertificateUnregisteredException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bMemberCompanyNotFoundError -> throw B2bMemberCompanyNotFoundException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ValidateB2bCertificateResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("validateB2bCertificate")
  public suspend fun validateB2bCertificateFuture(
    brn: String,
    test: Boolean? = null,
  ): CompletableFuture<ValidateB2bCertificateResponse> = GlobalScope.future { validateB2bCertificate(brn, test) }


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
   * @throws B2bCertificateUnregisteredException 인증서가 등록되어 있지 않은 경우
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bMemberCompanyNotFoundException 연동 사업자가 존재하지 않는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bCertificateSuspend")
  public suspend fun getB2bCertificate(
    brn: String,
    test: Boolean? = null,
  ): B2bCertificate {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b", "member-companies", brn.toString(), "certificate")
        if (test != null) parameters.append("test", test.toString())
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
        json.decodeFromString<GetB2bCertificateError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bCertificateUnregisteredError -> throw B2bCertificateUnregisteredException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bMemberCompanyNotFoundError -> throw B2bMemberCompanyNotFoundException(httpBodyDecoded)
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
  @JvmName("getB2bCertificate")
  public suspend fun getB2bCertificateFuture(
    brn: String,
    test: Boolean? = null,
  ): CompletableFuture<B2bCertificate> = GlobalScope.future { getB2bCertificate(brn, test) }


  /**
   * 예금주 조회
   *
   * 원하는 계좌의 예금주를 조회합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param bank
   * 은행
   * @param accountNumber
   * 계좌번호
   *
   * @throws B2bBankAccountNotFoundException 계좌가 존재하지 않는 경우
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bFinancialSystemCommunicationException 금융기관과의 통신에 실패한 경우
   * @throws B2bFinancialSystemFailureException 금융기관 장애
   * @throws B2bFinancialSystemUnderMaintenanceException 금융기관 시스템이 점검 중인 경우
   * @throws B2bForeignExchangeAccountException 계좌 정보 조회가 불가능한 외화 계좌인 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bRegularMaintenanceTimeException 금융기관 시스템이 정기 점검 중인 경우
   * @throws B2bSuspendedAccountException 정지 계좌인 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bBankAccountHolderSuspend")
  public suspend fun getB2bBankAccountHolder(
    test: Boolean? = null,
    bank: Bank,
    accountNumber: String,
  ): GetB2bBankAccountHolderResponse {
    val requestBody = Input(
      bank = bank,
      accountNumber = accountNumber,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("b2b", "bank-accounts", "holder")
        if (test != null) parameters.append("test", test.toString())
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
        json.decodeFromString<GetB2bAccountHolderError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bBankAccountNotFoundError -> throw B2bBankAccountNotFoundException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bFinancialSystemCommunicationError -> throw B2bFinancialSystemCommunicationException(httpBodyDecoded)
        is B2bFinancialSystemFailureError -> throw B2bFinancialSystemFailureException(httpBodyDecoded)
        is B2bFinancialSystemUnderMaintenanceError -> throw B2bFinancialSystemUnderMaintenanceException(httpBodyDecoded)
        is B2bForeignExchangeAccountError -> throw B2bForeignExchangeAccountException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bRegularMaintenanceTimeError -> throw B2bRegularMaintenanceTimeException(httpBodyDecoded)
        is B2bSuspendedAccountError -> throw B2bSuspendedAccountException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bBankAccountHolderResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bBankAccountHolder")
  public suspend fun getB2bBankAccountHolderFuture(
    test: Boolean? = null,
    bank: Bank,
    accountNumber: String,
  ): CompletableFuture<GetB2bBankAccountHolderResponse> = GlobalScope.future { getB2bBankAccountHolder(test, bank, accountNumber) }


  /**
   * 사업자 상태 조회
   *
   * 원하는 사업자의 상태를 조회합니다. 포트원 B2B 서비스에 연동 및 등록되지 않은 사업자도 조회 가능합니다.
   *
   * @param brn
   * 사업자등록번호
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bCompanyNotFoundException 사업자가 존재하지 않는 경우
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bHometaxUnderMaintenanceException 홈택스가 점검중이거나 순단이 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bCompanyStateSuspend")
  public suspend fun getB2bCompanyState(
    brn: String,
    test: Boolean? = null,
  ): B2bCompanyState {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b", "companies", brn.toString(), "state")
        if (test != null) parameters.append("test", test.toString())
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
        json.decodeFromString<GetB2bCompanyStateError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bCompanyNotFoundError -> throw B2bCompanyNotFoundException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bHometaxUnderMaintenanceError -> throw B2bHometaxUnderMaintenanceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bCompanyState>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bCompanyState")
  public suspend fun getB2bCompanyStateFuture(
    brn: String,
    test: Boolean? = null,
  ): CompletableFuture<B2bCompanyState> = GlobalScope.future { getB2bCompanyState(brn, test) }

  internal fun close() {
    client.close()
  }
}
