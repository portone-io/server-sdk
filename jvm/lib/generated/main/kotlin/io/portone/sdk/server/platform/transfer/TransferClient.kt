package io.portone.sdk.server.transfer

import io.ktor.client.HttpClient
import io.portone.sdk.server.CreateManualTransferResponse
import io.portone.sdk.server.CreateOrderCancelTransferResponse
import io.portone.sdk.server.CreateOrderTransferResponse
import io.portone.sdk.server.DeletePlatformTransferResponse
import io.portone.sdk.server.GetPlatformTransferSummariesResponse
import io.portone.sdk.server.PlatformTransfer
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.transfer.CreateManualTransferResponse
import io.portone.sdk.server.platform.transfer.CreateOrderCancelTransferResponse
import io.portone.sdk.server.platform.transfer.CreateOrderTransferResponse
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderCancelTransferBodyDiscount
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderCancelTransferBodyExternalCancellationDetail
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderCancelTransferBodyOrderDetail
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyAdditionalFee
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyDiscount
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyExternalPaymentDetail
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyOrderDetail
import io.portone.sdk.server.platform.transfer.DeletePlatformTransferResponse
import io.portone.sdk.server.platform.transfer.GetPlatformTransferSummariesResponse
import io.portone.sdk.server.platform.transfer.PlatformTransfer
import io.portone.sdk.server.platform.transfer.PlatformTransferFilterInput
import io.portone.sdk.server.platform.transfer.PlatformTransferSheetField
import io.portone.sdk.server.platform.transfer.PlatformUserDefinedPropertyKeyValue
import io.portone.sdk.server.platform.transfer.TransferParameters
import java.io.Closeable
import kotlin.Array
import kotlin.String
import kotlinx.serialization.json.Json

public class TransferClient(
  private val apiSecret: String,
  private val storeId: String,
  private val apiBase: String,
) : Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 정산건 조회
   *
   * 정산건을 조회합니다.
   *
   * @param id
   * 조회하고 싶은 정산건 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformTransferNotFoundException PlatformTransferNotFoundError
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformTransferSuspend")
  public suspend fun getPlatformTransfer(
    id: string,
  ): PlatformTransfer {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "transfers", id)
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
        json.decodeFromString<GetPlatformTransferError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformTransferNotFoundError -> throw PlatformTransferNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PlatformTransfer>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformTransfer")
  public suspend fun getPlatformTransferFuture(
    id: string,
  ): CompletableFuture<PlatformTransfer> = GlobalScope.future { getPlatformTransfer(id) }


  /**
   * 정산건 삭제
   *
   * scheduled, in_process 상태의 정산건만 삭제가능합니다.
   *
   * @param id
   * 정산건 아이디
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformCancelOrderTransfersExistsException PlatformCancelOrderTransfersExistsError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformTransferNonDeletableStatusException PlatformTransferNonDeletableStatusError
   * @throws PlatformTransferNotFoundException PlatformTransferNotFoundError
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("deletePlatformTransferSuspend")
  public suspend fun deletePlatformTransfer(
    id: string,
  ): DeletePlatformTransferResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "transfers", id)
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
        json.decodeFromString<DeletePlatformTransferError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformCancelOrderTransfersExistsError -> throw PlatformCancelOrderTransfersExistsException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformTransferNonDeletableStatusError -> throw PlatformTransferNonDeletableStatusException(httpBodyDecoded)
        is PlatformTransferNotFoundError -> throw PlatformTransferNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<DeletePlatformTransferResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("deletePlatformTransfer")
  public suspend fun deletePlatformTransferFuture(
    id: string,
  ): CompletableFuture<DeletePlatformTransferResponse> = GlobalScope.future { deletePlatformTransfer(id) }


  /**
   * 정산건 다건 조회
   *
   * 성공 응답으로 조회된 정산건 요약 리스트와 페이지 정보가 반환됩니다.
   *
   * @param page
   * 요청할 페이지 정보
   * @param filter
   * 조회할 정산건 조건 필터
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getPlatformTransferSummariesSuspend")
  public suspend fun getPlatformTransferSummaries(
    page: PageInput? = null,
    filter: PlatformTransferFilterInput? = null,
  ): GetPlatformTransferSummariesResponse {
    val requestBody = GetPlatformTransferSummariesBody(
      page = page,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "transfer-summaries")
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
        json.decodeFromString<GetPlatformTransferSummariesError>(httpBody)
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
      json.decodeFromString<GetPlatformTransferSummariesResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformTransferSummaries")
  public suspend fun getPlatformTransferSummariesFuture(
    page: PageInput? = null,
    filter: PlatformTransferFilterInput? = null,
  ): CompletableFuture<GetPlatformTransferSummariesResponse> = GlobalScope.future { getPlatformTransferSummaries(page, filter) }


  /**
   * 주문 정산건 생성
   *
   * 성공 응답으로 생성된 주문 정산건 객체가 반환됩니다.
   *
   * @param partnerId
   * 파트너 아이디
   * @param contractId
   * 계약 아이디
   *
   * 기본값은 파트너의 기본 계약 아이디 입니다.
   * @param memo
   * 메모
   * @param paymentId
   * 결제 아이디
   * @param orderDetail
   * 주문 정보
   * @param taxFreeAmount
   * 주문 면세 금액
   *
   * 주문 항목과 면세 금액을 같이 전달하시면 최종 면세 금액은 주문 항목의 면세 금액이 아닌 전달해주신 면세 금액으로 적용됩니다.
   * @param settlementStartDate
   * 정산 시작일
   *
   * 기본값은 결제 일시 입니다.
   * @param discounts
   * 할인 정보
   * @param additionalFees
   * 추가 수수료 정보
   * @param externalPaymentDetail
   * 외부 결제 상세 정보
   *
   * 해당 정보가 존재하는 경우 외부 결제 정산건 으로 등록되고, 존재하지않은 경우 포트원 결제 정산건으로 등록됩니다.
   * @param isForTest
   * 테스트 모드 여부
   *
   * 기본값은 false 입니다.
   * @param parameters
   * 정산 파라미터 (실험기능)
   * @param userDefinedProperties
   * 사용자 정의 속성
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformAdditionalFeePoliciesNotFoundException PlatformAdditionalFeePoliciesNotFoundError
   * @throws PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedException PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
   * @throws PlatformContractNotFoundException PlatformContractNotFoundError
   * @throws PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedException PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
   * @throws PlatformCurrencyNotSupportedException 지원 되지 않는 통화를 선택한 경우
   * @throws PlatformDiscountSharePoliciesNotFoundException PlatformDiscountSharePoliciesNotFoundError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformPartnerNotFoundException PlatformPartnerNotFoundError
   * @throws PlatformPaymentNotFoundException PlatformPaymentNotFoundError
   * @throws PlatformProductIdDuplicatedException PlatformProductIdDuplicatedError
   * @throws PlatformSettlementAmountExceededException 정산 가능한 금액을 초과한 경우
   * @throws PlatformSettlementParameterNotFoundException 정산 파라미터가 존재하지 않는 경우
   * @throws PlatformSettlementPaymentAmountExceededPortOnePaymentException 정산 요청 결제 금액이 포트원 결제 내역의 결제 금액을 초과한 경우
   * @throws PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentException 정산 요청 공급대가가 포트원 결제 내역의 공급대가를 초과한 경우
   * @throws PlatformSettlementTaxFreeAmountExceededPortOnePaymentException 정산 요청 면세 금액이 포트원 결제 내역의 면세 금액을 초과한 경우
   * @throws PlatformTransferAlreadyExistsException PlatformTransferAlreadyExistsError
   * @throws PlatformUserDefinedPropertyNotFoundException 사용자 정의 속성이 존재 하지 않는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("createPlatformOrderTransferSuspend")
  public suspend fun createPlatformOrderTransfer(
    partnerId: string,
    contractId: string? = null,
    memo: string? = null,
    paymentId: string,
    orderDetail: CreatePlatformOrderTransferBodyOrderDetail,
    taxFreeAmount: Long? = null,
    settlementStartDate: string? = null,
    discounts: Array<CreatePlatformOrderTransferBodyDiscount>,
    additionalFees: Array<CreatePlatformOrderTransferBodyAdditionalFee>,
    externalPaymentDetail: CreatePlatformOrderTransferBodyExternalPaymentDetail? = null,
    isForTest: Boolean? = null,
    parameters: TransferParameters? = null,
    userDefinedProperties: Array<PlatformUserDefinedPropertyKeyValue>? = null,
  ): CreateOrderTransferResponse {
    val requestBody = CreatePlatformOrderTransferBody(
      partnerId = partnerId,
      contractId = contractId,
      memo = memo,
      paymentId = paymentId,
      orderDetail = orderDetail,
      taxFreeAmount = taxFreeAmount,
      settlementStartDate = settlementStartDate,
      discounts = discounts,
      additionalFees = additionalFees,
      externalPaymentDetail = externalPaymentDetail,
      isForTest = isForTest,
      parameters = parameters,
      userDefinedProperties = userDefinedProperties,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "transfers", "order")
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
        json.decodeFromString<CreatePlatformOrderTransferError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformAdditionalFeePoliciesNotFoundError -> throw PlatformAdditionalFeePoliciesNotFoundException(httpBodyDecoded)
        is PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError -> throw PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedException(httpBodyDecoded)
        is PlatformContractNotFoundError -> throw PlatformContractNotFoundException(httpBodyDecoded)
        is PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError -> throw PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedException(httpBodyDecoded)
        is PlatformCurrencyNotSupportedError -> throw PlatformCurrencyNotSupportedException(httpBodyDecoded)
        is PlatformDiscountSharePoliciesNotFoundError -> throw PlatformDiscountSharePoliciesNotFoundException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformPartnerNotFoundError -> throw PlatformPartnerNotFoundException(httpBodyDecoded)
        is PlatformPaymentNotFoundError -> throw PlatformPaymentNotFoundException(httpBodyDecoded)
        is PlatformProductIdDuplicatedError -> throw PlatformProductIdDuplicatedException(httpBodyDecoded)
        is PlatformSettlementAmountExceededError -> throw PlatformSettlementAmountExceededException(httpBodyDecoded)
        is PlatformSettlementParameterNotFoundError -> throw PlatformSettlementParameterNotFoundException(httpBodyDecoded)
        is PlatformSettlementPaymentAmountExceededPortOnePaymentError -> throw PlatformSettlementPaymentAmountExceededPortOnePaymentException(httpBodyDecoded)
        is PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError -> throw PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentException(httpBodyDecoded)
        is PlatformSettlementTaxFreeAmountExceededPortOnePaymentError -> throw PlatformSettlementTaxFreeAmountExceededPortOnePaymentException(httpBodyDecoded)
        is PlatformTransferAlreadyExistsError -> throw PlatformTransferAlreadyExistsException(httpBodyDecoded)
        is PlatformUserDefinedPropertyNotFoundError -> throw PlatformUserDefinedPropertyNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreateOrderTransferResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformOrderTransfer")
  public suspend fun createPlatformOrderTransferFuture(
    partnerId: string,
    contractId: string? = null,
    memo: string? = null,
    paymentId: string,
    orderDetail: CreatePlatformOrderTransferBodyOrderDetail,
    taxFreeAmount: Long? = null,
    settlementStartDate: string? = null,
    discounts: Array<CreatePlatformOrderTransferBodyDiscount>,
    additionalFees: Array<CreatePlatformOrderTransferBodyAdditionalFee>,
    externalPaymentDetail: CreatePlatformOrderTransferBodyExternalPaymentDetail? = null,
    isForTest: Boolean? = null,
    parameters: TransferParameters? = null,
    userDefinedProperties: Array<PlatformUserDefinedPropertyKeyValue>? = null,
  ): CompletableFuture<CreateOrderTransferResponse> = GlobalScope.future { createPlatformOrderTransfer(partnerId, contractId, memo, paymentId, orderDetail, taxFreeAmount, settlementStartDate, discounts, additionalFees, externalPaymentDetail, isForTest, parameters, userDefinedProperties) }


  /**
   * 주문 취소 정산건 생성
   *
   * 성공 응답으로 생성된 주문 취소 정산건 객체가 반환됩니다.
   *
   * @param partnerId
   * 파트너 아이디
   * @param paymentId
   * 결제 아이디
   * @param transferId
   * 정산건 아이디
   * @param cancellationId
   * 취소 내역 아이디
   * @param memo
   * 메모
   * @param orderDetail
   * 주문 취소 정보
   * @param taxFreeAmount
   * 주문 취소 면세 금액
   *
   * 주문 취소 항목과 취소 면세 금액을 같이 전달하시면 최종 취소 면세 금액은 주문 취소 항목의 면세 금액이 아닌 전달해주신 취소 면세 금액으로 적용됩니다.
   * @param discounts
   * 할인 정보
   * @param settlementStartDate
   * 정산 시작일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * @param externalCancellationDetail
   * 외부 결제 상세 정보
   *
   * 해당 정보가 존재하는 경우 외부 결제 취소 정산건으로 등록되고, 존재하지않은 경우 포트원 결제 취소 정산건으로 등록됩니다.
   * @param isForTest
   * 테스트 모드 여부
   *
   * 기본값은 false 입니다.
   * @param userDefinedProperties
   * 사용자 정의 속성
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformCancellableAmountExceededException 취소 가능한 금액이 초과한 경우
   * @throws PlatformCancellableDiscountAmountExceededException PlatformCancellableDiscountAmountExceededError
   * @throws PlatformCancellableDiscountTaxFreeAmountExceededException PlatformCancellableDiscountTaxFreeAmountExceededError
   * @throws PlatformCancellableProductQuantityExceededException PlatformCancellableProductQuantityExceededError
   * @throws PlatformCancellationAndPaymentTypeMismatchedException PlatformCancellationAndPaymentTypeMismatchedError
   * @throws PlatformCancellationNotFoundException PlatformCancellationNotFoundError
   * @throws PlatformCannotSpecifyTransferException 정산 건 식별에 실패한 경우
   * @throws PlatformDiscountSharePolicyIdDuplicatedException PlatformDiscountSharePolicyIdDuplicatedError
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformOrderDetailMismatchedException PlatformOrderDetailMismatchedError
   * @throws PlatformOrderTransferAlreadyCancelledException PlatformOrderTransferAlreadyCancelledError
   * @throws PlatformPaymentNotFoundException PlatformPaymentNotFoundError
   * @throws PlatformProductIdDuplicatedException PlatformProductIdDuplicatedError
   * @throws PlatformProductIdNotFoundException PlatformProductIdNotFoundError
   * @throws PlatformSettlementAmountExceededException 정산 가능한 금액을 초과한 경우
   * @throws PlatformSettlementCancelAmountExceededPortOneCancelException 정산 취소 요청 금액이 포트원 결제 취소 내역의 취소 금액을 초과한 경우
   * @throws PlatformTransferAlreadyExistsException PlatformTransferAlreadyExistsError
   * @throws PlatformTransferDiscountSharePolicyNotFoundException PlatformTransferDiscountSharePolicyNotFoundError
   * @throws PlatformTransferNotFoundException PlatformTransferNotFoundError
   * @throws PlatformUserDefinedPropertyNotFoundException 사용자 정의 속성이 존재 하지 않는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("createPlatformOrderCancelTransferSuspend")
  public suspend fun createPlatformOrderCancelTransfer(
    partnerId: string? = null,
    paymentId: string? = null,
    transferId: string? = null,
    cancellationId: string,
    memo: string? = null,
    orderDetail: CreatePlatformOrderCancelTransferBodyOrderDetail? = null,
    taxFreeAmount: Long? = null,
    discounts: Array<CreatePlatformOrderCancelTransferBodyDiscount>,
    settlementStartDate: string? = null,
    externalCancellationDetail: CreatePlatformOrderCancelTransferBodyExternalCancellationDetail? = null,
    isForTest: Boolean? = null,
    userDefinedProperties: Array<PlatformUserDefinedPropertyKeyValue>? = null,
  ): CreateOrderCancelTransferResponse {
    val requestBody = CreatePlatformOrderCancelTransferBody(
      partnerId = partnerId,
      paymentId = paymentId,
      transferId = transferId,
      cancellationId = cancellationId,
      memo = memo,
      orderDetail = orderDetail,
      taxFreeAmount = taxFreeAmount,
      discounts = discounts,
      settlementStartDate = settlementStartDate,
      externalCancellationDetail = externalCancellationDetail,
      isForTest = isForTest,
      userDefinedProperties = userDefinedProperties,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "transfers", "order-cancel")
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
        json.decodeFromString<CreatePlatformOrderCancelTransferError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformCancellableAmountExceededError -> throw PlatformCancellableAmountExceededException(httpBodyDecoded)
        is PlatformCancellableDiscountAmountExceededError -> throw PlatformCancellableDiscountAmountExceededException(httpBodyDecoded)
        is PlatformCancellableDiscountTaxFreeAmountExceededError -> throw PlatformCancellableDiscountTaxFreeAmountExceededException(httpBodyDecoded)
        is PlatformCancellableProductQuantityExceededError -> throw PlatformCancellableProductQuantityExceededException(httpBodyDecoded)
        is PlatformCancellationAndPaymentTypeMismatchedError -> throw PlatformCancellationAndPaymentTypeMismatchedException(httpBodyDecoded)
        is PlatformCancellationNotFoundError -> throw PlatformCancellationNotFoundException(httpBodyDecoded)
        is PlatformCannotSpecifyTransferError -> throw PlatformCannotSpecifyTransferException(httpBodyDecoded)
        is PlatformDiscountSharePolicyIdDuplicatedError -> throw PlatformDiscountSharePolicyIdDuplicatedException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformOrderDetailMismatchedError -> throw PlatformOrderDetailMismatchedException(httpBodyDecoded)
        is PlatformOrderTransferAlreadyCancelledError -> throw PlatformOrderTransferAlreadyCancelledException(httpBodyDecoded)
        is PlatformPaymentNotFoundError -> throw PlatformPaymentNotFoundException(httpBodyDecoded)
        is PlatformProductIdDuplicatedError -> throw PlatformProductIdDuplicatedException(httpBodyDecoded)
        is PlatformProductIdNotFoundError -> throw PlatformProductIdNotFoundException(httpBodyDecoded)
        is PlatformSettlementAmountExceededError -> throw PlatformSettlementAmountExceededException(httpBodyDecoded)
        is PlatformSettlementCancelAmountExceededPortOneCancelError -> throw PlatformSettlementCancelAmountExceededPortOneCancelException(httpBodyDecoded)
        is PlatformTransferAlreadyExistsError -> throw PlatformTransferAlreadyExistsException(httpBodyDecoded)
        is PlatformTransferDiscountSharePolicyNotFoundError -> throw PlatformTransferDiscountSharePolicyNotFoundException(httpBodyDecoded)
        is PlatformTransferNotFoundError -> throw PlatformTransferNotFoundException(httpBodyDecoded)
        is PlatformUserDefinedPropertyNotFoundError -> throw PlatformUserDefinedPropertyNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreateOrderCancelTransferResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformOrderCancelTransfer")
  public suspend fun createPlatformOrderCancelTransferFuture(
    partnerId: string? = null,
    paymentId: string? = null,
    transferId: string? = null,
    cancellationId: string,
    memo: string? = null,
    orderDetail: CreatePlatformOrderCancelTransferBodyOrderDetail? = null,
    taxFreeAmount: Long? = null,
    discounts: Array<CreatePlatformOrderCancelTransferBodyDiscount>,
    settlementStartDate: string? = null,
    externalCancellationDetail: CreatePlatformOrderCancelTransferBodyExternalCancellationDetail? = null,
    isForTest: Boolean? = null,
    userDefinedProperties: Array<PlatformUserDefinedPropertyKeyValue>? = null,
  ): CompletableFuture<CreateOrderCancelTransferResponse> = GlobalScope.future { createPlatformOrderCancelTransfer(partnerId, paymentId, transferId, cancellationId, memo, orderDetail, taxFreeAmount, discounts, settlementStartDate, externalCancellationDetail, isForTest, userDefinedProperties) }


  /**
   * 수기 정산건 생성
   *
   * 성공 응답으로 생성된 수기 정산건 객체가 반환됩니다.
   *
   * @param partnerId
   * 파트너 아이디
   * @param memo
   * 메모
   * @param settlementAmount
   * 정산 금액
   * @param settlementDate
   * 정산 일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * @param isForTest
   * 테스트 모드 여부
   *
   * 기본값은 false 입니다.
   * @param userDefinedProperties
   * 사용자 정의 속성
   *
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws PlatformNotEnabledException 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
   * @throws PlatformPartnerNotFoundException PlatformPartnerNotFoundError
   * @throws PlatformUserDefinedPropertyNotFoundException 사용자 정의 속성이 존재 하지 않는 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("createPlatformManualTransferSuspend")
  public suspend fun createPlatformManualTransfer(
    partnerId: string,
    memo: string? = null,
    settlementAmount: Long,
    settlementDate: string,
    isForTest: Boolean? = null,
    userDefinedProperties: Array<PlatformUserDefinedPropertyKeyValue>? = null,
  ): CreateManualTransferResponse {
    val requestBody = CreatePlatformManualTransferBody(
      partnerId = partnerId,
      memo = memo,
      settlementAmount = settlementAmount,
      settlementDate = settlementDate,
      isForTest = isForTest,
      userDefinedProperties = userDefinedProperties,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "transfers", "manual")
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
        json.decodeFromString<CreatePlatformManualTransferError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PlatformNotEnabledError -> throw PlatformNotEnabledException(httpBodyDecoded)
        is PlatformPartnerNotFoundError -> throw PlatformPartnerNotFoundException(httpBodyDecoded)
        is PlatformUserDefinedPropertyNotFoundError -> throw PlatformUserDefinedPropertyNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CreateManualTransferResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownError("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformManualTransfer")
  public suspend fun createPlatformManualTransferFuture(
    partnerId: string,
    memo: string? = null,
    settlementAmount: Long,
    settlementDate: string,
    isForTest: Boolean? = null,
    userDefinedProperties: Array<PlatformUserDefinedPropertyKeyValue>? = null,
  ): CompletableFuture<CreateManualTransferResponse> = GlobalScope.future { createPlatformManualTransfer(partnerId, memo, settlementAmount, settlementDate, isForTest, userDefinedProperties) }


  /**
   * 정산 상세 내역 다운로드
   *
   * 정산 상세 내역을 csv 파일로 다운로드 합니다.
   *
   * @param filter
   *
   * @param fields
   * 다운로드 할 시트 컬럼
   * @param transferUserDefinedPropertyKeys
   *
   * @param partnerUserDefinedPropertyKeys
   *
   *
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("downloadPlatformTransferSheetSuspend")
  public suspend fun downloadPlatformTransferSheet(
    filter: PlatformTransferFilterInput? = null,
    fields: Array<PlatformTransferSheetField>? = null,
    transferUserDefinedPropertyKeys: Array<String>? = null,
    partnerUserDefinedPropertyKeys: Array<String>? = null,
  ): String {
    val requestBody = DownloadPlatformTransferSheetBody(
      filter = filter,
      fields = fields,
      transferUserDefinedPropertyKeys = transferUserDefinedPropertyKeys,
      partnerUserDefinedPropertyKeys = partnerUserDefinedPropertyKeys,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "transfer-summaries", "sheet-file")
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Text.Csv)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<DownloadPlatformTransferSheetError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    return httpResponse.body<String>()
  }

  /** @suppress */
  @JvmName("downloadPlatformTransferSheet")
  public suspend fun downloadPlatformTransferSheetFuture(
    filter: PlatformTransferFilterInput? = null,
    fields: Array<PlatformTransferSheetField>? = null,
    transferUserDefinedPropertyKeys: Array<String>? = null,
    partnerUserDefinedPropertyKeys: Array<String>? = null,
  ): String = GlobalScope.future { downloadPlatformTransferSheet(filter, fields, transferUserDefinedPropertyKeys, partnerUserDefinedPropertyKeys) }

  override fun close() {
    client.close()
  }
}
