package io.portone.sdk.server.platform.partner

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
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.errors.ArchivePlatformPartnerError
import io.portone.sdk.server.errors.ArchivePlatformPartnerException
import io.portone.sdk.server.errors.CreatePlatformPartnerError
import io.portone.sdk.server.errors.CreatePlatformPartnerException
import io.portone.sdk.server.errors.CreatePlatformPartnersError
import io.portone.sdk.server.errors.CreatePlatformPartnersException
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetPlatformPartnerError
import io.portone.sdk.server.errors.GetPlatformPartnerException
import io.portone.sdk.server.errors.GetPlatformPartnersError
import io.portone.sdk.server.errors.GetPlatformPartnersException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.PlatformAccountVerificationAlreadyUsedError
import io.portone.sdk.server.errors.PlatformAccountVerificationAlreadyUsedException
import io.portone.sdk.server.errors.PlatformAccountVerificationFailedError
import io.portone.sdk.server.errors.PlatformAccountVerificationFailedException
import io.portone.sdk.server.errors.PlatformAccountVerificationNotFoundError
import io.portone.sdk.server.errors.PlatformAccountVerificationNotFoundException
import io.portone.sdk.server.errors.PlatformArchivedPartnerError
import io.portone.sdk.server.errors.PlatformArchivedPartnerException
import io.portone.sdk.server.errors.PlatformCannotArchiveScheduledPartnerError
import io.portone.sdk.server.errors.PlatformCannotArchiveScheduledPartnerException
import io.portone.sdk.server.errors.PlatformCompanyVerificationAlreadyUsedError
import io.portone.sdk.server.errors.PlatformCompanyVerificationAlreadyUsedException
import io.portone.sdk.server.errors.PlatformContractNotFoundError
import io.portone.sdk.server.errors.PlatformContractNotFoundException
import io.portone.sdk.server.errors.PlatformContractsNotFoundError
import io.portone.sdk.server.errors.PlatformContractsNotFoundException
import io.portone.sdk.server.errors.PlatformCurrencyNotSupportedError
import io.portone.sdk.server.errors.PlatformCurrencyNotSupportedException
import io.portone.sdk.server.errors.PlatformInsufficientDataToChangePartnerTypeError
import io.portone.sdk.server.errors.PlatformInsufficientDataToChangePartnerTypeException
import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnerBrnUnchangeableError
import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnerBrnUnchangeableException
import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnerTypeUnchangeableError
import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnerTypeUnchangeableException
import io.portone.sdk.server.errors.PlatformNotEnabledError
import io.portone.sdk.server.errors.PlatformNotEnabledException
import io.portone.sdk.server.errors.PlatformPartnerIdAlreadyExistsError
import io.portone.sdk.server.errors.PlatformPartnerIdAlreadyExistsException
import io.portone.sdk.server.errors.PlatformPartnerIdsAlreadyExistError
import io.portone.sdk.server.errors.PlatformPartnerIdsAlreadyExistException
import io.portone.sdk.server.errors.PlatformPartnerIdsDuplicatedError
import io.portone.sdk.server.errors.PlatformPartnerIdsDuplicatedException
import io.portone.sdk.server.errors.PlatformPartnerNotFoundError
import io.portone.sdk.server.errors.PlatformPartnerNotFoundException
import io.portone.sdk.server.errors.PlatformUserDefinedPropertyNotFoundError
import io.portone.sdk.server.errors.PlatformUserDefinedPropertyNotFoundException
import io.portone.sdk.server.errors.RecoverPlatformPartnerError
import io.portone.sdk.server.errors.RecoverPlatformPartnerException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.errors.UpdatePlatformPartnerError
import io.portone.sdk.server.errors.UpdatePlatformPartnerException
import io.portone.sdk.server.platform.PlatformPartner
import io.portone.sdk.server.platform.PlatformPartnerFilterInput
import io.portone.sdk.server.platform.PlatformProperties
import io.portone.sdk.server.platform.UpdatePlatformPartnerBody
import io.portone.sdk.server.platform.UpdatePlatformPartnerBodyAccount
import io.portone.sdk.server.platform.UpdatePlatformPartnerBodyContact
import io.portone.sdk.server.platform.UpdatePlatformPartnerBodyType
import io.portone.sdk.server.platform.partner.ArchivePlatformPartnerResponse
import io.portone.sdk.server.platform.partner.CreatePlatformPartnerBody
import io.portone.sdk.server.platform.partner.CreatePlatformPartnerBodyAccount
import io.portone.sdk.server.platform.partner.CreatePlatformPartnerBodyContact
import io.portone.sdk.server.platform.partner.CreatePlatformPartnerBodyType
import io.portone.sdk.server.platform.partner.CreatePlatformPartnerResponse
import io.portone.sdk.server.platform.partner.CreatePlatformPartnersBody
import io.portone.sdk.server.platform.partner.CreatePlatformPartnersResponse
import io.portone.sdk.server.platform.partner.GetPlatformPartnersBody
import io.portone.sdk.server.platform.partner.GetPlatformPartnersResponse
import io.portone.sdk.server.platform.partner.RecoverPlatformPartnerResponse
import io.portone.sdk.server.platform.partner.UpdatePlatformPartnerResponse
import java.io.Closeable
import java.util.concurrent.CompletableFuture
import kotlin.Array
import kotlin.String
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json

/**
 * API Secret을 사용해 포트원 API 클라이언트를 생성합니다.
 */
public class PartnerClient(
  private val apiSecret: String,
  private val apiBase: String = "https://api.portone.io",
  private val storeId: String? = null,
): Closeable {
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
   * @throws GetPlatformPartnersException
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
        parameters.append("requestBody", json.encodeToString(requestBody))
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
        json.decodeFromString<GetPlatformPartnersError.Recognized>(httpBody)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformPartners")
  public fun getPlatformPartnersFuture(
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
   * @throws CreatePlatformPartnerException
   */
  @JvmName("createPlatformPartnerSuspend")
  public suspend fun createPlatformPartner(
    id: String? = null,
    name: String,
    contact: CreatePlatformPartnerBodyContact,
    account: CreatePlatformPartnerBodyAccount,
    defaultContractId: String,
    memo: String? = null,
    tags: List<String>,
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
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("platform", "partners")
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
        json.decodeFromString<CreatePlatformPartnerError.Recognized>(httpBody)
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
        is PlatformCompanyVerificationAlreadyUsedError -> throw PlatformCompanyVerificationAlreadyUsedException(httpBodyDecoded)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformPartner")
  public fun createPlatformPartnerFuture(
    id: String? = null,
    name: String,
    contact: CreatePlatformPartnerBodyContact,
    account: CreatePlatformPartnerBodyAccount,
    defaultContractId: String,
    memo: String? = null,
    tags: List<String>,
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
   * @throws GetPlatformPartnerException
   */
  @JvmName("getPlatformPartnerSuspend")
  public suspend fun getPlatformPartner(
    id: String,
  ): PlatformPartner {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "partners", id.toString())
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
        json.decodeFromString<GetPlatformPartnerError.Recognized>(httpBody)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformPartner")
  public fun getPlatformPartnerFuture(
    id: String,
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
   * @throws UpdatePlatformPartnerException
   */
  @JvmName("updatePlatformPartnerSuspend")
  public suspend fun updatePlatformPartner(
    id: String,
    name: String? = null,
    contact: UpdatePlatformPartnerBodyContact? = null,
    account: UpdatePlatformPartnerBodyAccount? = null,
    defaultContractId: String? = null,
    memo: String? = null,
    tags: List<String>? = null,
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
    val httpResponse = client.patch(apiBase) {
      url {
        appendPathSegments("platform", "partners", id.toString())
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
        json.decodeFromString<UpdatePlatformPartnerError.Recognized>(httpBody)
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
        is PlatformCompanyVerificationAlreadyUsedError -> throw PlatformCompanyVerificationAlreadyUsedException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformInsufficientDataToChangePartnerTypeError -> throw PlatformInsufficientDataToChangePartnerTypeException(httpBodyDecoded)
        is PlatformMemberCompanyConnectedPartnerBrnUnchangeableError -> throw PlatformMemberCompanyConnectedPartnerBrnUnchangeableException(httpBodyDecoded)
        is PlatformMemberCompanyConnectedPartnerTypeUnchangeableError -> throw PlatformMemberCompanyConnectedPartnerTypeUnchangeableException(httpBodyDecoded)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updatePlatformPartner")
  public fun updatePlatformPartnerFuture(
    id: String,
    name: String? = null,
    contact: UpdatePlatformPartnerBodyContact? = null,
    account: UpdatePlatformPartnerBodyAccount? = null,
    defaultContractId: String? = null,
    memo: String? = null,
    tags: List<String>? = null,
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
   * @throws CreatePlatformPartnersException
   */
  @JvmName("createPlatformPartnersSuspend")
  public suspend fun createPlatformPartners(
    partners: List<CreatePlatformPartnerBody>,
  ): CreatePlatformPartnersResponse {
    val requestBody = CreatePlatformPartnersBody(
      partners = partners,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("platform", "partners", "batch")
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
        json.decodeFromString<CreatePlatformPartnersError.Recognized>(httpBody)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformPartners")
  public fun createPlatformPartnersFuture(
    partners: List<CreatePlatformPartnerBody>,
  ): CompletableFuture<CreatePlatformPartnersResponse> = GlobalScope.future { createPlatformPartners(partners) }


  /**
   * 파트너 복원
   *
   * 주어진 아이디에 대응되는 파트너를 보관합니다.
   *
   * @param id
   * 파트너 아이디
   *
   * @throws ArchivePlatformPartnerException
   */
  @JvmName("archivePlatformPartnerSuspend")
  public suspend fun archivePlatformPartner(
    id: String,
  ): ArchivePlatformPartnerResponse {
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("platform", "partners", id.toString(), "archive")
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
        json.decodeFromString<ArchivePlatformPartnerError.Recognized>(httpBody)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("archivePlatformPartner")
  public fun archivePlatformPartnerFuture(
    id: String,
  ): CompletableFuture<ArchivePlatformPartnerResponse> = GlobalScope.future { archivePlatformPartner(id) }


  /**
   * 파트너 복원
   *
   * 주어진 아이디에 대응되는 파트너를 복원합니다.
   *
   * @param id
   * 파트너 아이디
   *
   * @throws RecoverPlatformPartnerException
   */
  @JvmName("recoverPlatformPartnerSuspend")
  public suspend fun recoverPlatformPartner(
    id: String,
  ): RecoverPlatformPartnerResponse {
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("platform", "partners", id.toString(), "recover")
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
        json.decodeFromString<RecoverPlatformPartnerError.Recognized>(httpBody)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("recoverPlatformPartner")
  public fun recoverPlatformPartnerFuture(
    id: String,
  ): CompletableFuture<RecoverPlatformPartnerResponse> = GlobalScope.future { recoverPlatformPartner(id) }

  override fun close() {
    client.close()
  }
}
