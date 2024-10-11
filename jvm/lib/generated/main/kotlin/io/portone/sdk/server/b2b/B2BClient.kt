package io.portone.sdk.server

import io.ktor.client.HttpClient
import io.portone.sdk.server.B2bCertificate
import io.portone.sdk.server.B2bCompanyContact
import io.portone.sdk.server.B2bCompanyState
import io.portone.sdk.server.B2bMemberCompany
import io.portone.sdk.server.B2bTaxInvoice
import io.portone.sdk.server.CreateB2bTaxInvoiceFileUploadLinkResponse
import io.portone.sdk.server.GetB2bBankAccountHolderResponse
import io.portone.sdk.server.GetB2bCertificateRegistrationUrlResponse
import io.portone.sdk.server.GetB2bContactIdExistenceResponse
import io.portone.sdk.server.GetB2bTaxInvoiceAttachmentsResponse
import io.portone.sdk.server.GetB2bTaxInvoicePdfDownloadUrlResponse
import io.portone.sdk.server.GetB2bTaxInvoicePopupUrlResponse
import io.portone.sdk.server.GetB2bTaxInvoicePrintUrlResponse
import io.portone.sdk.server.GetB2bTaxInvoicesResponse
import io.portone.sdk.server.RegisterB2bMemberCompanyResponse
import io.portone.sdk.server.UpdateB2bMemberCompanyContactResponse
import io.portone.sdk.server.UpdateB2bMemberCompanyResponse
import io.portone.sdk.server.b2b.B2bCertificate
import io.portone.sdk.server.b2b.B2bCompanyContact
import io.portone.sdk.server.b2b.B2bCompanyContactInput
import io.portone.sdk.server.b2b.B2bCompanyState
import io.portone.sdk.server.b2b.B2bMemberCompany
import io.portone.sdk.server.b2b.B2bSearchDateType
import io.portone.sdk.server.b2b.B2bTaxInvoice
import io.portone.sdk.server.b2b.B2bTaxInvoiceDocumentKeyType
import io.portone.sdk.server.b2b.B2bTaxInvoiceInput
import io.portone.sdk.server.b2b.CreateB2bTaxInvoiceFileUploadLinkResponse
import io.portone.sdk.server.b2b.GetB2bBankAccountHolderResponse
import io.portone.sdk.server.b2b.GetB2bCertificateRegistrationUrlResponse
import io.portone.sdk.server.b2b.GetB2bContactIdExistenceResponse
import io.portone.sdk.server.b2b.GetB2bTaxInvoiceAttachmentsResponse
import io.portone.sdk.server.b2b.GetB2bTaxInvoicePdfDownloadUrlResponse
import io.portone.sdk.server.b2b.GetB2bTaxInvoicePopupUrlResponse
import io.portone.sdk.server.b2b.GetB2bTaxInvoicePrintUrlResponse
import io.portone.sdk.server.b2b.GetB2bTaxInvoicesResponse
import io.portone.sdk.server.b2b.RegisterB2bMemberCompanyResponse
import io.portone.sdk.server.b2b.UpdateB2bMemberCompanyContactResponse
import io.portone.sdk.server.b2b.UpdateB2bMemberCompanyResponse
import io.portone.sdk.server.common.Bank
import java.io.Closeable
import kotlin.String
import kotlinx.serialization.json.Json

public class B2BClient(
  private val apiSecret: String,
  private val storeId: String,
  private val apiBase: String,
) : Closeable {
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
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bMemberCompanySuspend")
  public suspend fun getB2bMemberCompany(
    brn: string,
    test: Boolean? = null,
  ): B2bMemberCompany {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "member-companies", brn)
        if (test != null) parameters.append("test", test)
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
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bMemberCompany>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bMemberCompany")
  public suspend fun getB2bMemberCompanyFuture(
    brn: string,
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
   * @param name
   * 회사명
   * @param ceoName
   * 대표자 성명
   * @param address
   * 회사 주소
   * @param businessType
   * 업태
   * @param businessClass
   * 업종
   *
   * @throws B2bMemberCompanyNotFoundException 연동 사업자가 존재하지 않는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("updateB2bMemberCompanySuspend")
  public suspend fun updateB2bMemberCompany(
    brn: string,
    test: Boolean? = null,
    name: string? = null,
    ceoName: string? = null,
    address: string? = null,
    businessType: string? = null,
    businessClass: string? = null,
  ): UpdateB2bMemberCompanyResponse {
    val requestBody = UpdateB2bMemberCompanyBody(
      name = name,
      ceoName = ceoName,
      address = address,
      businessType = businessType,
      businessClass = businessClass,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "member-companies", brn)
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<UpdateB2bMemberCompanyError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bMemberCompanyNotFoundError -> throw B2bMemberCompanyNotFoundException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdateB2bMemberCompanyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updateB2bMemberCompany")
  public suspend fun updateB2bMemberCompanyFuture(
    brn: string,
    test: Boolean? = null,
    name: string? = null,
    ceoName: string? = null,
    address: string? = null,
    businessType: string? = null,
    businessClass: string? = null,
  ): CompletableFuture<UpdateB2bMemberCompanyResponse> = GlobalScope.future { updateB2bMemberCompany(brn, test, name, ceoName, address, businessType, businessClass) }


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
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("registerB2bMemberCompanySuspend")
  public suspend fun registerB2bMemberCompany(
    test: Boolean? = null,
    company: B2bMemberCompany,
    contact: B2bCompanyContactInput,
  ): RegisterB2bMemberCompanyResponse {
    val requestBody = RegisterB2bMemberCompanyBody(
      company = company,
      contact = contact,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "member-companies")
        if (test != null) parameters.append("test", test)
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
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<RegisterB2bMemberCompanyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("registerB2bMemberCompany")
  public suspend fun registerB2bMemberCompanyFuture(
    test: Boolean? = null,
    company: B2bMemberCompany,
    contact: B2bCompanyContactInput,
  ): CompletableFuture<RegisterB2bMemberCompanyResponse> = GlobalScope.future { registerB2bMemberCompany(test, company, contact) }


  /**
   * 담당자 조회
   *
   * 연동 사업자에 등록된 담당자를 조회합니다.
   *
   * @param brn
   * 사업자등록번호
   * @param contactId
   * 담당자 ID
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bContactNotFoundException 담당자가 존재하지 않는 경우
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bMemberCompanyNotFoundException 연동 사업자가 존재하지 않는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bMemberCompanyContactSuspend")
  public suspend fun getB2bMemberCompanyContact(
    brn: string,
    contactId: string,
    test: Boolean? = null,
  ): B2bCompanyContact {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "member-companies", brn, "contacts", contactId)
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<GetB2bMemberCompanyContactError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bContactNotFoundError -> throw B2bContactNotFoundException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bMemberCompanyNotFoundError -> throw B2bMemberCompanyNotFoundException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bCompanyContact>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bMemberCompanyContact")
  public suspend fun getB2bMemberCompanyContactFuture(
    brn: string,
    contactId: string,
    test: Boolean? = null,
  ): CompletableFuture<B2bCompanyContact> = GlobalScope.future { getB2bMemberCompanyContact(brn, contactId, test) }


  /**
   * 담당자 정보 수정
   *
   * 담당자 정보를 수정합니다.
   *
   * @param brn
   * 사업자등록번호
   * @param contactId
   * 담당자 ID
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param password
   * 비밀번호
   * @param name
   * 담당자 성명
   * @param phoneNumber
   * 담당자 핸드폰 번호
   * @param email
   * 담당자 이메일
   *
   * @throws B2bContactNotFoundException 담당자가 존재하지 않는 경우
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bMemberCompanyNotFoundException 연동 사업자가 존재하지 않는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("updateB2bMemberCompanyContactSuspend")
  public suspend fun updateB2bMemberCompanyContact(
    brn: string,
    contactId: string,
    test: Boolean? = null,
    password: string? = null,
    name: string? = null,
    phoneNumber: string? = null,
    email: string? = null,
  ): UpdateB2bMemberCompanyContactResponse {
    val requestBody = UpdateB2bMemberCompanyContactBody(
      password = password,
      name = name,
      phoneNumber = phoneNumber,
      email = email,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "member-companies", brn, "contacts", contactId)
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<UpdateB2bMemberCompanyContactError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bContactNotFoundError -> throw B2bContactNotFoundException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bMemberCompanyNotFoundError -> throw B2bMemberCompanyNotFoundException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdateB2bMemberCompanyContactResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updateB2bMemberCompanyContact")
  public suspend fun updateB2bMemberCompanyContactFuture(
    brn: string,
    contactId: string,
    test: Boolean? = null,
    password: string? = null,
    name: string? = null,
    phoneNumber: string? = null,
    email: string? = null,
  ): CompletableFuture<UpdateB2bMemberCompanyContactResponse> = GlobalScope.future { updateB2bMemberCompanyContact(brn, contactId, test, password, name, phoneNumber, email) }


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
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bCertificateRegistrationUrlSuspend")
  public suspend fun getB2bCertificateRegistrationUrl(
    brn: string,
    test: Boolean? = null,
  ): GetB2bCertificateRegistrationUrlResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "member-companies", brn, "certificate", "registration-url")
        if (test != null) parameters.append("test", test)
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
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bCertificateRegistrationUrlResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bCertificateRegistrationUrl")
  public suspend fun getB2bCertificateRegistrationUrlFuture(
    brn: string,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bCertificateRegistrationUrlResponse> = GlobalScope.future { getB2bCertificateRegistrationUrl(brn, test) }


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
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bCertificateSuspend")
  public suspend fun getB2bCertificate(
    brn: string,
    test: Boolean? = null,
  ): B2bCertificate {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "member-companies", brn, "certificate")
        if (test != null) parameters.append("test", test)
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
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bCertificate>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bCertificate")
  public suspend fun getB2bCertificateFuture(
    brn: string,
    test: Boolean? = null,
  ): CompletableFuture<B2bCertificate> = GlobalScope.future { getB2bCertificate(brn, test) }


  /**
   * 담당자 ID 존재 여부 확인
   *
   * 담당자 ID가 이미 사용중인지 확인합니다.
   *
   * @param contactId
   * 담당자 ID
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bContactIdExistenceSuspend")
  public suspend fun getB2bContactIdExistence(
    contactId: string,
    test: Boolean? = null,
  ): GetB2bContactIdExistenceResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "member-companies", "contacts", "id-existence")
        parameters.append("contactId", contactId)
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<getB2bContactIdExistenceError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bContactIdExistenceResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bContactIdExistence")
  public suspend fun getB2bContactIdExistenceFuture(
    contactId: string,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bContactIdExistenceResponse> = GlobalScope.future { getB2bContactIdExistence(contactId, test) }


  /**
   * 예금주 조회
   *
   * 원하는 계좌의 예금주를 조회합니다.
   *
   * @param bank
   * 은행
   * @param accountNumber
   * '-'를 제외한 계좌 번호
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
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
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bBankAccountHolderSuspend")
  public suspend fun getB2bBankAccountHolder(
    bank: Bank,
    accountNumber: string,
    test: Boolean? = null,
  ): GetB2bBankAccountHolderResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "bank-accounts", bank, accountNumber, "holder")
        if (test != null) parameters.append("test", test)
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
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bBankAccountHolderResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bBankAccountHolder")
  public suspend fun getB2bBankAccountHolderFuture(
    bank: Bank,
    accountNumber: string,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bBankAccountHolderResponse> = GlobalScope.future { getB2bBankAccountHolder(bank, accountNumber, test) }


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
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bCompanyStateSuspend")
  public suspend fun getB2bCompanyState(
    brn: string,
    test: Boolean? = null,
  ): B2bCompanyState {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "company", brn, "state")
        if (test != null) parameters.append("test", test)
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
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bCompanyState>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bCompanyState")
  public suspend fun getB2bCompanyStateFuture(
    brn: string,
    test: Boolean? = null,
  ): CompletableFuture<B2bCompanyState> = GlobalScope.future { getB2bCompanyState(brn, test) }


  /**
   * 세금계산서 역발행 요청
   *
   * 공급자에게 세금계산서 역발행을 요청합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param taxInvoice
   * 세금계산서 생성 요청 정보
   * @param memo
   * 메모
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bRecipientNotFoundException 공급받는자가 존재하지 않은 경우
   * @throws B2bSupplierNotFoundException 공급자가 존재하지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("requestB2bTaxInvoiceReverseIssuanceSuspend")
  public suspend fun requestB2bTaxInvoiceReverseIssuance(
    test: Boolean? = null,
    taxInvoice: B2bTaxInvoiceInput,
    memo: string? = null,
  ): B2bTaxInvoice {
    val requestBody = RequestB2bTaxInvoiceReverseIssuanceRequestBody(
      taxInvoice = taxInvoice,
      memo = memo,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", "request-reverse-issuance")
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<RequestB2bTaxInvoiceReverseIssuanceError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bRecipientNotFoundError -> throw B2bRecipientNotFoundException(httpBodyDecoded)
        is B2bSupplierNotFoundError -> throw B2bSupplierNotFoundException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bTaxInvoice>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("requestB2bTaxInvoiceReverseIssuance")
  public suspend fun requestB2bTaxInvoiceReverseIssuanceFuture(
    test: Boolean? = null,
    taxInvoice: B2bTaxInvoiceInput,
    memo: string? = null,
  ): CompletableFuture<B2bTaxInvoice> = GlobalScope.future { requestB2bTaxInvoiceReverseIssuance(test, taxInvoice, memo) }


  /**
   * 세금 계산서 조회
   *
   * 등록된 세금 계산서를 공급자 혹은 공급받는자 문서번호로 조회합니다.
   *
   * @param documentKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param documentKeyType
   * 문서 번호 유형
   *
   * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bTaxInvoiceSuspend")
  public suspend fun getB2bTaxInvoice(
    documentKey: string,
    brn: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    test: Boolean? = null,
  ): B2bTaxInvoice {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", documentKey)
        parameters.append("brn", brn)
        if (documentKeyType != null) parameters.append("documentKeyType", documentKeyType)
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<GetB2bTaxInvoiceError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bTaxInvoice>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bTaxInvoice")
  public suspend fun getB2bTaxInvoiceFuture(
    documentKey: string,
    brn: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    test: Boolean? = null,
  ): CompletableFuture<B2bTaxInvoice> = GlobalScope.future { getB2bTaxInvoice(documentKey, brn, documentKeyType, test) }


  /**
   * 세금계산서 삭제
   *
   * 세금계산서를 삭제합니다.
   *
   * @param documentKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param documentKeyType
   * 문서 번호 유형
   *
   * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNonDeletableStatusException 세금계산서가 삭제 가능한 상태가 아닌 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("deleteB2bTaxInvoiceSuspend")
  public suspend fun deleteB2bTaxInvoice(
    documentKey: string,
    brn: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    test: Boolean? = null,
  ) {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", documentKey)
        parameters.append("brn", brn)
        if (documentKeyType != null) parameters.append("documentKeyType", documentKeyType)
        if (test != null) parameters.append("test", test)
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<DeleteB2bTaxInvoiceError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNonDeletableStatusError -> throw B2bTaxInvoiceNonDeletableStatusException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
  }

  /** @suppress */
  @JvmName("deleteB2bTaxInvoice")
  public suspend fun deleteB2bTaxInvoiceFuture(
    documentKey: string,
    brn: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    test: Boolean? = null,
  ) = GlobalScope.future { deleteB2bTaxInvoice(documentKey, brn, documentKeyType, test) }


  /**
   * 세금계산서 발행
   *
   * 역발행의 경우 역발행요청(REQUESTED) 상태, 정발행의 경우 임시저장(REGISTERED) 상태의 세금계산서를 발행합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param brn
   * 사업자등록번호
   * @param documentKey
   * 세금계산서 문서 번호
   * @param documentKeyType
   * 문서 번호 유형
   *
   * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param memo
   * 메모
   * @param emailSubject
   * 이메일 제목
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotRequestedStatusException 세금계산서가 역발행 대기 상태가 아닌 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("issueB2bTaxInvoiceSuspend")
  public suspend fun issueB2bTaxInvoice(
    test: Boolean? = null,
    brn: string,
    documentKey: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    memo: string? = null,
    emailSubject: string? = null,
  ): B2bTaxInvoice {
    val requestBody = IssueB2bTaxInvoiceRequestBody(
      brn = brn,
      documentKey = documentKey,
      documentKeyType = documentKeyType,
      memo = memo,
      emailSubject = emailSubject,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", "issue")
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<IssueB2bTaxInvoiceError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceNotRequestedStatusError -> throw B2bTaxInvoiceNotRequestedStatusException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bTaxInvoice>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("issueB2bTaxInvoice")
  public suspend fun issueB2bTaxInvoiceFuture(
    test: Boolean? = null,
    brn: string,
    documentKey: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    memo: string? = null,
    emailSubject: string? = null,
  ): CompletableFuture<B2bTaxInvoice> = GlobalScope.future { issueB2bTaxInvoice(test, brn, documentKey, documentKeyType, memo, emailSubject) }


  /**
   * 세금계산서 역발행 요청 취소
   *
   * 공급받는자가 공급자에게 세금계산서 역발행 요청한 것을 취소합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param brn
   * 사업자등록번호
   * @param documentKey
   * 세금계산서 문서 번호
   * @param documentKeyType
   * 문서 번호 유형
   *
   * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param memo
   * 메모
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotRequestedStatusException 세금계산서가 역발행 대기 상태가 아닌 경우
   * @throws B2bTaxInvoiceNoRecipientDocumentKeyException 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("cancelB2bTaxInvoiceRequestSuspend")
  public suspend fun cancelB2bTaxInvoiceRequest(
    test: Boolean? = null,
    brn: string,
    documentKey: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    memo: string? = null,
  ): B2bTaxInvoice {
    val requestBody = CancelB2bTaxInvoiceRequestBody(
      brn = brn,
      documentKey = documentKey,
      documentKeyType = documentKeyType,
      memo = memo,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", "cancel-request")
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<CancelB2bTaxInvoiceRequestError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceNotRequestedStatusError -> throw B2bTaxInvoiceNotRequestedStatusException(httpBodyDecoded)
        is B2bTaxInvoiceNoRecipientDocumentKeyError -> throw B2bTaxInvoiceNoRecipientDocumentKeyException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bTaxInvoice>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("cancelB2bTaxInvoiceRequest")
  public suspend fun cancelB2bTaxInvoiceRequestFuture(
    test: Boolean? = null,
    brn: string,
    documentKey: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    memo: string? = null,
  ): CompletableFuture<B2bTaxInvoice> = GlobalScope.future { cancelB2bTaxInvoiceRequest(test, brn, documentKey, documentKeyType, memo) }


  /**
   * 세금계산서 역발행 취소
   *
   * 공급자가 발행 완료한 세금계산서를 국세청 전송 전 취소합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param brn
   * 사업자등록번호
   * @param documentKey
   * 세금계산서 문서 번호
   * @param documentKeyType
   * 문서 번호 유형
   *
   * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param memo
   * 메모
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotIssuedStatusException 세금계산서가 발행된(ISSUED) 상태가 아닌 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("cancelB2bTaxInvoiceIssuanceSuspend")
  public suspend fun cancelB2bTaxInvoiceIssuance(
    test: Boolean? = null,
    brn: string,
    documentKey: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    memo: string? = null,
  ): B2bTaxInvoice {
    val requestBody = CancelB2bTaxInvoiceIssuanceBody(
      brn = brn,
      documentKey = documentKey,
      documentKeyType = documentKeyType,
      memo = memo,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", "cancel-issuance")
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<CancelB2bTaxInvoiceIssuanceError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotIssuedStatusError -> throw B2bTaxInvoiceNotIssuedStatusException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bTaxInvoice>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("cancelB2bTaxInvoiceIssuance")
  public suspend fun cancelB2bTaxInvoiceIssuanceFuture(
    test: Boolean? = null,
    brn: string,
    documentKey: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    memo: string? = null,
  ): CompletableFuture<B2bTaxInvoice> = GlobalScope.future { cancelB2bTaxInvoiceIssuance(test, brn, documentKey, documentKeyType, memo) }


  /**
   * 세금계산서 역발행 요청 거부
   *
   * 공급자가 공급받는자로부터 요청받은 세금계산서 역발행 건을 거부합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param brn
   * 사업자등록번호
   * @param documentKey
   * 세금계산서 문서 번호
   * @param documentKeyType
   * 문서 번호 유형
   *
   * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param memo
   * 메모
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotRequestedStatusException 세금계산서가 역발행 대기 상태가 아닌 경우
   * @throws B2bTaxInvoiceNoSupplierDocumentKeyException 세금계산서에 공급자 문서 번호가 기입되지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("refuseB2bTaxInvoiceRequestSuspend")
  public suspend fun refuseB2bTaxInvoiceRequest(
    test: Boolean? = null,
    brn: string,
    documentKey: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    memo: string? = null,
  ): B2bTaxInvoice {
    val requestBody = RefuseB2bTaxInvoiceRequestBody(
      brn = brn,
      documentKey = documentKey,
      documentKeyType = documentKeyType,
      memo = memo,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", "refuse-request")
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<RefuseB2bTaxInvoiceRequestError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceNotRequestedStatusError -> throw B2bTaxInvoiceNotRequestedStatusException(httpBodyDecoded)
        is B2bTaxInvoiceNoSupplierDocumentKeyError -> throw B2bTaxInvoiceNoSupplierDocumentKeyException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bTaxInvoice>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("refuseB2bTaxInvoiceRequest")
  public suspend fun refuseB2bTaxInvoiceRequestFuture(
    test: Boolean? = null,
    brn: string,
    documentKey: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    memo: string? = null,
  ): CompletableFuture<B2bTaxInvoice> = GlobalScope.future { refuseB2bTaxInvoiceRequest(test, brn, documentKey, documentKeyType, memo) }


  /**
   * 세금 계산서 다건조회
   *
   * 조회 기간 내 등록된 세금 계산서를 다건 조회합니다.
   *
   * @param brn
   * 사업자등록번호
   * @param pageNumber
   * 페이지 번호
   *
   * 0부터 시작하는 페이지 번호. 기본 값은 0.
   * @param pageSize
   * 페이지 크기
   *
   * 각 페이지 당 포함할 객체 수. 기본 값은 500이며 최대 1000까지 요청가능합니다.
   * @param from
   * 조회 시작일
   * @param until
   * 조회 종료일
   * @param dateType
   * 조회 기간 기준
   * @param documentKeyType
   * 문서 번호 유형
   *
   * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bTaxInvoicesSuspend")
  public suspend fun getB2bTaxInvoices(
    brn: string,
    pageNumber: Int? = null,
    pageSize: Int? = null,
    `from`: string,
    until: string,
    dateType: B2bSearchDateType,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    test: Boolean? = null,
  ): GetB2bTaxInvoicesResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices")
        parameters.append("brn", brn)
        if (pageNumber != null) parameters.append("pageNumber", pageNumber)
        if (pageSize != null) parameters.append("pageSize", pageSize)
        parameters.append("from", from)
        parameters.append("until", until)
        parameters.append("dateType", dateType)
        if (documentKeyType != null) parameters.append("documentKeyType", documentKeyType)
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<GetB2bTaxInvoicesError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bTaxInvoicesResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bTaxInvoices")
  public suspend fun getB2bTaxInvoicesFuture(
    brn: string,
    pageNumber: Int? = null,
    pageSize: Int? = null,
    `from`: string,
    until: string,
    dateType: B2bSearchDateType,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bTaxInvoicesResponse> = GlobalScope.future { getB2bTaxInvoices(brn, pageNumber, pageSize, from, until, dateType, documentKeyType, test) }


  /**
   * 세금 계산서 팝업 URL 조회
   *
   * 등록된 세금 계산서 팝업 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.
   *
   * @param documentKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param documentKeyType
   * 문서 번호 유형
   *
   * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param includeMenu
   * 메뉴 포함 여부
   *
   * 팝업 URL에 메뉴 레이아웃을 포함 여부를 결정합니다. 기본 값은 true입니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bTaxInvoicePopupUrlSuspend")
  public suspend fun getB2bTaxInvoicePopupUrl(
    documentKey: string,
    brn: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    includeMenu: Boolean? = null,
    test: Boolean? = null,
  ): GetB2bTaxInvoicePopupUrlResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", documentKey, "popup-url")
        parameters.append("brn", brn)
        if (documentKeyType != null) parameters.append("documentKeyType", documentKeyType)
        if (includeMenu != null) parameters.append("includeMenu", includeMenu)
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<GetB2bTaxInvoicePopupUrlError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bTaxInvoicePopupUrlResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bTaxInvoicePopupUrl")
  public suspend fun getB2bTaxInvoicePopupUrlFuture(
    documentKey: string,
    brn: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    includeMenu: Boolean? = null,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bTaxInvoicePopupUrlResponse> = GlobalScope.future { getB2bTaxInvoicePopupUrl(documentKey, brn, documentKeyType, includeMenu, test) }


  /**
   * 세금 계산서 프린트 URL 조회
   *
   * 등록된 세금 계산서 프린트 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.
   *
   * @param documentKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param documentKeyType
   * 문서 번호 유형
   *
   * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bTaxInvoicePrintUrlSuspend")
  public suspend fun getB2bTaxInvoicePrintUrl(
    documentKey: string,
    brn: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    test: Boolean? = null,
  ): GetB2bTaxInvoicePrintUrlResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", documentKey, "print-url")
        parameters.append("brn", brn)
        if (documentKeyType != null) parameters.append("documentKeyType", documentKeyType)
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<GetB2bTaxInvoicePrintUrlError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bTaxInvoicePrintUrlResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bTaxInvoicePrintUrl")
  public suspend fun getB2bTaxInvoicePrintUrlFuture(
    documentKey: string,
    brn: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bTaxInvoicePrintUrlResponse> = GlobalScope.future { getB2bTaxInvoicePrintUrl(documentKey, brn, documentKeyType, test) }


  /**
   * 세금 계산서 PDF 다운로드 URL 조회
   *
   * 등록된 세금 계산서 PDF 다운로드 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.
   *
   * @param documentKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param documentKeyType
   * 문서 번호 유형
   *
   * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bTaxInvoicePdfDownloadUrlSuspend")
  public suspend fun getB2bTaxInvoicePdfDownloadUrl(
    documentKey: string,
    brn: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    test: Boolean? = null,
  ): GetB2bTaxInvoicePdfDownloadUrlResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", documentKey, "pdf-download-url")
        parameters.append("brn", brn)
        if (documentKeyType != null) parameters.append("documentKeyType", documentKeyType)
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<GetB2bTaxInvoicePdfDownloadUrlError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bTaxInvoicePdfDownloadUrlResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bTaxInvoicePdfDownloadUrl")
  public suspend fun getB2bTaxInvoicePdfDownloadUrlFuture(
    documentKey: string,
    brn: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bTaxInvoicePdfDownloadUrlResponse> = GlobalScope.future { getB2bTaxInvoicePdfDownloadUrl(documentKey, brn, documentKeyType, test) }


  /**
   * 세금계산서 임시 저장
   *
   * 세금계산서 임시 저장을 요청합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param taxInvoice
   * 세금계산서 생성 요청 정보
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bRecipientNotFoundException 공급받는자가 존재하지 않은 경우
   * @throws B2bSupplierNotFoundException 공급자가 존재하지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("requestB2bTaxInvoiceRegisterSuspend")
  public suspend fun requestB2bTaxInvoiceRegister(
    test: Boolean? = null,
    taxInvoice: B2bTaxInvoiceInput,
  ): B2bTaxInvoice {
    val requestBody = RequestB2bTaxInvoiceRegisterBody(
      taxInvoice = taxInvoice,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", "register")
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<RequestB2bTaxInvoiceRegisterError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bRecipientNotFoundError -> throw B2bRecipientNotFoundException(httpBodyDecoded)
        is B2bSupplierNotFoundError -> throw B2bSupplierNotFoundException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bTaxInvoice>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("requestB2bTaxInvoiceRegister")
  public suspend fun requestB2bTaxInvoiceRegisterFuture(
    test: Boolean? = null,
    taxInvoice: B2bTaxInvoiceInput,
  ): CompletableFuture<B2bTaxInvoice> = GlobalScope.future { requestB2bTaxInvoiceRegister(test, taxInvoice) }


  /**
   * 세금계산서 역발행 요청
   *
   * 임시저장(REGISTERED) 상태의 역발행 세금계산서를 공급자에게 발행 요청합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param brn
   * 사업자등록번호
   * @param documentKey
   * 세금계산서 문서 번호
   * @param documentKeyType
   * 문서 번호 유형
   *
   * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param memo
   * 메모
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotRegisteredStatusException 세금계산서가 임시저장 상태가 아닌 경우
   * @throws B2bTaxInvoiceNoRecipientDocumentKeyException 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("requestB2bTaxInvoiceSuspend")
  public suspend fun requestB2bTaxInvoice(
    test: Boolean? = null,
    brn: string,
    documentKey: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    memo: string? = null,
  ): B2bTaxInvoice {
    val requestBody = RequestB2bTaxInvoiceRequestBody(
      brn = brn,
      documentKey = documentKey,
      documentKeyType = documentKeyType,
      memo = memo,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", "request")
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<requestB2bTaxInvoiceError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceNotRegisteredStatusError -> throw B2bTaxInvoiceNotRegisteredStatusException(httpBodyDecoded)
        is B2bTaxInvoiceNoRecipientDocumentKeyError -> throw B2bTaxInvoiceNoRecipientDocumentKeyException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bTaxInvoice>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("requestB2bTaxInvoice")
  public suspend fun requestB2bTaxInvoiceFuture(
    test: Boolean? = null,
    brn: string,
    documentKey: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    memo: string? = null,
  ): CompletableFuture<B2bTaxInvoice> = GlobalScope.future { requestB2bTaxInvoice(test, brn, documentKey, documentKeyType, memo) }


  /**
   * 세금계산서 파일 업로드 링크 생성
   *
   * 세금계산서의 첨부파일를 업로드할 링크를 생성합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param fileName
   * 파일 이름
   *
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("createB2bTaxInvoiceFileUploadLinkSuspend")
  public suspend fun createB2bTaxInvoiceFileUploadLink(
    test: Boolean? = null,
    fileName: string,
  ): CreateB2bTaxInvoiceFileUploadLinkResponse {
    val requestBody = CreateB2bTaxInvoiceFileUploadLinkBody(
      fileName = fileName,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", "file-upload-link")
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<CreateB2bTaxInvoiceFileUploadLinkCreateError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreateB2bTaxInvoiceFileUploadLinkResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createB2bTaxInvoiceFileUploadLink")
  public suspend fun createB2bTaxInvoiceFileUploadLinkFuture(
    test: Boolean? = null,
    fileName: string,
  ): CompletableFuture<CreateB2bTaxInvoiceFileUploadLinkResponse> = GlobalScope.future { createB2bTaxInvoiceFileUploadLink(test, fileName) }


  /**
   * 세금계산서 파일 첨부
   *
   * 세금계산서에 파일을 첨부합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param brn
   * 사업자등록번호
   *
   * `-` 없이 숫자 10자리로 구성됩니다.
   * @param documentKey
   * 세금계산서 문서 번호
   * @param documentKeyType
   * 문서 번호 유형
   *
   * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param fileId
   * 파일 아이디
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bFileNotFoundException 업로드한 파일을 찾을 수 없는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotRegisteredStatusException 세금계산서가 임시저장 상태가 아닌 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("attachB2bTaxInvoiceFileSuspend")
  public suspend fun attachB2bTaxInvoiceFile(
    test: Boolean? = null,
    brn: string,
    documentKey: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    fileId: string,
  ) {
    val requestBody = AttachB2bTaxInvoiceFileBody(
      brn = brn,
      documentKey = documentKey,
      documentKeyType = documentKeyType,
      fileId = fileId,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", "attach-file")
        if (test != null) parameters.append("test", test)
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<AttachB2bTaxInvoiceFileError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bFileNotFoundError -> throw B2bFileNotFoundException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceNotRegisteredStatusError -> throw B2bTaxInvoiceNotRegisteredStatusException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
  }

  /** @suppress */
  @JvmName("attachB2bTaxInvoiceFile")
  public suspend fun attachB2bTaxInvoiceFileFuture(
    test: Boolean? = null,
    brn: string,
    documentKey: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    fileId: string,
  ) = GlobalScope.future { attachB2bTaxInvoiceFile(test, brn, documentKey, documentKeyType, fileId) }


  /**
   * 세금계산서 첨부파일 목록 조회
   *
   * 세금계산서에 첨부된 파일 목록을 조회합니다.
   *
   * @param documentKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param documentKeyType
   * 문서 번호 유형
   *
   * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bTaxInvoiceAttachmentsSuspend")
  public suspend fun getB2bTaxInvoiceAttachments(
    documentKey: string,
    brn: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    test: Boolean? = null,
  ): GetB2bTaxInvoiceAttachmentsResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", documentKey, "attachments")
        parameters.append("brn", brn)
        if (documentKeyType != null) parameters.append("documentKeyType", documentKeyType)
        if (test != null) parameters.append("test", test)
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
        json.decodeFromString<GetB2bTaxInvoiceAttachmentsError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bTaxInvoiceAttachmentsResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bTaxInvoiceAttachments")
  public suspend fun getB2bTaxInvoiceAttachmentsFuture(
    documentKey: string,
    brn: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bTaxInvoiceAttachmentsResponse> = GlobalScope.future { getB2bTaxInvoiceAttachments(documentKey, brn, documentKeyType, test) }


  /**
   * 세금계산서 첨부파일 삭제
   *
   * 세금계산서 첨부파일을 삭제합니다.
   *
   * @param documentKey
   * 세금계산서 문서 번호
   * @param attachmentId
   * 첨부파일 아이디
   * @param brn
   * 사업자등록번호
   * @param documentKeyType
   * 문서 번호 유형
   *
   * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceAttachmentNotFoundException 세금계산서의 첨부파일을 찾을 수 없는 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotRegisteredStatusException 세금계산서가 임시저장 상태가 아닌 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("deleteB2bTaxInvoiceAttachmentSuspend")
  public suspend fun deleteB2bTaxInvoiceAttachment(
    documentKey: string,
    attachmentId: string,
    brn: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    test: Boolean? = null,
  ) {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b-preview", "tax-invoices", documentKey, "attachments", attachmentId)
        parameters.append("brn", brn)
        if (documentKeyType != null) parameters.append("documentKeyType", documentKeyType)
        if (test != null) parameters.append("test", test)
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<DeleteB2bTaxInvoiceAttachmentError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceAttachmentNotFoundError -> throw B2bTaxInvoiceAttachmentNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceNotRegisteredStatusError -> throw B2bTaxInvoiceNotRegisteredStatusException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
  }

  /** @suppress */
  @JvmName("deleteB2bTaxInvoiceAttachment")
  public suspend fun deleteB2bTaxInvoiceAttachmentFuture(
    documentKey: string,
    attachmentId: string,
    brn: string,
    documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
    test: Boolean? = null,
  ) = GlobalScope.future { deleteB2bTaxInvoiceAttachment(documentKey, attachmentId, brn, documentKeyType, test) }

  override fun close() {
    client.close()
  }
}
