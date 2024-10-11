package io.portone.sdk.server.partner

import io.ktor.client.HttpClient
import io.portone.sdk.server.ArchivePlatformPartnerResponse
import io.portone.sdk.server.CreatePlatformPartnerResponse
import io.portone.sdk.server.CreatePlatformPartnersResponse
import io.portone.sdk.server.GetPlatformPartnersResponse
import io.portone.sdk.server.PlatformPartner
import io.portone.sdk.server.RecoverPlatformPartnerResponse
import io.portone.sdk.server.UpdatePlatformPartnerResponse
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.PlatformPartner
import io.portone.sdk.server.platform.PlatformPartnerFilterInput
import io.portone.sdk.server.platform.PlatformProperties
import io.portone.sdk.server.platform.UpdatePlatformPartnerBodyAccount
import io.portone.sdk.server.platform.UpdatePlatformPartnerBodyContact
import io.portone.sdk.server.platform.UpdatePlatformPartnerBodyType
import io.portone.sdk.server.platform.partner.ArchivePlatformPartnerResponse
import io.portone.sdk.server.platform.partner.CreatePlatformPartnerBody
import io.portone.sdk.server.platform.partner.CreatePlatformPartnerBodyAccount
import io.portone.sdk.server.platform.partner.CreatePlatformPartnerBodyContact
import io.portone.sdk.server.platform.partner.CreatePlatformPartnerBodyType
import io.portone.sdk.server.platform.partner.CreatePlatformPartnerResponse
import io.portone.sdk.server.platform.partner.CreatePlatformPartnersResponse
import io.portone.sdk.server.platform.partner.GetPlatformPartnersResponse
import io.portone.sdk.server.platform.partner.RecoverPlatformPartnerResponse
import io.portone.sdk.server.platform.partner.UpdatePlatformPartnerResponse
import java.io.Closeable
import kotlin.Array
import kotlin.String
import kotlinx.serialization.json.Json

public class PartnerClient(
  private val apiSecret: String,
  private val storeId: String,
  private val apiBase: String,
) : Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 파트너 다건 조회
   *
   * 여러 파트너를 조회합니다.
   *
   * @param page
   * 요청할 페이지 정보
   * @param filter
   * 조회할 파트너 조건 필터
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformPartnersSuspend")
  public suspend fun getPlatformPartners(
    page: PageInput? = null,
    filter: PlatformPartnerFilterInput? = null,
  ): GetPlatformPartnersResponse {
    val requestBody = GetPlatformPartnersBody(
      page = page,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "partners")
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
        json.decodeFromString<GetPlatformPartnersError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetPlatformPartnersResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformPartners")
  public suspend fun getPlatformPartnersFuture(
    page: PageInput? = null,
    filter: PlatformPartnerFilterInput? = null,
  ): CompletableFuture<GetPlatformPartnersResponse> = GlobalScope.future { getPlatformPartners(page, filter) }


  /**
   * 파트너 생성
   *
   * 새로운 파트너를 생성합니다.
   *
   * @param id
   * 파트너에 부여할 고유 아이디
   *
   * 고객사 서버에 등록된 파트너 지칭 아이디와 동일하게 설정하는 것을 권장합니다. 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
   * @param name
   * 파트너 법인명 혹은 이름
   * @param contact
   * 파트너 담당자 연락 정보
   * @param account
   * 정산 계좌
   *
   * 파트너의 사업자등록번호가 존재하는 경우 명시합니다. 별도로 검증하지는 않으며, 번호와 기호 모두 입력 가능합니다.
   * @param defaultContractId
   * 기본 계약 아이디
   *
   * 이미 존재하는 계약 아이디를 등록해야 합니다.
   * @param memo
   * 파트너에 대한 메모
   *
   * 총 256자까지 입력할 수 있습니다.
   * @param tags
   * 파트너에 부여할 태그 리스트
   *
   * 최대 10개까지 입력할 수 있습니다.
   * @param type
   * 파트너 유형별 추가 정보
   *
   * 사업자/원천징수 대상자 중 추가할 파트너의 유형에 따른 정보를 입력해야 합니다.
   * @param userDefinedProperties
   * 사용자 정의 속성
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformAccountVerificationAlreadyUsedException 파트너 계좌 검증 아이디를 이미 사용한 경우
   * @throws PlatformAccountVerificationFailedException 파트너 계좌 인증이 실패한 경우
   * @throws PlatformAccountVerificationNotFoundException 파트너 계좌 검증 아이디를 찾을 수 없는 경우
   * @throws PlatformContractNotFoundException PlatformContractNotFoundError
   * @throws PlatformCurrencyNotSupportedException 지원 되지 않는 통화를 선택한 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformPartnerIdAlreadyExistsException PlatformPartnerIdAlreadyExistsError
   * @throws PlatformUserDefinedPropertyNotFoundException 사용자 정의 속성이 존재 하지 않는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("createPlatformPartnerSuspend")
  public suspend fun createPlatformPartner(
    id: string? = null,
    name: string,
    contact: CreatePlatformPartnerBodyContact,
    account: CreatePlatformPartnerBodyAccount,
    defaultContractId: string,
    memo: string? = null,
    tags: Array<String>,
    type: CreatePlatformPartnerBodyType,
    userDefinedProperties: PlatformProperties? = null,
  ): CreatePlatformPartnerResponse {
    val requestBody = CreatePlatformPartnerBody(
      id = id,
      name = name,
      contact = contact,
      account = account,
      defaultContractId = defaultContractId,
      memo = memo,
      tags = tags,
      type = type,
      userDefinedProperties = userDefinedProperties,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "partners")
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
        json.decodeFromString<CreatePlatformPartnerError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAccountVerificationAlreadyUsedError -> throw PlatformAccountVerificationAlreadyUsedException(httpBodyDecoded)
        is PlatformAccountVerificationFailedError -> throw PlatformAccountVerificationFailedException(httpBodyDecoded)
        is PlatformAccountVerificationNotFoundError -> throw PlatformAccountVerificationNotFoundException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformCurrencyNotSupportedError -> throw PlatformCurrencyNotSupportedException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformPartnerIdAlreadyExistsError -> throw PlatformPartnerIdAlreadyExistsException(httpBodyDecoded)
        is PlatformUserDefinedPropertyNotFoundError -> throw PlatformUserDefinedPropertyNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreatePlatformPartnerResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformPartner")
  public suspend fun createPlatformPartnerFuture(
    id: string? = null,
    name: string,
    contact: CreatePlatformPartnerBodyContact,
    account: CreatePlatformPartnerBodyAccount,
    defaultContractId: string,
    memo: string? = null,
    tags: Array<String>,
    type: CreatePlatformPartnerBodyType,
    userDefinedProperties: PlatformProperties? = null,
  ): CompletableFuture<CreatePlatformPartnerResponse> = GlobalScope.future { createPlatformPartner(id, name, contact, account, defaultContractId, memo, tags, type, userDefinedProperties) }


  /**
   * 파트너 조회
   *
   * 파트너 객체를 조회합니다.
   *
   * @param id
   * 조회하고 싶은 파트너 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformPartnerNotFoundException PlatformPartnerNotFoundError
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformPartnerSuspend")
  public suspend fun getPlatformPartner(
    id: string,
  ): PlatformPartner {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "partners", id)
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
        json.decodeFromString<GetPlatformPartnerError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformPartnerNotFoundError -> throw PlatformPartnerNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PlatformPartner>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformPartner")
  public suspend fun getPlatformPartnerFuture(
    id: string,
  ): CompletableFuture<PlatformPartner> = GlobalScope.future { getPlatformPartner(id) }


  /**
   * 파트너 수정
   *
   * 주어진 아이디에 대응되는 파트너 정보를 업데이트합니다.
   *
   * @param id
   * 업데이트할 파트너 아이디
   * @param name
   * 파트너 법인명 혹은 이름
   * @param contact
   * 파트너 담당자 연락 정보
   * @param account
   * 정산 계좌
   * @param defaultContractId
   * 파트너에 설정된 기본 계약 아이디
   * @param memo
   * 파트너에 대한 메모
   * @param tags
   * 파트너의 태그 리스트
   * @param type
   * 파트너 유형별 정보
   * @param userDefinedProperties
   * 사용자 정의 속성
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformAccountVerificationAlreadyUsedException 파트너 계좌 검증 아이디를 이미 사용한 경우
   * @throws PlatformAccountVerificationFailedException 파트너 계좌 인증이 실패한 경우
   * @throws PlatformAccountVerificationNotFoundException 파트너 계좌 검증 아이디를 찾을 수 없는 경우
   * @throws PlatformArchivedPartnerException 보관된 파트너를 업데이트하려고 하는 경우
   * @throws PlatformContractNotFoundException PlatformContractNotFoundError
   * @throws PlatformInsufficientDataToChangePartnerTypeException 파트너 타입 수정에 필요한 데이터가 부족한 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformPartnerNotFoundException PlatformPartnerNotFoundError
   * @throws PlatformUserDefinedPropertyNotFoundException 사용자 정의 속성이 존재 하지 않는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("updatePlatformPartnerSuspend")
  public suspend fun updatePlatformPartner(
    id: string,
    name: string? = null,
    contact: UpdatePlatformPartnerBodyContact? = null,
    account: UpdatePlatformPartnerBodyAccount? = null,
    defaultContractId: string? = null,
    memo: string? = null,
    tags: Array<String>? = null,
    type: UpdatePlatformPartnerBodyType? = null,
    userDefinedProperties: PlatformProperties? = null,
  ): UpdatePlatformPartnerResponse {
    val requestBody = UpdatePlatformPartnerBody(
      name = name,
      contact = contact,
      account = account,
      defaultContractId = defaultContractId,
      memo = memo,
      tags = tags,
      type = type,
      userDefinedProperties = userDefinedProperties,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "partners", id)
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
        json.decodeFromString<UpdatePlatformPartnerError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAccountVerificationAlreadyUsedError -> throw PlatformAccountVerificationAlreadyUsedException(httpBodyDecoded)
        is PlatformAccountVerificationFailedError -> throw PlatformAccountVerificationFailedException(httpBodyDecoded)
        is PlatformAccountVerificationNotFoundError -> throw PlatformAccountVerificationNotFoundException(httpBodyDecoded)
        is PlatformArchivedPartnerError -> throw PlatformArchivedPartnerException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformInsufficientDataToChangePartnerTypeError -> throw PlatformInsufficientDataToChangePartnerTypeException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformPartnerNotFoundError -> throw PlatformPartnerNotFoundException(httpBodyDecoded)
        is PlatformUserDefinedPropertyNotFoundError -> throw PlatformUserDefinedPropertyNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdatePlatformPartnerResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updatePlatformPartner")
  public suspend fun updatePlatformPartnerFuture(
    id: string,
    name: string? = null,
    contact: UpdatePlatformPartnerBodyContact? = null,
    account: UpdatePlatformPartnerBodyAccount? = null,
    defaultContractId: string? = null,
    memo: string? = null,
    tags: Array<String>? = null,
    type: UpdatePlatformPartnerBodyType? = null,
    userDefinedProperties: PlatformProperties? = null,
  ): CompletableFuture<UpdatePlatformPartnerResponse> = GlobalScope.future { updatePlatformPartner(id, name, contact, account, defaultContractId, memo, tags, type, userDefinedProperties) }


  /**
   * 파트너 다건 생성
   *
   * 새로운 파트너를 다건 생성합니다.
   *
   * @param partners
   * 생성할 파트너 리스트 정보
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformContractsNotFoundException PlatformContractsNotFoundError
   * @throws PlatformCurrencyNotSupportedException 지원 되지 않는 통화를 선택한 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformPartnerIdsAlreadyExistException PlatformPartnerIdsAlreadyExistError
   * @throws PlatformPartnerIdsDuplicatedException PlatformPartnerIdsDuplicatedError
   * @throws PlatformUserDefinedPropertyNotFoundException 사용자 정의 속성이 존재 하지 않는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("createPlatformPartnersSuspend")
  public suspend fun createPlatformPartners(
    partners: Array<CreatePlatformPartnerBody>,
  ): CreatePlatformPartnersResponse {
    val requestBody = CreatePlatformPartnersBody(
      partners = partners,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "partners", "batch")
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
        json.decodeFromString<CreatePlatformPartnersError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformContractsNotFoundError -> throw PlatformContractsNotFoundException(httpBodyDecoded)
        is PlatformCurrencyNotSupportedError -> throw PlatformCurrencyNotSupportedException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformPartnerIdsAlreadyExistError -> throw PlatformPartnerIdsAlreadyExistException(httpBodyDecoded)
        is PlatformPartnerIdsDuplicatedError -> throw PlatformPartnerIdsDuplicatedException(httpBodyDecoded)
        is PlatformUserDefinedPropertyNotFoundError -> throw PlatformUserDefinedPropertyNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreatePlatformPartnersResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformPartners")
  public suspend fun createPlatformPartnersFuture(
    partners: Array<CreatePlatformPartnerBody>,
  ): CompletableFuture<CreatePlatformPartnersResponse> = GlobalScope.future { createPlatformPartners(partners) }


  /**
   * 파트너 복원
   *
   * 주어진 아이디에 대응되는 파트너를 보관합니다.
   *
   * @param id
   * 파트너 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformCannotArchiveScheduledPartnerException 예약된 업데이트가 있는 파트너를 보관하려고 하는 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformPartnerNotFoundException PlatformPartnerNotFoundError
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("archivePlatformPartnerSuspend")
  public suspend fun archivePlatformPartner(
    id: string,
  ): ArchivePlatformPartnerResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "partners", id, "archive")
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
        json.decodeFromString<ArchivePlatformPartnerError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformCannotArchiveScheduledPartnerError -> throw PlatformCannotArchiveScheduledPartnerException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformPartnerNotFoundError -> throw PlatformPartnerNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ArchivePlatformPartnerResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("archivePlatformPartner")
  public suspend fun archivePlatformPartnerFuture(
    id: string,
  ): CompletableFuture<ArchivePlatformPartnerResponse> = GlobalScope.future { archivePlatformPartner(id) }


  /**
   * 파트너 복원
   *
   * 주어진 아이디에 대응되는 파트너를 복원합니다.
   *
   * @param id
   * 파트너 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformPartnerNotFoundException PlatformPartnerNotFoundError
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("recoverPlatformPartnerSuspend")
  public suspend fun recoverPlatformPartner(
    id: string,
  ): RecoverPlatformPartnerResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "partners", id, "recover")
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
        json.decodeFromString<RecoverPlatformPartnerError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformPartnerNotFoundError -> throw PlatformPartnerNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<RecoverPlatformPartnerResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("recoverPlatformPartner")
  public suspend fun recoverPlatformPartnerFuture(
    id: string,
  ): CompletableFuture<RecoverPlatformPartnerResponse> = GlobalScope.future { recoverPlatformPartner(id) }

  override fun close() {
    client.close()
  }
}
