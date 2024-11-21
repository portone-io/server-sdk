package io.portone.sdk.server.payment

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
import io.portone.sdk.server.common.BillingKeyPaymentInput
import io.portone.sdk.server.common.CashReceiptInput
import io.portone.sdk.server.common.Country
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.CustomerInput
import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.common.PaymentAmountInput
import io.portone.sdk.server.common.PaymentProduct
import io.portone.sdk.server.common.PaymentProductType
import io.portone.sdk.server.common.SeparatedAddressInput
import io.portone.sdk.server.errors.AlreadyPaidError
import io.portone.sdk.server.errors.AlreadyPaidException
import io.portone.sdk.server.errors.ApplyEscrowLogisticsError
import io.portone.sdk.server.errors.BillingKeyAlreadyDeletedError
import io.portone.sdk.server.errors.BillingKeyAlreadyDeletedException
import io.portone.sdk.server.errors.BillingKeyNotFoundError
import io.portone.sdk.server.errors.BillingKeyNotFoundException
import io.portone.sdk.server.errors.CancelAmountExceedsCancellableAmountError
import io.portone.sdk.server.errors.CancelAmountExceedsCancellableAmountException
import io.portone.sdk.server.errors.CancelPaymentError
import io.portone.sdk.server.errors.CancelTaxAmountExceedsCancellableTaxAmountError
import io.portone.sdk.server.errors.CancelTaxAmountExceedsCancellableTaxAmountException
import io.portone.sdk.server.errors.CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError
import io.portone.sdk.server.errors.CancelTaxFreeAmountExceedsCancellableTaxFreeAmountException
import io.portone.sdk.server.errors.CancellableAmountConsistencyBrokenError
import io.portone.sdk.server.errors.CancellableAmountConsistencyBrokenException
import io.portone.sdk.server.errors.ChannelNotFoundError
import io.portone.sdk.server.errors.ChannelNotFoundException
import io.portone.sdk.server.errors.CloseVirtualAccountError
import io.portone.sdk.server.errors.ConfirmEscrowError
import io.portone.sdk.server.errors.DiscountAmountExceedsTotalAmountError
import io.portone.sdk.server.errors.DiscountAmountExceedsTotalAmountException
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetAllPaymentsError
import io.portone.sdk.server.errors.GetPaymentError
import io.portone.sdk.server.errors.GetPaymentsError
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.MaxTransactionCountReachedError
import io.portone.sdk.server.errors.MaxTransactionCountReachedException
import io.portone.sdk.server.errors.MaxWebhookRetryCountReachedError
import io.portone.sdk.server.errors.MaxWebhookRetryCountReachedException
import io.portone.sdk.server.errors.ModifyEscrowLogisticsError
import io.portone.sdk.server.errors.NegativePromotionAdjustedCancelAmountError
import io.portone.sdk.server.errors.NegativePromotionAdjustedCancelAmountException
import io.portone.sdk.server.errors.PayInstantlyError
import io.portone.sdk.server.errors.PayWithBillingKeyError
import io.portone.sdk.server.errors.PaymentAlreadyCancelledError
import io.portone.sdk.server.errors.PaymentAlreadyCancelledException
import io.portone.sdk.server.errors.PaymentNotFoundError
import io.portone.sdk.server.errors.PaymentNotFoundException
import io.portone.sdk.server.errors.PaymentNotPaidError
import io.portone.sdk.server.errors.PaymentNotPaidException
import io.portone.sdk.server.errors.PaymentNotWaitingForDepositError
import io.portone.sdk.server.errors.PaymentNotWaitingForDepositException
import io.portone.sdk.server.errors.PaymentScheduleAlreadyExistsError
import io.portone.sdk.server.errors.PaymentScheduleAlreadyExistsException
import io.portone.sdk.server.errors.PgProviderError
import io.portone.sdk.server.errors.PgProviderException
import io.portone.sdk.server.errors.PreRegisterPaymentError
import io.portone.sdk.server.errors.PromotionDiscountRetainOptionShouldNotBeChangedError
import io.portone.sdk.server.errors.PromotionDiscountRetainOptionShouldNotBeChangedException
import io.portone.sdk.server.errors.PromotionPayMethodDoesNotMatchError
import io.portone.sdk.server.errors.PromotionPayMethodDoesNotMatchException
import io.portone.sdk.server.errors.RegisterStoreReceiptError
import io.portone.sdk.server.errors.ResendWebhookError
import io.portone.sdk.server.errors.SumOfPartsExceedsCancelAmountError
import io.portone.sdk.server.errors.SumOfPartsExceedsCancelAmountException
import io.portone.sdk.server.errors.SumOfPartsExceedsTotalAmountError
import io.portone.sdk.server.errors.SumOfPartsExceedsTotalAmountException
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.errors.WebhookNotFoundError
import io.portone.sdk.server.errors.WebhookNotFoundException
import io.portone.sdk.server.payment.ApplyEscrowLogisticsResponse
import io.portone.sdk.server.payment.CancelPaymentBody
import io.portone.sdk.server.payment.CancelPaymentBodyRefundAccount
import io.portone.sdk.server.payment.CancelPaymentResponse
import io.portone.sdk.server.payment.CancelRequester
import io.portone.sdk.server.payment.CloseVirtualAccountResponse
import io.portone.sdk.server.payment.ConfirmEscrowBody
import io.portone.sdk.server.payment.ConfirmEscrowResponse
import io.portone.sdk.server.payment.GetAllPaymentsByCursorBody
import io.portone.sdk.server.payment.GetAllPaymentsByCursorResponse
import io.portone.sdk.server.payment.GetPaymentsBody
import io.portone.sdk.server.payment.GetPaymentsResponse
import io.portone.sdk.server.payment.InstantPaymentInput
import io.portone.sdk.server.payment.InstantPaymentMethodInput
import io.portone.sdk.server.payment.ModifyEscrowLogisticsBody
import io.portone.sdk.server.payment.ModifyEscrowLogisticsResponse
import io.portone.sdk.server.payment.PayInstantlyResponse
import io.portone.sdk.server.payment.PayWithBillingKeyResponse
import io.portone.sdk.server.payment.Payment
import io.portone.sdk.server.payment.PaymentEscrowReceiverInput
import io.portone.sdk.server.payment.PaymentEscrowSenderInput
import io.portone.sdk.server.payment.PaymentFilterInput
import io.portone.sdk.server.payment.PaymentLogistics
import io.portone.sdk.server.payment.PreRegisterPaymentBody
import io.portone.sdk.server.payment.PreRegisterPaymentResponse
import io.portone.sdk.server.payment.PromotionDiscountRetainOption
import io.portone.sdk.server.payment.RegisterEscrowLogisticsBody
import io.portone.sdk.server.payment.RegisterStoreReceiptBody
import io.portone.sdk.server.payment.RegisterStoreReceiptBodyItem
import io.portone.sdk.server.payment.RegisterStoreReceiptResponse
import io.portone.sdk.server.payment.ResendWebhookBody
import io.portone.sdk.server.payment.ResendWebhookResponse
import io.portone.sdk.server.payment.billingkey.BillingKeyClient
import io.portone.sdk.server.payment.cashreceipt.CashReceiptClient
import io.portone.sdk.server.payment.paymentschedule.PaymentScheduleClient
import io.portone.sdk.server.payment.promotion.PromotionClient
import java.io.Closeable
import java.time.Instant
import java.util.concurrent.CompletableFuture
import kotlin.Array
import kotlin.String
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import kotlinx.serialization.json.JsonObject

public class PaymentClient(
  private val apiSecret: String,
  private val apiBase: String = "https://api.portone.io",
  private val storeId: String? = null,
): Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 결제 정보 사전 등록
   *
   * 결제 정보를 사전 등록합니다.
   *
   * @param paymentId
   * 결제 건 아이디
   * @param totalAmount
   * 결제 총 금액
   * @param taxFreeAmount
   * 결제 면세 금액
   * @param currency
   * 통화 단위
   *
   * @throws PreRegisterPaymentException
   */
  @JvmName("preRegisterPaymentSuspend")
  public suspend fun preRegisterPayment(
    paymentId: String,
    totalAmount: Long? = null,
    taxFreeAmount: Long? = null,
    currency: Currency? = null,
  ): PreRegisterPaymentResponse {
    val requestBody = PreRegisterPaymentBody(
      storeId = storeId,
      totalAmount = totalAmount,
      taxFreeAmount = taxFreeAmount,
      currency = currency,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("payments", paymentId.toString(), "pre-register")
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
        json.decodeFromString<PreRegisterPaymentError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is AlreadyPaidError -> throw AlreadyPaidException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
        else -> throw UnknownException("Unknown API error: $httpBody")
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PreRegisterPaymentResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("preRegisterPayment")
  public fun preRegisterPaymentFuture(
    paymentId: String,
    totalAmount: Long? = null,
    taxFreeAmount: Long? = null,
    currency: Currency? = null,
  ): CompletableFuture<PreRegisterPaymentResponse> = GlobalScope.future { preRegisterPayment(paymentId, totalAmount, taxFreeAmount, currency) }


  /**
   * 결제 단건 조회
   *
   * 주어진 아이디에 대응되는 결제 건을 조회합니다.
   *
   * @param paymentId
   * 조회할 결제 아이디
   *
   * @throws GetPaymentException
   */
  @JvmName("getPaymentSuspend")
  public suspend fun getPayment(
    paymentId: String,
  ): Payment {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("payments", paymentId.toString())
        if (storeId != null) parameters.append("storeId", storeId.toString())
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
        json.decodeFromString<GetPaymentError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PaymentNotFoundError -> throw PaymentNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
        else -> throw UnknownException("Unknown API error: $httpBody")
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<Payment>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPayment")
  public fun getPaymentFuture(
    paymentId: String,
  ): CompletableFuture<Payment> = GlobalScope.future { getPayment(paymentId) }


  /**
   * 결제 다건 조회(페이지 기반)
   *
   * 주어진 조건에 맞는 결제 건들을 페이지 기반으로 조회합니다.
   *
   * @param page
   * 요청할 페이지 정보
   *
   * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
   * @param filter
   * 조회할 결제 건 조건 필터
   *
   * V1 결제 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.
   *
   * @throws GetPaymentsException
   */
  @JvmName("getPaymentsSuspend")
  public suspend fun getPayments(
    page: PageInput? = null,
    filter: PaymentFilterInput? = null,
  ): GetPaymentsResponse {
    val requestBody = GetPaymentsBody(
      page = page,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("payments")
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
        json.decodeFromString<GetPaymentsError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
        else -> throw UnknownException("Unknown API error: $httpBody")
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetPaymentsResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getPayments")
  public fun getPaymentsFuture(
    page: PageInput? = null,
    filter: PaymentFilterInput? = null,
  ): CompletableFuture<GetPaymentsResponse> = GlobalScope.future { getPayments(page, filter) }


  /**
   * 결제 대용량 다건 조회(커서 기반)
   *
   * 기간 내 모든 결제 건을 커서 기반으로 조회합니다. 결제 건의 생성일시를 기준으로 주어진 기간 내 존재하는 모든 결제 건이 조회됩니다.
   *
   * @param from
   * 결제 건 생성시점 범위 조건의 시작
   *
   * 값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
   * @param until
   * 결제 건 생성시점 범위 조건의 끝
   *
   * 값을 입력하지 않으면 현재 시점으로 설정됩니다.
   * @param cursor
   * 커서
   *
   * 결제 건 리스트 중 어디서부터 읽어야 할지 가리키는 값입니다. 최초 요청일 경우 값을 입력하지 마시되, 두번째 요청 부터는 이전 요청 응답값의 cursor를 입력해주시면 됩니다.
   * @param size
   * 페이지 크기
   *
   * 미입력 시 기본값은 10 이며 최대 1000까지 허용
   *
   * @throws GetAllPaymentsException
   */
  @JvmName("getAllPaymentsByCursorSuspend")
  public suspend fun getAllPaymentsByCursor(
    `from`: Instant? = null,
    until: Instant? = null,
    cursor: String? = null,
    size: Int? = null,
  ): GetAllPaymentsByCursorResponse {
    val requestBody = GetAllPaymentsByCursorBody(
      storeId = storeId,
      from = from,
      until = until,
      cursor = cursor,
      size = size,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("payments-by-cursor")
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
        json.decodeFromString<GetAllPaymentsError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
        else -> throw UnknownException("Unknown API error: $httpBody")
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetAllPaymentsByCursorResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getAllPaymentsByCursor")
  public fun getAllPaymentsByCursorFuture(
    `from`: Instant? = null,
    until: Instant? = null,
    cursor: String? = null,
    size: Int? = null,
  ): CompletableFuture<GetAllPaymentsByCursorResponse> = GlobalScope.future { getAllPaymentsByCursor(from, until, cursor, size) }


  /**
   * 결제 취소
   *
   * 결제 취소를 요청합니다.
   *
   * @param paymentId
   * 결제 건 아이디
   * @param amount
   * 취소 총 금액
   *
   * 값을 입력하지 않으면 전액 취소됩니다.
   * @param taxFreeAmount
   * 취소 금액 중 면세 금액
   *
   * 값을 입력하지 않으면 전액 과세 취소됩니다.
   * @param vatAmount
   * 취소 금액 중 부가세액
   *
   * 값을 입력하지 않으면 자동 계산됩니다.
   * @param reason
   * 취소 사유
   * @param requester
   * 취소 요청자
   *
   * 고객에 의한 취소일 경우 Customer, 관리자에 의한 취소일 경우 Admin으로 입력합니다.
   * @param promotionDiscountRetainOption
   * 프로모션 할인율 유지 옵션
   *
   * 프로모션이 적용된 결제를 부분 취소하는 경우, 최초 할인율을 유지할지 여부를 선택할 수 있습니다.
   * RETAIN 으로 설정 시, 최초 할인율을 유지할 수 있도록 취소 금액이 조정됩니다.
   * RELEASE 으로 설정 시, 취소 후 남은 금액이 속한 구간에 맞게 프로모션 할인이 새롭게 적용됩니다.
   * 값을 입력하지 않으면 RELEASE 로 취급합니다.
   * @param currentCancellableAmount
   * 결제 건의 취소 가능 잔액
   *
   * 본 취소 요청 이전의 취소 가능 잔액으로써, 값을 입력하면 잔액이 일치하는 경우에만 취소가 진행됩니다. 값을 입력하지 않으면 별도의 검증 처리를 수행하지 않습니다.
   * @param refundAccount
   * 환불 계좌
   *
   * 계좌 환불일 경우 입력합니다. 계좌 환불이 필요한 경우는 가상계좌 환불, 휴대폰 익월 환불 등이 있습니다.
   *
   * @throws CancelPaymentException
   */
  @JvmName("cancelPaymentSuspend")
  public suspend fun cancelPayment(
    paymentId: String,
    amount: Long? = null,
    taxFreeAmount: Long? = null,
    vatAmount: Long? = null,
    reason: String,
    requester: CancelRequester? = null,
    promotionDiscountRetainOption: PromotionDiscountRetainOption? = null,
    currentCancellableAmount: Long? = null,
    refundAccount: CancelPaymentBodyRefundAccount? = null,
  ): CancelPaymentResponse {
    val requestBody = CancelPaymentBody(
      storeId = storeId,
      amount = amount,
      taxFreeAmount = taxFreeAmount,
      vatAmount = vatAmount,
      reason = reason,
      requester = requester,
      promotionDiscountRetainOption = promotionDiscountRetainOption,
      currentCancellableAmount = currentCancellableAmount,
      refundAccount = refundAccount,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("payments", paymentId.toString(), "cancel")
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
        json.decodeFromString<CancelPaymentError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is CancellableAmountConsistencyBrokenError -> throw CancellableAmountConsistencyBrokenException(httpBodyDecoded)
        is CancelAmountExceedsCancellableAmountError -> throw CancelAmountExceedsCancellableAmountException(httpBodyDecoded)
        is CancelTaxAmountExceedsCancellableTaxAmountError -> throw CancelTaxAmountExceedsCancellableTaxAmountException(httpBodyDecoded)
        is CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError -> throw CancelTaxFreeAmountExceedsCancellableTaxFreeAmountException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is NegativePromotionAdjustedCancelAmountError -> throw NegativePromotionAdjustedCancelAmountException(httpBodyDecoded)
        is PaymentAlreadyCancelledError -> throw PaymentAlreadyCancelledException(httpBodyDecoded)
        is PaymentNotFoundError -> throw PaymentNotFoundException(httpBodyDecoded)
        is PaymentNotPaidError -> throw PaymentNotPaidException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is PromotionDiscountRetainOptionShouldNotBeChangedError -> throw PromotionDiscountRetainOptionShouldNotBeChangedException(httpBodyDecoded)
        is SumOfPartsExceedsCancelAmountError -> throw SumOfPartsExceedsCancelAmountException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
        else -> throw UnknownException("Unknown API error: $httpBody")
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CancelPaymentResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("cancelPayment")
  public fun cancelPaymentFuture(
    paymentId: String,
    amount: Long? = null,
    taxFreeAmount: Long? = null,
    vatAmount: Long? = null,
    reason: String,
    requester: CancelRequester? = null,
    promotionDiscountRetainOption: PromotionDiscountRetainOption? = null,
    currentCancellableAmount: Long? = null,
    refundAccount: CancelPaymentBodyRefundAccount? = null,
  ): CompletableFuture<CancelPaymentResponse> = GlobalScope.future { cancelPayment(paymentId, amount, taxFreeAmount, vatAmount, reason, requester, promotionDiscountRetainOption, currentCancellableAmount, refundAccount) }


  /**
   * 빌링키 결제
   *
   * 빌링키로 결제를 진행합니다.
   *
   * @param paymentId
   * 결제 건 아이디
   * @param billingKey
   * 빌링키 결제에 사용할 빌링키
   * @param channelKey
   * 채널 키
   *
   * 다수 채널에 대해 발급된 빌링키에 대해, 결제 채널을 특정하고 싶을 때 명시
   * @param orderName
   * 주문명
   * @param customer
   * 고객 정보
   * @param customData
   * 사용자 지정 데이터
   * @param amount
   * 결제 금액 세부 입력 정보
   * @param currency
   * 통화
   * @param installmentMonth
   * 할부 개월 수
   * @param useFreeInterestFromMerchant
   * 무이자 할부 이자를 고객사가 부담할지 여부
   * @param useCardPoint
   * 카드 포인트 사용 여부
   * @param cashReceipt
   * 현금영수증 정보
   * @param country
   * 결제 국가
   * @param noticeUrls
   * 웹훅 주소
   *
   * 결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
   * 상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
   * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
   * @param products
   * 상품 정보
   *
   * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
   * @param productCount
   * 상품 개수
   * @param productType
   * 상품 유형
   * @param shippingAddress
   * 배송지 주소
   * @param promotionId
   * 해당 결제에 적용할 프로모션 아이디
   * @param bypass
   * PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)
   *
   * @throws PayWithBillingKeyException
   */
  @JvmName("payWithBillingKeySuspend")
  public suspend fun payWithBillingKey(
    paymentId: String,
    billingKey: String,
    channelKey: String? = null,
    orderName: String,
    customer: CustomerInput? = null,
    customData: String? = null,
    amount: PaymentAmountInput,
    currency: Currency,
    installmentMonth: Int? = null,
    useFreeInterestFromMerchant: Boolean? = null,
    useCardPoint: Boolean? = null,
    cashReceipt: CashReceiptInput? = null,
    country: Country? = null,
    noticeUrls: List<String>? = null,
    products: List<PaymentProduct>? = null,
    productCount: Int? = null,
    productType: PaymentProductType? = null,
    shippingAddress: SeparatedAddressInput? = null,
    promotionId: String? = null,
    bypass: JsonObject? = null,
  ): PayWithBillingKeyResponse {
    val requestBody = BillingKeyPaymentInput(
      storeId = storeId,
      billingKey = billingKey,
      channelKey = channelKey,
      orderName = orderName,
      customer = customer,
      customData = customData,
      amount = amount,
      currency = currency,
      installmentMonth = installmentMonth,
      useFreeInterestFromMerchant = useFreeInterestFromMerchant,
      useCardPoint = useCardPoint,
      cashReceipt = cashReceipt,
      country = country,
      noticeUrls = noticeUrls,
      products = products,
      productCount = productCount,
      productType = productType,
      shippingAddress = shippingAddress,
      promotionId = promotionId,
      bypass = bypass,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("payments", paymentId.toString(), "billing-key")
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
        json.decodeFromString<PayWithBillingKeyError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is AlreadyPaidError -> throw AlreadyPaidException(httpBodyDecoded)
        is BillingKeyAlreadyDeletedError -> throw BillingKeyAlreadyDeletedException(httpBodyDecoded)
        is BillingKeyNotFoundError -> throw BillingKeyNotFoundException(httpBodyDecoded)
        is ChannelNotFoundError -> throw ChannelNotFoundException(httpBodyDecoded)
        is DiscountAmountExceedsTotalAmountError -> throw DiscountAmountExceedsTotalAmountException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is MaxTransactionCountReachedError -> throw MaxTransactionCountReachedException(httpBodyDecoded)
        is PaymentScheduleAlreadyExistsError -> throw PaymentScheduleAlreadyExistsException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is PromotionPayMethodDoesNotMatchError -> throw PromotionPayMethodDoesNotMatchException(httpBodyDecoded)
        is SumOfPartsExceedsTotalAmountError -> throw SumOfPartsExceedsTotalAmountException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
        else -> throw UnknownException("Unknown API error: $httpBody")
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PayWithBillingKeyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("payWithBillingKey")
  public fun payWithBillingKeyFuture(
    paymentId: String,
    billingKey: String,
    channelKey: String? = null,
    orderName: String,
    customer: CustomerInput? = null,
    customData: String? = null,
    amount: PaymentAmountInput,
    currency: Currency,
    installmentMonth: Int? = null,
    useFreeInterestFromMerchant: Boolean? = null,
    useCardPoint: Boolean? = null,
    cashReceipt: CashReceiptInput? = null,
    country: Country? = null,
    noticeUrls: List<String>? = null,
    products: List<PaymentProduct>? = null,
    productCount: Int? = null,
    productType: PaymentProductType? = null,
    shippingAddress: SeparatedAddressInput? = null,
    promotionId: String? = null,
    bypass: JsonObject? = null,
  ): CompletableFuture<PayWithBillingKeyResponse> = GlobalScope.future { payWithBillingKey(paymentId, billingKey, channelKey, orderName, customer, customData, amount, currency, installmentMonth, useFreeInterestFromMerchant, useCardPoint, cashReceipt, country, noticeUrls, products, productCount, productType, shippingAddress, promotionId, bypass) }


  /**
   * 수기 결제
   *
   * 수기 결제를 진행합니다.
   *
   * @param paymentId
   * 결제 건 아이디
   * @param channelKey
   * 채널 키
   *
   * 채널 키 또는 채널 그룹 ID 필수
   * @param channelGroupId
   * 채널 그룹 ID
   *
   * 채널 키 또는 채널 그룹 ID 필수
   * @param method
   * 결제수단 정보
   * @param orderName
   * 주문명
   * @param isCulturalExpense
   * 문화비 지출 여부
   *
   * 기본값은 false 입니다.
   * @param isEscrow
   * 에스크로 결제 여부
   *
   * 기본값은 false 입니다.
   * @param customer
   * 고객 정보
   * @param customData
   * 사용자 지정 데이터
   * @param amount
   * 결제 금액 세부 입력 정보
   * @param currency
   * 통화
   * @param country
   * 결제 국가
   * @param noticeUrls
   * 웹훅 주소
   *
   * 결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
   * 상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
   * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
   * @param products
   * 상품 정보
   *
   * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
   * @param productCount
   * 상품 개수
   * @param productType
   * 상품 유형
   * @param shippingAddress
   * 배송지 주소
   * @param promotionId
   * 해당 결제에 적용할 프로모션 아이디
   *
   * @throws PayInstantlyException
   */
  @JvmName("payInstantlySuspend")
  public suspend fun payInstantly(
    paymentId: String,
    channelKey: String? = null,
    channelGroupId: String? = null,
    method: InstantPaymentMethodInput,
    orderName: String,
    isCulturalExpense: Boolean? = null,
    isEscrow: Boolean? = null,
    customer: CustomerInput? = null,
    customData: String? = null,
    amount: PaymentAmountInput,
    currency: Currency,
    country: Country? = null,
    noticeUrls: List<String>? = null,
    products: List<PaymentProduct>? = null,
    productCount: Int? = null,
    productType: PaymentProductType? = null,
    shippingAddress: SeparatedAddressInput? = null,
    promotionId: String? = null,
  ): PayInstantlyResponse {
    val requestBody = InstantPaymentInput(
      storeId = storeId,
      channelKey = channelKey,
      channelGroupId = channelGroupId,
      method = method,
      orderName = orderName,
      isCulturalExpense = isCulturalExpense,
      isEscrow = isEscrow,
      customer = customer,
      customData = customData,
      amount = amount,
      currency = currency,
      country = country,
      noticeUrls = noticeUrls,
      products = products,
      productCount = productCount,
      productType = productType,
      shippingAddress = shippingAddress,
      promotionId = promotionId,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("payments", paymentId.toString(), "instant")
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
        json.decodeFromString<PayInstantlyError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is AlreadyPaidError -> throw AlreadyPaidException(httpBodyDecoded)
        is ChannelNotFoundError -> throw ChannelNotFoundException(httpBodyDecoded)
        is DiscountAmountExceedsTotalAmountError -> throw DiscountAmountExceedsTotalAmountException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is MaxTransactionCountReachedError -> throw MaxTransactionCountReachedException(httpBodyDecoded)
        is PaymentScheduleAlreadyExistsError -> throw PaymentScheduleAlreadyExistsException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is PromotionPayMethodDoesNotMatchError -> throw PromotionPayMethodDoesNotMatchException(httpBodyDecoded)
        is SumOfPartsExceedsTotalAmountError -> throw SumOfPartsExceedsTotalAmountException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
        else -> throw UnknownException("Unknown API error: $httpBody")
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<PayInstantlyResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("payInstantly")
  public fun payInstantlyFuture(
    paymentId: String,
    channelKey: String? = null,
    channelGroupId: String? = null,
    method: InstantPaymentMethodInput,
    orderName: String,
    isCulturalExpense: Boolean? = null,
    isEscrow: Boolean? = null,
    customer: CustomerInput? = null,
    customData: String? = null,
    amount: PaymentAmountInput,
    currency: Currency,
    country: Country? = null,
    noticeUrls: List<String>? = null,
    products: List<PaymentProduct>? = null,
    productCount: Int? = null,
    productType: PaymentProductType? = null,
    shippingAddress: SeparatedAddressInput? = null,
    promotionId: String? = null,
  ): CompletableFuture<PayInstantlyResponse> = GlobalScope.future { payInstantly(paymentId, channelKey, channelGroupId, method, orderName, isCulturalExpense, isEscrow, customer, customData, amount, currency, country, noticeUrls, products, productCount, productType, shippingAddress, promotionId) }


  /**
   * 가상계좌 말소
   *
   * 발급된 가상계좌를 말소합니다.
   *
   * @param paymentId
   * 결제 건 아이디
   *
   * @throws CloseVirtualAccountException
   */
  @JvmName("closeVirtualAccountSuspend")
  public suspend fun closeVirtualAccount(
    paymentId: String,
  ): CloseVirtualAccountResponse {
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("payments", paymentId.toString(), "virtual-account", "close")
        if (storeId != null) parameters.append("storeId", storeId.toString())
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
        json.decodeFromString<CloseVirtualAccountError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PaymentNotFoundError -> throw PaymentNotFoundException(httpBodyDecoded)
        is PaymentNotWaitingForDepositError -> throw PaymentNotWaitingForDepositException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
        else -> throw UnknownException("Unknown API error: $httpBody")
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CloseVirtualAccountResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("closeVirtualAccount")
  public fun closeVirtualAccountFuture(
    paymentId: String,
  ): CompletableFuture<CloseVirtualAccountResponse> = GlobalScope.future { closeVirtualAccount(paymentId) }


  /**
   * 에스크로 배송 정보 등록
   *
   * 에스크로 배송 정보를 등록합니다.
   *
   * @param paymentId
   * 결제 건 아이디
   * @param sender
   * 에스크로 발송자 정보
   * @param receiver
   * 에스크로 수취인 정보
   * @param logistics
   * 에스크로 물류 정보
   * @param sendEmail
   * 이메일 알림 전송 여부
   *
   * 에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
   * @param products
   * 상품 정보
   *
   * @throws ApplyEscrowLogisticsException
   */
  @JvmName("applyEscrowLogisticsSuspend")
  public suspend fun applyEscrowLogistics(
    paymentId: String,
    sender: PaymentEscrowSenderInput? = null,
    receiver: PaymentEscrowReceiverInput? = null,
    logistics: PaymentLogistics,
    sendEmail: Boolean? = null,
    products: List<PaymentProduct>? = null,
  ): ApplyEscrowLogisticsResponse {
    val requestBody = RegisterEscrowLogisticsBody(
      storeId = storeId,
      sender = sender,
      receiver = receiver,
      logistics = logistics,
      sendEmail = sendEmail,
      products = products,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("payments", paymentId.toString(), "escrow", "logistics")
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
        json.decodeFromString<ApplyEscrowLogisticsError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PaymentNotFoundError -> throw PaymentNotFoundException(httpBodyDecoded)
        is PaymentNotPaidError -> throw PaymentNotPaidException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
        else -> throw UnknownException("Unknown API error: $httpBody")
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ApplyEscrowLogisticsResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("applyEscrowLogistics")
  public fun applyEscrowLogisticsFuture(
    paymentId: String,
    sender: PaymentEscrowSenderInput? = null,
    receiver: PaymentEscrowReceiverInput? = null,
    logistics: PaymentLogistics,
    sendEmail: Boolean? = null,
    products: List<PaymentProduct>? = null,
  ): CompletableFuture<ApplyEscrowLogisticsResponse> = GlobalScope.future { applyEscrowLogistics(paymentId, sender, receiver, logistics, sendEmail, products) }


  /**
   * 에스크로 배송 정보 수정
   *
   * 에스크로 배송 정보를 수정합니다.
   *
   * @param paymentId
   * 결제 건 아이디
   * @param sender
   * 에스크로 발송자 정보
   * @param receiver
   * 에스크로 수취인 정보
   * @param logistics
   * 에스크로 물류 정보
   * @param sendEmail
   * 이메일 알림 전송 여부
   *
   * 에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
   * @param products
   * 상품 정보
   *
   * @throws ModifyEscrowLogisticsException
   */
  @JvmName("modifyEscrowLogisticsSuspend")
  public suspend fun modifyEscrowLogistics(
    paymentId: String,
    sender: PaymentEscrowSenderInput? = null,
    receiver: PaymentEscrowReceiverInput? = null,
    logistics: PaymentLogistics,
    sendEmail: Boolean? = null,
    products: List<PaymentProduct>? = null,
  ): ModifyEscrowLogisticsResponse {
    val requestBody = ModifyEscrowLogisticsBody(
      storeId = storeId,
      sender = sender,
      receiver = receiver,
      logistics = logistics,
      sendEmail = sendEmail,
      products = products,
    )
    val httpResponse = client.patch(apiBase) {
      url {
        appendPathSegments("payments", paymentId.toString(), "escrow", "logistics")
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
        json.decodeFromString<ModifyEscrowLogisticsError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PaymentNotFoundError -> throw PaymentNotFoundException(httpBodyDecoded)
        is PaymentNotPaidError -> throw PaymentNotPaidException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
        else -> throw UnknownException("Unknown API error: $httpBody")
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ModifyEscrowLogisticsResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("modifyEscrowLogistics")
  public fun modifyEscrowLogisticsFuture(
    paymentId: String,
    sender: PaymentEscrowSenderInput? = null,
    receiver: PaymentEscrowReceiverInput? = null,
    logistics: PaymentLogistics,
    sendEmail: Boolean? = null,
    products: List<PaymentProduct>? = null,
  ): CompletableFuture<ModifyEscrowLogisticsResponse> = GlobalScope.future { modifyEscrowLogistics(paymentId, sender, receiver, logistics, sendEmail, products) }


  /**
   * 에스크로 구매 확정
   *
   * 에스크로 결제를 구매 확정 처리합니다
   *
   * @param paymentId
   * 결제 건 아이디
   * @param fromStore
   * 확인 주체가 상점인지 여부
   *
   * 구매확정요청 주체가 고객사 관리자인지 구매자인지 구분하기 위한 필드입니다.
   * 네이버페이 전용 파라미터이며, 구분이 모호한 경우 고객사 관리자(true)로 입력합니다.
   *
   * @throws ConfirmEscrowException
   */
  @JvmName("confirmEscrowSuspend")
  public suspend fun confirmEscrow(
    paymentId: String,
    fromStore: Boolean? = null,
  ): ConfirmEscrowResponse {
    val requestBody = ConfirmEscrowBody(
      storeId = storeId,
      fromStore = fromStore,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("payments", paymentId.toString(), "escrow", "complete")
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
        json.decodeFromString<ConfirmEscrowError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PaymentNotFoundError -> throw PaymentNotFoundException(httpBodyDecoded)
        is PaymentNotPaidError -> throw PaymentNotPaidException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
        else -> throw UnknownException("Unknown API error: $httpBody")
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ConfirmEscrowResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("confirmEscrow")
  public fun confirmEscrowFuture(
    paymentId: String,
    fromStore: Boolean? = null,
  ): CompletableFuture<ConfirmEscrowResponse> = GlobalScope.future { confirmEscrow(paymentId, fromStore) }


  /**
   * 웹훅 재발송
   *
   * 웹훅을 재발송합니다.
   *
   * @param paymentId
   * 결제 건 아이디
   * @param webhookId
   * 웹훅 아이디
   *
   * 입력하지 않으면 결제 건의 가장 최근 웹훅 아이디가 기본 적용됩니다
   *
   * @throws ResendWebhookException
   */
  @JvmName("resendWebhookSuspend")
  public suspend fun resendWebhook(
    paymentId: String,
    webhookId: String? = null,
  ): ResendWebhookResponse {
    val requestBody = ResendWebhookBody(
      storeId = storeId,
      webhookId = webhookId,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("payments", paymentId.toString(), "resend-webhook")
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
        json.decodeFromString<ResendWebhookError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is MaxWebhookRetryCountReachedError -> throw MaxWebhookRetryCountReachedException(httpBodyDecoded)
        is PaymentNotFoundError -> throw PaymentNotFoundException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
        is WebhookNotFoundError -> throw WebhookNotFoundException(httpBodyDecoded)
        else -> throw UnknownException("Unknown API error: $httpBody")
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<ResendWebhookResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("resendWebhook")
  public fun resendWebhookFuture(
    paymentId: String,
    webhookId: String? = null,
  ): CompletableFuture<ResendWebhookResponse> = GlobalScope.future { resendWebhook(paymentId, webhookId) }


  /**
   * 영수증 내 하위 상점 거래 등록
   *
   * 결제 내역 매출전표에 하위 상점의 거래를 등록합니다.
   * 지원되는 PG사:
   * KG이니시스(이용 전 콘솔 -> 결제연동 탭에서 INIApi Key 등록 필요)
   *
   * @param paymentId
   * 등록할 하위 상점 결제 건 아이디
   * @param items
   * 하위 상점 거래 목록
   *
   * @throws RegisterStoreReceiptException
   */
  @JvmName("registerStoreReceiptSuspend")
  public suspend fun registerStoreReceipt(
    paymentId: String,
    items: List<RegisterStoreReceiptBodyItem>,
  ): RegisterStoreReceiptResponse {
    val requestBody = RegisterStoreReceiptBody(
      items = items,
      storeId = storeId,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("payments", paymentId.toString(), "register-store-receipt")
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
        json.decodeFromString<RegisterStoreReceiptError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is PaymentNotFoundError -> throw PaymentNotFoundException(httpBodyDecoded)
        is PaymentNotPaidError -> throw PaymentNotPaidException(httpBodyDecoded)
        is PgProviderError -> throw PgProviderException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
        else -> throw UnknownException("Unknown API error: $httpBody")
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<RegisterStoreReceiptResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("registerStoreReceipt")
  public fun registerStoreReceiptFuture(
    paymentId: String,
    items: List<RegisterStoreReceiptBodyItem>,
  ): CompletableFuture<RegisterStoreReceiptResponse> = GlobalScope.future { registerStoreReceipt(paymentId, items) }

  public val billingKey: BillingKeyClient = BillingKeyClient(apiSecret, apiBase, storeId)
  public val cashReceipt: CashReceiptClient = CashReceiptClient(apiSecret, apiBase, storeId)
  public val paymentSchedule: PaymentScheduleClient = PaymentScheduleClient(apiSecret, apiBase, storeId)
  public val promotion: PromotionClient = PromotionClient(apiSecret, apiBase, storeId)
  override fun close() {
    billingKey.close()
    cashReceipt.close()
    paymentSchedule.close()
    promotion.close()
    client.close()
  }
}
