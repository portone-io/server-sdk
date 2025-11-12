package io.portone.sdk.server.platform.policy

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.plugins.HttpTimeout
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
import io.portone.sdk.server.errors.ArchivePlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.ArchivePlatformAdditionalFeePolicyException
import io.portone.sdk.server.errors.ArchivePlatformContractError
import io.portone.sdk.server.errors.ArchivePlatformContractException
import io.portone.sdk.server.errors.ArchivePlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.ArchivePlatformDiscountSharePolicyException
import io.portone.sdk.server.errors.CreatePlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.CreatePlatformAdditionalFeePolicyException
import io.portone.sdk.server.errors.CreatePlatformContractError
import io.portone.sdk.server.errors.CreatePlatformContractException
import io.portone.sdk.server.errors.CreatePlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.CreatePlatformDiscountSharePolicyException
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePoliciesError
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePoliciesException
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePolicyException
import io.portone.sdk.server.errors.GetPlatformContractError
import io.portone.sdk.server.errors.GetPlatformContractException
import io.portone.sdk.server.errors.GetPlatformContractsError
import io.portone.sdk.server.errors.GetPlatformContractsException
import io.portone.sdk.server.errors.GetPlatformDiscountSharePoliciesError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePoliciesException
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.PlatformAdditionalFeePolicyAlreadyExistsError
import io.portone.sdk.server.errors.PlatformAdditionalFeePolicyAlreadyExistsException
import io.portone.sdk.server.errors.PlatformAdditionalFeePolicyNotFoundError
import io.portone.sdk.server.errors.PlatformAdditionalFeePolicyNotFoundException
import io.portone.sdk.server.errors.PlatformArchivedAdditionalFeePolicyError
import io.portone.sdk.server.errors.PlatformArchivedAdditionalFeePolicyException
import io.portone.sdk.server.errors.PlatformArchivedContractError
import io.portone.sdk.server.errors.PlatformArchivedContractException
import io.portone.sdk.server.errors.PlatformArchivedDiscountSharePolicyError
import io.portone.sdk.server.errors.PlatformArchivedDiscountSharePolicyException
import io.portone.sdk.server.errors.PlatformCannotArchiveScheduledAdditionalFeePolicyError
import io.portone.sdk.server.errors.PlatformCannotArchiveScheduledAdditionalFeePolicyException
import io.portone.sdk.server.errors.PlatformCannotArchiveScheduledContractError
import io.portone.sdk.server.errors.PlatformCannotArchiveScheduledContractException
import io.portone.sdk.server.errors.PlatformCannotArchiveScheduledDiscountSharePolicyError
import io.portone.sdk.server.errors.PlatformCannotArchiveScheduledDiscountSharePolicyException
import io.portone.sdk.server.errors.PlatformContractAlreadyExistsError
import io.portone.sdk.server.errors.PlatformContractAlreadyExistsException
import io.portone.sdk.server.errors.PlatformContractNotFoundError
import io.portone.sdk.server.errors.PlatformContractNotFoundException
import io.portone.sdk.server.errors.PlatformDiscountSharePolicyAlreadyExistsError
import io.portone.sdk.server.errors.PlatformDiscountSharePolicyAlreadyExistsException
import io.portone.sdk.server.errors.PlatformDiscountSharePolicyNotFoundError
import io.portone.sdk.server.errors.PlatformDiscountSharePolicyNotFoundException
import io.portone.sdk.server.errors.PlatformNotEnabledError
import io.portone.sdk.server.errors.PlatformNotEnabledException
import io.portone.sdk.server.errors.RecoverPlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.RecoverPlatformAdditionalFeePolicyException
import io.portone.sdk.server.errors.RecoverPlatformContractError
import io.portone.sdk.server.errors.RecoverPlatformContractException
import io.portone.sdk.server.errors.RecoverPlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.RecoverPlatformDiscountSharePolicyException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.errors.UpdatePlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.UpdatePlatformAdditionalFeePolicyException
import io.portone.sdk.server.errors.UpdatePlatformContractError
import io.portone.sdk.server.errors.UpdatePlatformContractException
import io.portone.sdk.server.errors.UpdatePlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.UpdatePlatformDiscountSharePolicyException
import io.portone.sdk.server.platform.PlatformAdditionalFeePolicy
import io.portone.sdk.server.platform.PlatformContract
import io.portone.sdk.server.platform.PlatformDiscountSharePolicy
import io.portone.sdk.server.platform.PlatformFeeInput
import io.portone.sdk.server.platform.PlatformPayer
import io.portone.sdk.server.platform.PlatformSettlementCycleInput
import io.portone.sdk.server.platform.UpdatePlatformAdditionalFeePolicyBody
import io.portone.sdk.server.platform.UpdatePlatformContractBody
import io.portone.sdk.server.platform.UpdatePlatformDiscountSharePolicyBody
import io.portone.sdk.server.platform.policy.ArchivePlatformAdditionalFeePolicyResponse
import io.portone.sdk.server.platform.policy.ArchivePlatformContractResponse
import io.portone.sdk.server.platform.policy.ArchivePlatformDiscountSharePolicyResponse
import io.portone.sdk.server.platform.policy.CreatePlatformAdditionalFeePolicyBody
import io.portone.sdk.server.platform.policy.CreatePlatformAdditionalFeePolicyResponse
import io.portone.sdk.server.platform.policy.CreatePlatformContractBody
import io.portone.sdk.server.platform.policy.CreatePlatformContractResponse
import io.portone.sdk.server.platform.policy.CreatePlatformDiscountSharePolicyBody
import io.portone.sdk.server.platform.policy.CreatePlatformDiscountSharePolicyResponse
import io.portone.sdk.server.platform.policy.GetPlatformAdditionalFeePoliciesBody
import io.portone.sdk.server.platform.policy.GetPlatformAdditionalFeePoliciesResponse
import io.portone.sdk.server.platform.policy.GetPlatformContractsBody
import io.portone.sdk.server.platform.policy.GetPlatformContractsResponse
import io.portone.sdk.server.platform.policy.GetPlatformDiscountSharePoliciesBody
import io.portone.sdk.server.platform.policy.GetPlatformDiscountSharePoliciesResponse
import io.portone.sdk.server.platform.policy.PlatformAdditionalFeePolicyFilterInput
import io.portone.sdk.server.platform.policy.PlatformContractFilterInput
import io.portone.sdk.server.platform.policy.PlatformDiscountSharePolicyFilterInput
import io.portone.sdk.server.platform.policy.RecoverPlatformAdditionalFeePolicyResponse
import io.portone.sdk.server.platform.policy.RecoverPlatformContractResponse
import io.portone.sdk.server.platform.policy.RecoverPlatformDiscountSharePolicyResponse
import io.portone.sdk.server.platform.policy.UpdatePlatformAdditionalFeePolicyResponse
import io.portone.sdk.server.platform.policy.UpdatePlatformContractResponse
import io.portone.sdk.server.platform.policy.UpdatePlatformDiscountSharePolicyResponse
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
public class PolicyClient(
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
   * 추가 수수료 정책 보관
   *
   * 주어진 아이디에 대응되는 추가 수수료 정책을 보관합니다.
   *
   * @param id
   * 추가 수수료 정책 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws ArchivePlatformAdditionalFeePolicyException
   */
  @JvmName("archivePlatformAdditionalFeePolicySuspend")
  public suspend fun archivePlatformAdditionalFeePolicy(
    id: String,
    test: Boolean? = null,
  ): ArchivePlatformAdditionalFeePolicyResponse {
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "additional-fee-policies", id.toString(), "archive")
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
        json.decodeFromString<ArchivePlatformAdditionalFeePolicyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAdditionalFeePolicyNotFoundError -> throw PlatformAdditionalFeePolicyNotFoundException(httpBodyDecoded)
        is PlatformCannotArchiveScheduledAdditionalFeePolicyError -> throw PlatformCannotArchiveScheduledAdditionalFeePolicyException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ArchivePlatformAdditionalFeePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("archivePlatformAdditionalFeePolicy")
  public fun archivePlatformAdditionalFeePolicyFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<ArchivePlatformAdditionalFeePolicyResponse> = GlobalScope.future { archivePlatformAdditionalFeePolicy(id, test) }


  /**
   * 추가 수수료 정책 복원
   *
   * 주어진 아이디에 대응되는 추가 수수료 정책을 복원합니다.
   *
   * @param id
   * 추가 수수료 정책 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws RecoverPlatformAdditionalFeePolicyException
   */
  @JvmName("recoverPlatformAdditionalFeePolicySuspend")
  public suspend fun recoverPlatformAdditionalFeePolicy(
    id: String,
    test: Boolean? = null,
  ): RecoverPlatformAdditionalFeePolicyResponse {
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "additional-fee-policies", id.toString(), "recover")
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
        json.decodeFromString<RecoverPlatformAdditionalFeePolicyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAdditionalFeePolicyNotFoundError -> throw PlatformAdditionalFeePolicyNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<RecoverPlatformAdditionalFeePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("recoverPlatformAdditionalFeePolicy")
  public fun recoverPlatformAdditionalFeePolicyFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<RecoverPlatformAdditionalFeePolicyResponse> = GlobalScope.future { recoverPlatformAdditionalFeePolicy(id, test) }


  /**
   * 추가 수수료 정책 조회
   *
   * 주어진 아이디에 대응되는 추가 수수료 정책을 조회합니다.
   *
   * @param id
   * 조회할 추가 수수료 정책 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws GetPlatformAdditionalFeePolicyException
   */
  @JvmName("getPlatformAdditionalFeePolicySuspend")
  public suspend fun getPlatformAdditionalFeePolicy(
    id: String,
    test: Boolean? = null,
  ): PlatformAdditionalFeePolicy {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("platform", "additional-fee-policies", id.toString())
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
        json.decodeFromString<GetPlatformAdditionalFeePolicyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAdditionalFeePolicyNotFoundError -> throw PlatformAdditionalFeePolicyNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PlatformAdditionalFeePolicy>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformAdditionalFeePolicy")
  public fun getPlatformAdditionalFeePolicyFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<PlatformAdditionalFeePolicy> = GlobalScope.future { getPlatformAdditionalFeePolicy(id, test) }


  /**
   * 추가 수수료 정책 수정
   *
   * 주어진 아이디에 대응되는 추가 수수료 정책을 업데이트합니다.
   *
   * @param id
   * 업데이트할 추가 수수료 정책 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param fee
   * 책정 수수료
   * @param name
   * 추가 수수료 정책 이름
   * @param memo
   * 해당 추가 수수료 정책에 대한 메모
   * @param vatPayer
   * 부가세를 부담할 주체
   *
   * @throws UpdatePlatformAdditionalFeePolicyException
   */
  @JvmName("updatePlatformAdditionalFeePolicySuspend")
  public suspend fun updatePlatformAdditionalFeePolicy(
    id: String,
    test: Boolean? = null,
    fee: PlatformFeeInput? = null,
    name: String? = null,
    memo: String? = null,
    vatPayer: PlatformPayer? = null,
  ): UpdatePlatformAdditionalFeePolicyResponse {
    val requestBody = UpdatePlatformAdditionalFeePolicyBody(
      fee = fee,
      name = name,
      memo = memo,
      vatPayer = vatPayer,
    )
    val httpResponse = client.patch(apiBase) {
      url {
        this.appendPathSegments("platform", "additional-fee-policies", id.toString())
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
        json.decodeFromString<UpdatePlatformAdditionalFeePolicyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAdditionalFeePolicyNotFoundError -> throw PlatformAdditionalFeePolicyNotFoundException(httpBodyDecoded)
        is PlatformArchivedAdditionalFeePolicyError -> throw PlatformArchivedAdditionalFeePolicyException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdatePlatformAdditionalFeePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updatePlatformAdditionalFeePolicy")
  public fun updatePlatformAdditionalFeePolicyFuture(
    id: String,
    test: Boolean? = null,
    fee: PlatformFeeInput? = null,
    name: String? = null,
    memo: String? = null,
    vatPayer: PlatformPayer? = null,
  ): CompletableFuture<UpdatePlatformAdditionalFeePolicyResponse> = GlobalScope.future { updatePlatformAdditionalFeePolicy(id, test, fee, name, memo, vatPayer) }


  /**
   * 추가 수수료 정책 다건 조회
   *
   * 여러 추가 수수료 정책을 조회합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param page
   * 요청할 페이지 정보
   * @param filter
   * 조회할 추가 수수료 정책 조건 필터
   *
   * @throws GetPlatformAdditionalFeePoliciesException
   */
  @JvmName("getPlatformAdditionalFeePoliciesSuspend")
  public suspend fun getPlatformAdditionalFeePolicies(
    test: Boolean? = null,
    page: PageInput? = null,
    filter: PlatformAdditionalFeePolicyFilterInput? = null,
  ): GetPlatformAdditionalFeePoliciesResponse {
    val requestBody = GetPlatformAdditionalFeePoliciesBody(
      page = page,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("platform", "additional-fee-policies")
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
        json.decodeFromString<GetPlatformAdditionalFeePoliciesError.Recognized>(httpBody)
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
      json.decodeFromString<GetPlatformAdditionalFeePoliciesResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformAdditionalFeePolicies")
  public fun getPlatformAdditionalFeePoliciesFuture(
    test: Boolean? = null,
    page: PageInput? = null,
    filter: PlatformAdditionalFeePolicyFilterInput? = null,
  ): CompletableFuture<GetPlatformAdditionalFeePoliciesResponse> = GlobalScope.future { getPlatformAdditionalFeePolicies(test, page, filter) }


  /**
   * 추가 수수료 정책 생성
   *
   * 새로운 추가 수수료 정책을 생성합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param id
   * 생성할 추가 수수료 정책 아이디
   *
   * 명시하지 않으면 id 가 임의로 생성됩니다.
   * @param name
   * 이름
   * @param fee
   * 수수료 정보
   * @param memo
   * 메모
   * @param vatPayer
   * 부가세 부담 주체
   *
   * @throws CreatePlatformAdditionalFeePolicyException
   */
  @JvmName("createPlatformAdditionalFeePolicySuspend")
  public suspend fun createPlatformAdditionalFeePolicy(
    test: Boolean? = null,
    id: String? = null,
    name: String,
    fee: PlatformFeeInput,
    memo: String? = null,
    vatPayer: PlatformPayer,
  ): CreatePlatformAdditionalFeePolicyResponse {
    val requestBody = CreatePlatformAdditionalFeePolicyBody(
      id = id,
      name = name,
      fee = fee,
      memo = memo,
      vatPayer = vatPayer,
    )
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "additional-fee-policies")
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
        json.decodeFromString<CreatePlatformAdditionalFeePolicyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAdditionalFeePolicyAlreadyExistsError -> throw PlatformAdditionalFeePolicyAlreadyExistsException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreatePlatformAdditionalFeePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformAdditionalFeePolicy")
  public fun createPlatformAdditionalFeePolicyFuture(
    test: Boolean? = null,
    id: String? = null,
    name: String,
    fee: PlatformFeeInput,
    memo: String? = null,
    vatPayer: PlatformPayer,
  ): CompletableFuture<CreatePlatformAdditionalFeePolicyResponse> = GlobalScope.future { createPlatformAdditionalFeePolicy(test, id, name, fee, memo, vatPayer) }


  /**
   * 계약 보관
   *
   * 주어진 아이디에 대응되는 계약을 보관합니다.
   *
   * @param id
   * 계약 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws ArchivePlatformContractException
   */
  @JvmName("archivePlatformContractSuspend")
  public suspend fun archivePlatformContract(
    id: String,
    test: Boolean? = null,
  ): ArchivePlatformContractResponse {
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "contracts", id.toString(), "archive")
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
        json.decodeFromString<ArchivePlatformContractError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformCannotArchiveScheduledContractError -> throw PlatformCannotArchiveScheduledContractException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ArchivePlatformContractResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("archivePlatformContract")
  public fun archivePlatformContractFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<ArchivePlatformContractResponse> = GlobalScope.future { archivePlatformContract(id, test) }


  /**
   * 계약 복원
   *
   * 주어진 아이디에 대응되는 계약을 복원합니다.
   *
   * @param id
   * 계약 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws RecoverPlatformContractException
   */
  @JvmName("recoverPlatformContractSuspend")
  public suspend fun recoverPlatformContract(
    id: String,
    test: Boolean? = null,
  ): RecoverPlatformContractResponse {
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "contracts", id.toString(), "recover")
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
        json.decodeFromString<RecoverPlatformContractError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<RecoverPlatformContractResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("recoverPlatformContract")
  public fun recoverPlatformContractFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<RecoverPlatformContractResponse> = GlobalScope.future { recoverPlatformContract(id, test) }


  /**
   * 계약 조회
   *
   * 주어진 아이디에 대응되는 계약을 조회합니다.
   *
   * @param id
   * 조회할 계약 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws GetPlatformContractException
   */
  @JvmName("getPlatformContractSuspend")
  public suspend fun getPlatformContract(
    id: String,
    test: Boolean? = null,
  ): PlatformContract {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("platform", "contracts", id.toString())
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
        json.decodeFromString<GetPlatformContractError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PlatformContract>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformContract")
  public fun getPlatformContractFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<PlatformContract> = GlobalScope.future { getPlatformContract(id, test) }


  /**
   * 계약 수정
   *
   * 주어진 아이디에 대응되는 계약을 업데이트합니다.
   *
   * @param id
   * 업데이트할 계약 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param name
   * 계약 이름
   * @param memo
   * 계약 내부 표기를 위한 메모
   * @param platformFee
   * 중개수수료
   * @param settlementCycle
   * 정산 주기
   * @param platformFeeVatPayer
   * 중개수수료에 대한 부가세 부담 주체
   * @param subtractPaymentVatAmount
   * 정산 시 결제금액 부가세 감액 여부
   *
   * @throws UpdatePlatformContractException
   */
  @JvmName("updatePlatformContractSuspend")
  public suspend fun updatePlatformContract(
    id: String,
    test: Boolean? = null,
    name: String? = null,
    memo: String? = null,
    platformFee: PlatformFeeInput? = null,
    settlementCycle: PlatformSettlementCycleInput? = null,
    platformFeeVatPayer: PlatformPayer? = null,
    subtractPaymentVatAmount: Boolean? = null,
  ): UpdatePlatformContractResponse {
    val requestBody = UpdatePlatformContractBody(
      name = name,
      memo = memo,
      platformFee = platformFee,
      settlementCycle = settlementCycle,
      platformFeeVatPayer = platformFeeVatPayer,
      subtractPaymentVatAmount = subtractPaymentVatAmount,
    )
    val httpResponse = client.patch(apiBase) {
      url {
        this.appendPathSegments("platform", "contracts", id.toString())
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
        json.decodeFromString<UpdatePlatformContractError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformArchivedContractError -> throw PlatformArchivedContractException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdatePlatformContractResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updatePlatformContract")
  public fun updatePlatformContractFuture(
    id: String,
    test: Boolean? = null,
    name: String? = null,
    memo: String? = null,
    platformFee: PlatformFeeInput? = null,
    settlementCycle: PlatformSettlementCycleInput? = null,
    platformFeeVatPayer: PlatformPayer? = null,
    subtractPaymentVatAmount: Boolean? = null,
  ): CompletableFuture<UpdatePlatformContractResponse> = GlobalScope.future { updatePlatformContract(id, test, name, memo, platformFee, settlementCycle, platformFeeVatPayer, subtractPaymentVatAmount) }


  /**
   * 계약 다건 조회
   *
   * 여러 계약을 조회합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param page
   * 요청할 페이지 정보
   * @param filter
   * 조회할 계약 조건 필터
   *
   * @throws GetPlatformContractsException
   */
  @JvmName("getPlatformContractsSuspend")
  public suspend fun getPlatformContracts(
    test: Boolean? = null,
    page: PageInput? = null,
    filter: PlatformContractFilterInput? = null,
  ): GetPlatformContractsResponse {
    val requestBody = GetPlatformContractsBody(
      page = page,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("platform", "contracts")
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
        json.decodeFromString<GetPlatformContractsError.Recognized>(httpBody)
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
      json.decodeFromString<GetPlatformContractsResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformContracts")
  public fun getPlatformContractsFuture(
    test: Boolean? = null,
    page: PageInput? = null,
    filter: PlatformContractFilterInput? = null,
  ): CompletableFuture<GetPlatformContractsResponse> = GlobalScope.future { getPlatformContracts(test, page, filter) }


  /**
   * 계약 생성
   *
   * 새로운 계약을 생성합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param id
   * 계약에 부여할 고유 아이디
   *
   * 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
   * @param name
   * 계약 이름
   * @param memo
   * 계약 내부 표기를 위한 메모
   * @param platformFee
   * 중개수수료
   * @param settlementCycle
   * 정산 주기
   * @param platformFeeVatPayer
   * 중개수수료에 대한 부가세 부담 주체
   * @param subtractPaymentVatAmount
   * 정산 시 결제금액 부가세 감액 여부
   *
   * @throws CreatePlatformContractException
   */
  @JvmName("createPlatformContractSuspend")
  public suspend fun createPlatformContract(
    test: Boolean? = null,
    id: String? = null,
    name: String,
    memo: String? = null,
    platformFee: PlatformFeeInput,
    settlementCycle: PlatformSettlementCycleInput,
    platformFeeVatPayer: PlatformPayer,
    subtractPaymentVatAmount: Boolean,
  ): CreatePlatformContractResponse {
    val requestBody = CreatePlatformContractBody(
      id = id,
      name = name,
      memo = memo,
      platformFee = platformFee,
      settlementCycle = settlementCycle,
      platformFeeVatPayer = platformFeeVatPayer,
      subtractPaymentVatAmount = subtractPaymentVatAmount,
    )
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "contracts")
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
        json.decodeFromString<CreatePlatformContractError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformContractAlreadyExistsError -> throw PlatformContractAlreadyExistsException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreatePlatformContractResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformContract")
  public fun createPlatformContractFuture(
    test: Boolean? = null,
    id: String? = null,
    name: String,
    memo: String? = null,
    platformFee: PlatformFeeInput,
    settlementCycle: PlatformSettlementCycleInput,
    platformFeeVatPayer: PlatformPayer,
    subtractPaymentVatAmount: Boolean,
  ): CompletableFuture<CreatePlatformContractResponse> = GlobalScope.future { createPlatformContract(test, id, name, memo, platformFee, settlementCycle, platformFeeVatPayer, subtractPaymentVatAmount) }


  /**
   * 할인 분담 정책 보관
   *
   * 주어진 아이디에 대응되는 할인 분담을 보관합니다.
   *
   * @param id
   * 할인 분담 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws ArchivePlatformDiscountSharePolicyException
   */
  @JvmName("archivePlatformDiscountSharePolicySuspend")
  public suspend fun archivePlatformDiscountSharePolicy(
    id: String,
    test: Boolean? = null,
  ): ArchivePlatformDiscountSharePolicyResponse {
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "discount-share-policies", id.toString(), "archive")
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
        json.decodeFromString<ArchivePlatformDiscountSharePolicyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformCannotArchiveScheduledDiscountSharePolicyError -> throw PlatformCannotArchiveScheduledDiscountSharePolicyException(httpBodyDecoded)
        is PlatformDiscountSharePolicyNotFoundError -> throw PlatformDiscountSharePolicyNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ArchivePlatformDiscountSharePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("archivePlatformDiscountSharePolicy")
  public fun archivePlatformDiscountSharePolicyFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<ArchivePlatformDiscountSharePolicyResponse> = GlobalScope.future { archivePlatformDiscountSharePolicy(id, test) }


  /**
   * 할인 분담 정책 복원
   *
   * 주어진 아이디에 대응되는 할인 분담을 복원합니다.
   *
   * @param id
   * 할인 분담 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws RecoverPlatformDiscountSharePolicyException
   */
  @JvmName("recoverPlatformDiscountSharePolicySuspend")
  public suspend fun recoverPlatformDiscountSharePolicy(
    id: String,
    test: Boolean? = null,
  ): RecoverPlatformDiscountSharePolicyResponse {
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "discount-share-policies", id.toString(), "recover")
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
        json.decodeFromString<RecoverPlatformDiscountSharePolicyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformDiscountSharePolicyNotFoundError -> throw PlatformDiscountSharePolicyNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<RecoverPlatformDiscountSharePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("recoverPlatformDiscountSharePolicy")
  public fun recoverPlatformDiscountSharePolicyFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<RecoverPlatformDiscountSharePolicyResponse> = GlobalScope.future { recoverPlatformDiscountSharePolicy(id, test) }


  /**
   * 할인 분담 정책 조회
   *
   * 주어진 아이디에 대응되는 할인 분담을 조회합니다.
   *
   * @param id
   * 조회할 할인 분담 정책 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   *
   * @throws GetPlatformDiscountSharePolicyException
   */
  @JvmName("getPlatformDiscountSharePolicySuspend")
  public suspend fun getPlatformDiscountSharePolicy(
    id: String,
    test: Boolean? = null,
  ): PlatformDiscountSharePolicy {
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("platform", "discount-share-policies", id.toString())
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
        json.decodeFromString<GetPlatformDiscountSharePolicyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformDiscountSharePolicyNotFoundError -> throw PlatformDiscountSharePolicyNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PlatformDiscountSharePolicy>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformDiscountSharePolicy")
  public fun getPlatformDiscountSharePolicyFuture(
    id: String,
    test: Boolean? = null,
  ): CompletableFuture<PlatformDiscountSharePolicy> = GlobalScope.future { getPlatformDiscountSharePolicy(id, test) }


  /**
   * 할인 분담 정책 수정
   *
   * 주어진 아이디에 대응되는 할인 분담을 업데이트합니다.
   *
   * @param id
   * 업데이트할 할인 분담 정책 아이디
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param name
   * 할인 분담 정책 이름
   * @param partnerShareRate
   * 할인 분담율
   *
   * 파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
   * @param memo
   * 해당 할인 분담에 대한 메모
   *
   * @throws UpdatePlatformDiscountSharePolicyException
   */
  @JvmName("updatePlatformDiscountSharePolicySuspend")
  public suspend fun updatePlatformDiscountSharePolicy(
    id: String,
    test: Boolean? = null,
    name: String? = null,
    partnerShareRate: Int? = null,
    memo: String? = null,
  ): UpdatePlatformDiscountSharePolicyResponse {
    val requestBody = UpdatePlatformDiscountSharePolicyBody(
      name = name,
      partnerShareRate = partnerShareRate,
      memo = memo,
    )
    val httpResponse = client.patch(apiBase) {
      url {
        this.appendPathSegments("platform", "discount-share-policies", id.toString())
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
        json.decodeFromString<UpdatePlatformDiscountSharePolicyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformArchivedDiscountSharePolicyError -> throw PlatformArchivedDiscountSharePolicyException(httpBodyDecoded)
        is PlatformDiscountSharePolicyNotFoundError -> throw PlatformDiscountSharePolicyNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdatePlatformDiscountSharePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updatePlatformDiscountSharePolicy")
  public fun updatePlatformDiscountSharePolicyFuture(
    id: String,
    test: Boolean? = null,
    name: String? = null,
    partnerShareRate: Int? = null,
    memo: String? = null,
  ): CompletableFuture<UpdatePlatformDiscountSharePolicyResponse> = GlobalScope.future { updatePlatformDiscountSharePolicy(id, test, name, partnerShareRate, memo) }


  /**
   * 할인 분담 정책 다건 조회
   *
   * 여러 할인 분담을 조회합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param page
   * 요청할 페이지 정보
   * @param filter
   * 조회할 할인 분담 정책 조건 필터
   *
   * @throws GetPlatformDiscountSharePoliciesException
   */
  @JvmName("getPlatformDiscountSharePoliciesSuspend")
  public suspend fun getPlatformDiscountSharePolicies(
    test: Boolean? = null,
    page: PageInput? = null,
    filter: PlatformDiscountSharePolicyFilterInput? = null,
  ): GetPlatformDiscountSharePoliciesResponse {
    val requestBody = GetPlatformDiscountSharePoliciesBody(
      page = page,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        this.appendPathSegments("platform", "discount-share-policies")
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
        json.decodeFromString<GetPlatformDiscountSharePoliciesError.Recognized>(httpBody)
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
      json.decodeFromString<GetPlatformDiscountSharePoliciesResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformDiscountSharePolicies")
  public fun getPlatformDiscountSharePoliciesFuture(
    test: Boolean? = null,
    page: PageInput? = null,
    filter: PlatformDiscountSharePolicyFilterInput? = null,
  ): CompletableFuture<GetPlatformDiscountSharePoliciesResponse> = GlobalScope.future { getPlatformDiscountSharePolicies(test, page, filter) }


  /**
   * 할인 분담 정책 생성
   *
   * 새로운 할인 분담을 생성합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   * @param id
   * 할인 분담에 부여할 고유 아이디
   *
   * 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
   * @param name
   * 할인 분담에 부여할 이름
   * @param partnerShareRate
   * 파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
   * @param memo
   * 해당 할인 분담에 대한 메모 ex) 파트너 브랜드 쿠폰
   *
   * @throws CreatePlatformDiscountSharePolicyException
   */
  @JvmName("createPlatformDiscountSharePolicySuspend")
  public suspend fun createPlatformDiscountSharePolicy(
    test: Boolean? = null,
    id: String? = null,
    name: String,
    partnerShareRate: Int,
    memo: String? = null,
  ): CreatePlatformDiscountSharePolicyResponse {
    val requestBody = CreatePlatformDiscountSharePolicyBody(
      id = id,
      name = name,
      partnerShareRate = partnerShareRate,
      memo = memo,
    )
    val httpResponse = client.post(apiBase) {
      url {
        this.appendPathSegments("platform", "discount-share-policies")
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
        json.decodeFromString<CreatePlatformDiscountSharePolicyError.Recognized>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformDiscountSharePolicyAlreadyExistsError -> throw PlatformDiscountSharePolicyAlreadyExistsException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreatePlatformDiscountSharePolicyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformDiscountSharePolicy")
  public fun createPlatformDiscountSharePolicyFuture(
    test: Boolean? = null,
    id: String? = null,
    name: String,
    partnerShareRate: Int,
    memo: String? = null,
  ): CompletableFuture<CreatePlatformDiscountSharePolicyResponse> = GlobalScope.future { createPlatformDiscountSharePolicy(test, id, name, partnerShareRate, memo) }

  override fun close() {
    client.close()
  }
}
