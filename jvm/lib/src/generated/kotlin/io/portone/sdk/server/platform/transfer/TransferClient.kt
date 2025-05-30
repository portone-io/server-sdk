package io.portone.sdk.server.platform.transfer

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.request.`get`
import io.ktor.client.request.accept
import io.ktor.client.request.delete
import io.ktor.client.request.headers
import io.ktor.client.request.post
import io.ktor.client.request.setBody
import io.ktor.http.ContentType
import io.ktor.http.HttpHeaders
import io.ktor.http.appendPathSegments
import io.ktor.http.contentType
import io.ktor.http.userAgent
import io.portone.sdk.server.USER_AGENT
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.errors.CreatePlatformManualTransferError
import io.portone.sdk.server.errors.CreatePlatformManualTransferException
import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferException
import io.portone.sdk.server.errors.CreatePlatformOrderTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderTransferException
import io.portone.sdk.server.errors.DeletePlatformTransferError
import io.portone.sdk.server.errors.DeletePlatformTransferException
import io.portone.sdk.server.errors.DownloadPlatformTransferSheetError
import io.portone.sdk.server.errors.DownloadPlatformTransferSheetException
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetPlatformTransferError
import io.portone.sdk.server.errors.GetPlatformTransferException
import io.portone.sdk.server.errors.GetPlatformTransferSummariesError
import io.portone.sdk.server.errors.GetPlatformTransferSummariesException
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.PlatformAdditionalFeePoliciesNotFoundError
import io.portone.sdk.server.errors.PlatformAdditionalFeePoliciesNotFoundException
import io.portone.sdk.server.errors.PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
import io.portone.sdk.server.errors.PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedException
import io.portone.sdk.server.errors.PlatformCancelOrderTransfersExistsError
import io.portone.sdk.server.errors.PlatformCancelOrderTransfersExistsException
import io.portone.sdk.server.errors.PlatformCancellableAmountExceededError
import io.portone.sdk.server.errors.PlatformCancellableAmountExceededException
import io.portone.sdk.server.errors.PlatformCancellableDiscountAmountExceededError
import io.portone.sdk.server.errors.PlatformCancellableDiscountAmountExceededException
import io.portone.sdk.server.errors.PlatformCancellableDiscountTaxFreeAmountExceededError
import io.portone.sdk.server.errors.PlatformCancellableDiscountTaxFreeAmountExceededException
import io.portone.sdk.server.errors.PlatformCancellableProductQuantityExceededError
import io.portone.sdk.server.errors.PlatformCancellableProductQuantityExceededException
import io.portone.sdk.server.errors.PlatformCancellationAndPaymentTypeMismatchedError
import io.portone.sdk.server.errors.PlatformCancellationAndPaymentTypeMismatchedException
import io.portone.sdk.server.errors.PlatformCancellationNotFoundError
import io.portone.sdk.server.errors.PlatformCancellationNotFoundException
import io.portone.sdk.server.errors.PlatformCannotSpecifyTransferError
import io.portone.sdk.server.errors.PlatformCannotSpecifyTransferException
import io.portone.sdk.server.errors.PlatformContractNotFoundError
import io.portone.sdk.server.errors.PlatformContractNotFoundException
import io.portone.sdk.server.errors.PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
import io.portone.sdk.server.errors.PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedException
import io.portone.sdk.server.errors.PlatformCurrencyNotSupportedError
import io.portone.sdk.server.errors.PlatformCurrencyNotSupportedException
import io.portone.sdk.server.errors.PlatformDiscountSharePoliciesNotFoundError
import io.portone.sdk.server.errors.PlatformDiscountSharePoliciesNotFoundException
import io.portone.sdk.server.errors.PlatformDiscountSharePolicyIdDuplicatedError
import io.portone.sdk.server.errors.PlatformDiscountSharePolicyIdDuplicatedException
import io.portone.sdk.server.errors.PlatformNotEnabledError
import io.portone.sdk.server.errors.PlatformNotEnabledException
import io.portone.sdk.server.errors.PlatformOrderDetailMismatchedError
import io.portone.sdk.server.errors.PlatformOrderDetailMismatchedException
import io.portone.sdk.server.errors.PlatformOrderTransferAlreadyCancelledError
import io.portone.sdk.server.errors.PlatformOrderTransferAlreadyCancelledException
import io.portone.sdk.server.errors.PlatformPartnerNotFoundError
import io.portone.sdk.server.errors.PlatformPartnerNotFoundException
import io.portone.sdk.server.errors.PlatformPaymentNotFoundError
import io.portone.sdk.server.errors.PlatformPaymentNotFoundException
import io.portone.sdk.server.errors.PlatformProductIdDuplicatedError
import io.portone.sdk.server.errors.PlatformProductIdDuplicatedException
import io.portone.sdk.server.errors.PlatformProductIdNotFoundError
import io.portone.sdk.server.errors.PlatformProductIdNotFoundException
import io.portone.sdk.server.errors.PlatformSettlementAmountExceededError
import io.portone.sdk.server.errors.PlatformSettlementAmountExceededException
import io.portone.sdk.server.errors.PlatformSettlementCancelAmountExceededPortOneCancelError
import io.portone.sdk.server.errors.PlatformSettlementCancelAmountExceededPortOneCancelException
import io.portone.sdk.server.errors.PlatformSettlementDateEarlierThanSettlementStartDateError
import io.portone.sdk.server.errors.PlatformSettlementDateEarlierThanSettlementStartDateException
import io.portone.sdk.server.errors.PlatformSettlementParameterNotFoundError
import io.portone.sdk.server.errors.PlatformSettlementParameterNotFoundException
import io.portone.sdk.server.errors.PlatformSettlementPaymentAmountExceededPortOnePaymentError
import io.portone.sdk.server.errors.PlatformSettlementPaymentAmountExceededPortOnePaymentException
import io.portone.sdk.server.errors.PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError
import io.portone.sdk.server.errors.PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentException
import io.portone.sdk.server.errors.PlatformSettlementTaxFreeAmountExceededPortOnePaymentError
import io.portone.sdk.server.errors.PlatformSettlementTaxFreeAmountExceededPortOnePaymentException
import io.portone.sdk.server.errors.PlatformTransferAlreadyExistsError
import io.portone.sdk.server.errors.PlatformTransferAlreadyExistsException
import io.portone.sdk.server.errors.PlatformTransferDiscountSharePolicyNotFoundError
import io.portone.sdk.server.errors.PlatformTransferDiscountSharePolicyNotFoundException
import io.portone.sdk.server.errors.PlatformTransferNonDeletableStatusError
import io.portone.sdk.server.errors.PlatformTransferNonDeletableStatusException
import io.portone.sdk.server.errors.PlatformTransferNotFoundError
import io.portone.sdk.server.errors.PlatformTransferNotFoundException
import io.portone.sdk.server.errors.PlatformUserDefinedPropertyNotFoundError
import io.portone.sdk.server.errors.PlatformUserDefinedPropertyNotFoundException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.platform.transfer.CreateManualTransferResponse
import io.portone.sdk.server.platform.transfer.CreateOrderCancelTransferResponse
import io.portone.sdk.server.platform.transfer.CreateOrderTransferResponse
import io.portone.sdk.server.platform.transfer.CreatePlatformManualTransferBody
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderCancelTransferBody
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderCancelTransferBodyDiscount
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderCancelTransferBodyExternalCancellationDetail
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderCancelTransferBodyOrderDetail
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBody
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyAdditionalFee
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyDiscount
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyExternalPaymentDetail
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyOrderDetail
import io.portone.sdk.server.platform.transfer.DeletePlatformTransferResponse
import io.portone.sdk.server.platform.transfer.DownloadPlatformTransferSheetBody
import io.portone.sdk.server.platform.transfer.GetPlatformTransferSummariesBody
import io.portone.sdk.server.platform.transfer.GetPlatformTransferSummariesResponse
import io.portone.sdk.server.platform.transfer.PlatformTransfer
import io.portone.sdk.server.platform.transfer.PlatformTransferFilterInput
import io.portone.sdk.server.platform.transfer.PlatformUserDefinedPropertyKeyValue
import io.portone.sdk.server.platform.transfer.TransferParameters
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
 *
 * @param apiSecret 포트원 API Secret입니다.
 * @param apiBase 포트원 REST API 주소입니다. 기본값은 `"https://api.portone.io"`입니다.
 * @param storeId 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.
 */
public class TransferClient(
  private val apiSecret: String,
  private val apiBase: String = "https://api.portone.io",
  private val storeId: String? = null,
): Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 정산 상세 내역 다운로드
   *
   * 정산 상세 내역을 csv 파일로 다운로드 합니다.
   *
   * @param filter
   * 컬럼 키 목록
   *
   * - TRANSFER_MEMO:  메모
   * - TRANSFER_TYPE: 정산 유형
   * - TRANSFER_STATUS:  상태
   * - TRANSFER_ID: 정산 아이디
   * - TRANSFER_SETTLEMENT_DATE:  정산일
   * - TRANSFER_SETTLEMENT_AMOUNT: 정산 금액
   * - TRANSFER_SETTLEMENT_TAX_FREE_AMOUNT: 정산 면세액
   * - TRANSFER_SETTLEMENT_CURRENCY: 정산 통화
   * - TRANSFER_SETTLEMENT_START_DATE: 정산 시작일
   * - TRANSFER_ORDER_NAME:  주문명
   * - TRANSFER_ORDER_AMOUNT: 주문 금액
   * - TRANSFER_ORDER_TAX_FREE_AMOUNT: 주문 면세액
   * - TRANSFER_PAYMENT_ID: 주문 번호
   * - TRANSFER_PAYMENT_METHOD: 결제 수단
   * - TRANSFER_PAYMENT_AMOUNT: 결제 금액
   * - TRANSFER_PAYMENT_SUPPLY_AMOUNT: 결제 공급가액
   * - TRANSFER_PAYMENT_VAT_AMOUNT: 결제 부가세액
   * - TRANSFER_PAYMENT_TAX_FREE_AMOUNT: 결제 면세액
   * - TRANSFER_PAYMENT_VAT_BURDEN_AMOUNT: 결제 부가세 부담금
   * - TRANSFER_PLATFORM_FEE:  중개수수료
   * - TRANSFER_PLATFORM_FEE_VAT: 중개수수료 부가세 부담금
   * - TRANSFER_DISCOUNT_AMOUNT: 할인 금액
   * - TRANSFER_DISCOUNT_TAX_FREE_AMOUNT: 할인 면세액
   * - TRANSFER_DISCOUNT_SHARE_AMOUNT: 할인 분담금
   * - TRANSFER_DISCOUNT_SHARE_TAX_FREE_AMOUNT: 할인 면세 분담금
   * - TRANSFER_ADDITIONAL_FEE:  추가수수료
   * - TRANSFER_ADDITIONAL_FEE_VAT: 추가수수료 부가세 부담금
   * - TRANSFER_{UserDefinedProperty.Key}
   * - FORMULA_{UserDefinedFormula.Key}
   * - PARTNER_* : 파트너 컬럼 키 사용 가능(w/o PARTNER_STATUS_UPDATED_AT)
   * @param fields
   *
   *
   * @throws DownloadPlatformTransferSheetException
   */
  @JvmName("downloadPlatformTransferSheetSuspend")
  public suspend fun downloadPlatformTransferSheet(
    filter: PlatformTransferFilterInput? = null,
    fields: List<String>? = null,
  ): String {
    val requestBody = DownloadPlatformTransferSheetBody(
      filter = filter,
      fields = fields,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "transfer-summaries", "sheet-file")
        parameters.append("requestBody", json.encodeToString(requestBody))
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      accept(ContentType.Text.CSV)
      userAgent(USER_AGENT)
    }
    if (httpResponse.status.value !in 200..299) {
      val httpBody = httpResponse.body<String>()
      val httpBodyDecoded = try {
        json.decodeFromString<DownloadPlatformTransferSheetError.Recognized>(httpBody)
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
  public fun downloadPlatformTransferSheetFuture(
    filter: PlatformTransferFilterInput? = null,
    fields: List<String>? = null,
  ): CompletableFuture<String> = GlobalScope.future { downloadPlatformTransferSheet(filter, fields) }


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
   * @throws GetPlatformTransferSummariesException
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
        json.decodeFromString<GetPlatformTransferSummariesError.Recognized>(httpBody)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformTransferSummaries")
  public fun getPlatformTransferSummariesFuture(
    page: PageInput? = null,
    filter: PlatformTransferFilterInput? = null,
  ): CompletableFuture<GetPlatformTransferSummariesResponse> = GlobalScope.future { getPlatformTransferSummaries(page, filter) }


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
   * @param settlementTaxFreeAmount
   * 정산 면세 금액
   * @param settlementDate
   * 정산 일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   * @param isForTest
   * 테스트 모드 여부
   *
   * 기본값은 false 입니다.
   * @param userDefinedProperties
   * 사용자 정의 속성
   *
   * @throws CreatePlatformManualTransferException
   */
  @JvmName("createPlatformManualTransferSuspend")
  public suspend fun createPlatformManualTransfer(
    partnerId: String,
    memo: String? = null,
    settlementAmount: Long,
    settlementTaxFreeAmount: Long? = null,
    settlementDate: String,
    isForTest: Boolean? = null,
    userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>? = null,
  ): CreateManualTransferResponse {
    val requestBody = CreatePlatformManualTransferBody(
      partnerId = partnerId,
      memo = memo,
      settlementAmount = settlementAmount,
      settlementTaxFreeAmount = settlementTaxFreeAmount,
      settlementDate = settlementDate,
      isForTest = isForTest,
      userDefinedProperties = userDefinedProperties,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("platform", "transfers", "manual")
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
        json.decodeFromString<CreatePlatformManualTransferError.Recognized>(httpBody)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformManualTransfer")
  public fun createPlatformManualTransferFuture(
    partnerId: String,
    memo: String? = null,
    settlementAmount: Long,
    settlementTaxFreeAmount: Long? = null,
    settlementDate: String,
    isForTest: Boolean? = null,
    userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>? = null,
  ): CompletableFuture<CreateManualTransferResponse> = GlobalScope.future { createPlatformManualTransfer(partnerId, memo, settlementAmount, settlementTaxFreeAmount, settlementDate, isForTest, userDefinedProperties) }


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
   * (yyyy-MM-dd)
   * @param settlementDate
   * 정산일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
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
   * @throws CreatePlatformOrderTransferException
   */
  @JvmName("createPlatformOrderTransferSuspend")
  public suspend fun createPlatformOrderTransfer(
    partnerId: String,
    contractId: String? = null,
    memo: String? = null,
    paymentId: String,
    orderDetail: CreatePlatformOrderTransferBodyOrderDetail,
    taxFreeAmount: Long? = null,
    settlementStartDate: String? = null,
    settlementDate: String? = null,
    discounts: List<CreatePlatformOrderTransferBodyDiscount>,
    additionalFees: List<CreatePlatformOrderTransferBodyAdditionalFee>,
    externalPaymentDetail: CreatePlatformOrderTransferBodyExternalPaymentDetail? = null,
    isForTest: Boolean? = null,
    parameters: TransferParameters? = null,
    userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>? = null,
  ): CreateOrderTransferResponse {
    val requestBody = CreatePlatformOrderTransferBody(
      partnerId = partnerId,
      contractId = contractId,
      memo = memo,
      paymentId = paymentId,
      orderDetail = orderDetail,
      taxFreeAmount = taxFreeAmount,
      settlementStartDate = settlementStartDate,
      settlementDate = settlementDate,
      discounts = discounts,
      additionalFees = additionalFees,
      externalPaymentDetail = externalPaymentDetail,
      isForTest = isForTest,
      parameters = parameters,
      userDefinedProperties = userDefinedProperties,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("platform", "transfers", "order")
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
        json.decodeFromString<CreatePlatformOrderTransferError.Recognized>(httpBody)
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
        is PlatformSettlementDateEarlierThanSettlementStartDateError -> throw PlatformSettlementDateEarlierThanSettlementStartDateException(httpBodyDecoded)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformOrderTransfer")
  public fun createPlatformOrderTransferFuture(
    partnerId: String,
    contractId: String? = null,
    memo: String? = null,
    paymentId: String,
    orderDetail: CreatePlatformOrderTransferBodyOrderDetail,
    taxFreeAmount: Long? = null,
    settlementStartDate: String? = null,
    settlementDate: String? = null,
    discounts: List<CreatePlatformOrderTransferBodyDiscount>,
    additionalFees: List<CreatePlatformOrderTransferBodyAdditionalFee>,
    externalPaymentDetail: CreatePlatformOrderTransferBodyExternalPaymentDetail? = null,
    isForTest: Boolean? = null,
    parameters: TransferParameters? = null,
    userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>? = null,
  ): CompletableFuture<CreateOrderTransferResponse> = GlobalScope.future { createPlatformOrderTransfer(partnerId, contractId, memo, paymentId, orderDetail, taxFreeAmount, settlementStartDate, settlementDate, discounts, additionalFees, externalPaymentDetail, isForTest, parameters, userDefinedProperties) }


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
   * (yyyy-MM-dd)
   * @param settlementDate
   * 정산일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
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
   * @throws CreatePlatformOrderCancelTransferException
   */
  @JvmName("createPlatformOrderCancelTransferSuspend")
  public suspend fun createPlatformOrderCancelTransfer(
    partnerId: String? = null,
    paymentId: String? = null,
    transferId: String? = null,
    cancellationId: String,
    memo: String? = null,
    orderDetail: CreatePlatformOrderCancelTransferBodyOrderDetail? = null,
    taxFreeAmount: Long? = null,
    discounts: List<CreatePlatformOrderCancelTransferBodyDiscount>,
    settlementStartDate: String? = null,
    settlementDate: String? = null,
    externalCancellationDetail: CreatePlatformOrderCancelTransferBodyExternalCancellationDetail? = null,
    isForTest: Boolean? = null,
    userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>? = null,
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
      settlementDate = settlementDate,
      externalCancellationDetail = externalCancellationDetail,
      isForTest = isForTest,
      userDefinedProperties = userDefinedProperties,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("platform", "transfers", "order-cancel")
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
        json.decodeFromString<CreatePlatformOrderCancelTransferError.Recognized>(httpBody)
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
        is PlatformSettlementDateEarlierThanSettlementStartDateError -> throw PlatformSettlementDateEarlierThanSettlementStartDateException(httpBodyDecoded)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createPlatformOrderCancelTransfer")
  public fun createPlatformOrderCancelTransferFuture(
    partnerId: String? = null,
    paymentId: String? = null,
    transferId: String? = null,
    cancellationId: String,
    memo: String? = null,
    orderDetail: CreatePlatformOrderCancelTransferBodyOrderDetail? = null,
    taxFreeAmount: Long? = null,
    discounts: List<CreatePlatformOrderCancelTransferBodyDiscount>,
    settlementStartDate: String? = null,
    settlementDate: String? = null,
    externalCancellationDetail: CreatePlatformOrderCancelTransferBodyExternalCancellationDetail? = null,
    isForTest: Boolean? = null,
    userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>? = null,
  ): CompletableFuture<CreateOrderCancelTransferResponse> = GlobalScope.future { createPlatformOrderCancelTransfer(partnerId, paymentId, transferId, cancellationId, memo, orderDetail, taxFreeAmount, discounts, settlementStartDate, settlementDate, externalCancellationDetail, isForTest, userDefinedProperties) }


  /**
   * 정산건 조회
   *
   * 정산건을 조회합니다.
   *
   * @param id
   * 조회하고 싶은 정산건 아이디
   *
   * @throws GetPlatformTransferException
   */
  @JvmName("getPlatformTransferSuspend")
  public suspend fun getPlatformTransfer(
    id: String,
  ): PlatformTransfer {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("platform", "transfers", id.toString())
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
        json.decodeFromString<GetPlatformTransferError.Recognized>(httpBody)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPlatformTransfer")
  public fun getPlatformTransferFuture(
    id: String,
  ): CompletableFuture<PlatformTransfer> = GlobalScope.future { getPlatformTransfer(id) }


  /**
   * 정산건 삭제
   *
   * scheduled, in_process 상태의 정산건만 삭제가능합니다.
   *
   * @param id
   * 정산건 아이디
   *
   * @throws DeletePlatformTransferException
   */
  @JvmName("deletePlatformTransferSuspend")
  public suspend fun deletePlatformTransfer(
    id: String,
  ): DeletePlatformTransferResponse {
    val httpResponse = client.delete(apiBase) {
      url {
        appendPathSegments("platform", "transfers", id.toString())
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
        json.decodeFromString<DeletePlatformTransferError.Recognized>(httpBody)
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
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("deletePlatformTransfer")
  public fun deletePlatformTransferFuture(
    id: String,
  ): CompletableFuture<DeletePlatformTransferResponse> = GlobalScope.future { deletePlatformTransfer(id) }

  override fun close() {
    client.close()
  }
}
