package io.portone.sdk.server.b2b.taxinvoice

import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.okhttp.OkHttp
import io.ktor.client.request.`get`
import io.ktor.client.request.accept
import io.ktor.client.request.delete
import io.ktor.client.request.headers
import io.ktor.client.request.post
import io.ktor.client.request.put
import io.ktor.client.request.setBody
import io.ktor.http.ContentType
import io.ktor.http.HttpHeaders
import io.ktor.http.appendPathSegments
import io.ktor.http.contentType
import io.ktor.http.userAgent
import io.portone.sdk.server.USER_AGENT
import io.portone.sdk.server.b2b.taxinvoice.AttachB2bTaxInvoiceFileBody
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoice
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceInput
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceKeyType
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceModificationCreateBody
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceModificationUpdateBody
import io.portone.sdk.server.b2b.taxinvoice.CancelB2bTaxInvoiceIssuanceBody
import io.portone.sdk.server.b2b.taxinvoice.CancelB2bTaxInvoiceIssuanceResponse
import io.portone.sdk.server.b2b.taxinvoice.CancelB2bTaxInvoiceRequestBody
import io.portone.sdk.server.b2b.taxinvoice.CancelB2bTaxInvoiceRequestResponse
import io.portone.sdk.server.b2b.taxinvoice.CreateB2bFileUploadUrlBody
import io.portone.sdk.server.b2b.taxinvoice.CreateB2bFileUploadUrlPayload
import io.portone.sdk.server.b2b.taxinvoice.DeleteB2bTaxInvoiceResponse
import io.portone.sdk.server.b2b.taxinvoice.DraftB2bTaxInvoiceBody
import io.portone.sdk.server.b2b.taxinvoice.DraftB2bTaxInvoiceResponse
import io.portone.sdk.server.b2b.taxinvoice.GetB2bTaxInvoiceAttachmentsResponse
import io.portone.sdk.server.b2b.taxinvoice.GetB2bTaxInvoicePdfDownloadUrlResponse
import io.portone.sdk.server.b2b.taxinvoice.GetB2bTaxInvoicePopupUrlResponse
import io.portone.sdk.server.b2b.taxinvoice.GetB2bTaxInvoicePrintUrlResponse
import io.portone.sdk.server.b2b.taxinvoice.GetB2bTaxInvoicesBody
import io.portone.sdk.server.b2b.taxinvoice.GetB2bTaxInvoicesBodyFilter
import io.portone.sdk.server.b2b.taxinvoice.GetB2bTaxInvoicesResponse
import io.portone.sdk.server.b2b.taxinvoice.IssueB2bTaxInvoiceBody
import io.portone.sdk.server.b2b.taxinvoice.IssueB2bTaxInvoiceResponse
import io.portone.sdk.server.b2b.taxinvoice.RefuseB2bTaxInvoiceRequestBody
import io.portone.sdk.server.b2b.taxinvoice.RefuseB2bTaxInvoiceRequestResponse
import io.portone.sdk.server.b2b.taxinvoice.RequestB2bTaxInvoiceResponse
import io.portone.sdk.server.b2b.taxinvoice.RequestB2bTaxInvoiceReverseIssuanceBody
import io.portone.sdk.server.b2b.taxinvoice.RequestB2bTaxInvoiceReverseIssuanceResponse
import io.portone.sdk.server.b2b.taxinvoice.SendToNtsB2bTaxInvoiceResponse
import io.portone.sdk.server.b2b.taxinvoice.UpdateB2bTaxInvoiceDraftBody
import io.portone.sdk.server.b2b.taxinvoice.UpdateB2bTaxInvoiceDraftResponse
import io.portone.sdk.server.errors.AttachB2bTaxInvoiceFileError
import io.portone.sdk.server.errors.B2BCannotChangeTaxTypeError
import io.portone.sdk.server.errors.B2BCannotChangeTaxTypeException
import io.portone.sdk.server.errors.B2BTaxInvoiceStatusNotSendingCompletedError
import io.portone.sdk.server.errors.B2BTaxInvoiceStatusNotSendingCompletedException
import io.portone.sdk.server.errors.B2bExternalServiceError
import io.portone.sdk.server.errors.B2bExternalServiceException
import io.portone.sdk.server.errors.B2bFileNotFoundError
import io.portone.sdk.server.errors.B2bFileNotFoundException
import io.portone.sdk.server.errors.B2bIdAlreadyExistsError
import io.portone.sdk.server.errors.B2bIdAlreadyExistsException
import io.portone.sdk.server.errors.B2bModificationNotProvidedError
import io.portone.sdk.server.errors.B2bModificationNotProvidedException
import io.portone.sdk.server.errors.B2bNotEnabledError
import io.portone.sdk.server.errors.B2bNotEnabledException
import io.portone.sdk.server.errors.B2bOriginalTaxInvoiceNotFoundError
import io.portone.sdk.server.errors.B2bOriginalTaxInvoiceNotFoundException
import io.portone.sdk.server.errors.B2bRecipientNotFoundError
import io.portone.sdk.server.errors.B2bRecipientNotFoundException
import io.portone.sdk.server.errors.B2bSupplierNotFoundError
import io.portone.sdk.server.errors.B2bSupplierNotFoundException
import io.portone.sdk.server.errors.B2bTaxInvoiceAttachmentNotFoundError
import io.portone.sdk.server.errors.B2bTaxInvoiceAttachmentNotFoundException
import io.portone.sdk.server.errors.B2bTaxInvoiceNoRecipientDocumentKeyError
import io.portone.sdk.server.errors.B2bTaxInvoiceNoRecipientDocumentKeyException
import io.portone.sdk.server.errors.B2bTaxInvoiceNoSupplierDocumentKeyError
import io.portone.sdk.server.errors.B2bTaxInvoiceNoSupplierDocumentKeyException
import io.portone.sdk.server.errors.B2bTaxInvoiceNonDeletableStatusError
import io.portone.sdk.server.errors.B2bTaxInvoiceNonDeletableStatusException
import io.portone.sdk.server.errors.B2bTaxInvoiceNotDraftedStatusError
import io.portone.sdk.server.errors.B2bTaxInvoiceNotDraftedStatusException
import io.portone.sdk.server.errors.B2bTaxInvoiceNotFoundError
import io.portone.sdk.server.errors.B2bTaxInvoiceNotFoundException
import io.portone.sdk.server.errors.B2bTaxInvoiceNotIssuedStatusError
import io.portone.sdk.server.errors.B2bTaxInvoiceNotIssuedStatusException
import io.portone.sdk.server.errors.B2bTaxInvoiceNotRequestedStatusError
import io.portone.sdk.server.errors.B2bTaxInvoiceNotRequestedStatusException
import io.portone.sdk.server.errors.B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError
import io.portone.sdk.server.errors.B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedException
import io.portone.sdk.server.errors.B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError
import io.portone.sdk.server.errors.B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedException
import io.portone.sdk.server.errors.CancelB2bTaxInvoiceIssuanceError
import io.portone.sdk.server.errors.CancelB2bTaxInvoiceRequestError
import io.portone.sdk.server.errors.CreateB2bFileUploadUrlError
import io.portone.sdk.server.errors.DeleteB2bTaxInvoiceAttachmentError
import io.portone.sdk.server.errors.DeleteB2bTaxInvoiceError
import io.portone.sdk.server.errors.DraftB2bTaxInvoiceError
import io.portone.sdk.server.errors.ForbiddenError
import io.portone.sdk.server.errors.ForbiddenException
import io.portone.sdk.server.errors.GetB2bTaxInvoiceAttachmentsError
import io.portone.sdk.server.errors.GetB2bTaxInvoiceError
import io.portone.sdk.server.errors.GetB2bTaxInvoicePdfDownloadUrlError
import io.portone.sdk.server.errors.GetB2bTaxInvoicePopupUrlError
import io.portone.sdk.server.errors.GetB2bTaxInvoicePrintUrlError
import io.portone.sdk.server.errors.GetB2bTaxInvoicesError
import io.portone.sdk.server.errors.InvalidRequestError
import io.portone.sdk.server.errors.InvalidRequestException
import io.portone.sdk.server.errors.IssueB2bTaxInvoiceError
import io.portone.sdk.server.errors.RefuseB2bTaxInvoiceRequestError
import io.portone.sdk.server.errors.RequestB2bTaxInvoiceReverseIssuanceError
import io.portone.sdk.server.errors.SendToNtsB2bTaxInvoiceError
import io.portone.sdk.server.errors.UnauthorizedError
import io.portone.sdk.server.errors.UnauthorizedException
import io.portone.sdk.server.errors.UnknownException
import io.portone.sdk.server.errors.UpdateB2bTaxInvoiceDraftError
import io.portone.sdk.server.errors.requestB2bTaxInvoiceError
import java.io.Closeable
import java.util.concurrent.CompletableFuture
import kotlin.String
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.future.future
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json

public class TaxInvoiceClient internal constructor(
  private val apiSecret: String,
  private val apiBase: String,
  private val storeId: String?,
) {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }

  /**
   * 세금계산서 역발행 즉시 요청
   *
   * 공급자에게 세금계산서 역발행을 즉시 요청합니다. 임시저장 API와 역발행 요청 API 기능을 한 번의 프로세스로 처리합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param taxInvoice
   * 세금계산서 생성 요청 정보
   * @param memo
   * 메모
   * @param modification
   * 수정 세금계산서 입력 정보
   *
   * @throws B2BCannotChangeTaxTypeException 세금계산서 과세 유형을 수정할 수 없는 경우
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bIdAlreadyExistsException ID가 이미 사용중인 경우
   * @throws B2bModificationNotProvidedException 세금계산서 수정 입력 정보를 찾을 수 없는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bOriginalTaxInvoiceNotFoundException 원본 세금계산서가 존재하지 않은 경우
   * @throws B2bRecipientNotFoundException 공급받는자가 존재하지 않은 경우
   * @throws B2bSupplierNotFoundException 공급자가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedException 세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
   * @throws B2BTaxInvoiceStatusNotSendingCompletedException 원본 세금계산서가 전송완료 상태가 아닌 경우
   * @throws B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedException 세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("requestB2bTaxInvoiceReverseIssuanceSuspend")
  public suspend fun requestB2bTaxInvoiceReverseIssuance(
    test: Boolean? = null,
    taxInvoice: B2bTaxInvoiceInput,
    memo: String? = null,
    modification: B2bTaxInvoiceModificationCreateBody? = null,
  ): RequestB2bTaxInvoiceReverseIssuanceResponse {
    val requestBody = RequestB2bTaxInvoiceReverseIssuanceBody(
      taxInvoice = taxInvoice,
      memo = memo,
      modification = modification,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", "request-reverse-issuance")
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
        json.decodeFromString<RequestB2bTaxInvoiceReverseIssuanceError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2BCannotChangeTaxTypeError -> throw B2BCannotChangeTaxTypeException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bIdAlreadyExistsError -> throw B2bIdAlreadyExistsException(httpBodyDecoded)
        is B2bModificationNotProvidedError -> throw B2bModificationNotProvidedException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bOriginalTaxInvoiceNotFoundError -> throw B2bOriginalTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bRecipientNotFoundError -> throw B2bRecipientNotFoundException(httpBodyDecoded)
        is B2bSupplierNotFoundError -> throw B2bSupplierNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError -> throw B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedException(httpBodyDecoded)
        is B2BTaxInvoiceStatusNotSendingCompletedError -> throw B2BTaxInvoiceStatusNotSendingCompletedException(httpBodyDecoded)
        is B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError -> throw B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<RequestB2bTaxInvoiceReverseIssuanceResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("requestB2bTaxInvoiceReverseIssuance")
  public suspend fun requestB2bTaxInvoiceReverseIssuanceFuture(
    test: Boolean? = null,
    taxInvoice: B2bTaxInvoiceInput,
    memo: String? = null,
    modification: B2bTaxInvoiceModificationCreateBody? = null,
  ): CompletableFuture<RequestB2bTaxInvoiceReverseIssuanceResponse> = GlobalScope.future { requestB2bTaxInvoiceReverseIssuance(test, taxInvoice, memo, modification) }


  /**
   * 세금 계산서 조회
   *
   * 등록된 세금 계산서를 세금계산서 아이디로 조회합니다.
   *
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bTaxInvoiceSuspend")
  public suspend fun getB2bTaxInvoice(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): B2bTaxInvoice {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", taxInvoiceKey.toString())
        if (brn != null) parameters.append("brn", brn.toString())
        if (taxInvoiceKeyType != null) parameters.append("taxInvoiceKeyType", taxInvoiceKeyType.toString())
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
        json.decodeFromString<GetB2bTaxInvoiceError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<B2bTaxInvoice>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bTaxInvoice")
  public suspend fun getB2bTaxInvoiceFuture(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): CompletableFuture<B2bTaxInvoice> = GlobalScope.future { getB2bTaxInvoice(taxInvoiceKey, brn, taxInvoiceKeyType, test) }


  /**
   * 세금계산서 삭제
   *
   * 세금계산서를 삭제합니다.
   *
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNonDeletableStatusException 세금계산서가 삭제 가능한 상태가 아닌 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("deleteB2bTaxInvoiceSuspend")
  public suspend fun deleteB2bTaxInvoice(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): DeleteB2bTaxInvoiceResponse {
    val httpResponse = client.delete(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", taxInvoiceKey.toString())
        if (brn != null) parameters.append("brn", brn.toString())
        if (taxInvoiceKeyType != null) parameters.append("taxInvoiceKeyType", taxInvoiceKeyType.toString())
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
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<DeleteB2bTaxInvoiceResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("deleteB2bTaxInvoice")
  public suspend fun deleteB2bTaxInvoiceFuture(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): CompletableFuture<DeleteB2bTaxInvoiceResponse> = GlobalScope.future { deleteB2bTaxInvoice(taxInvoiceKey, brn, taxInvoiceKeyType, test) }


  /**
   * 세금계산서 발행 승인
   *
   * 역발행의 경우 역발행요청(REQUESTED) 상태, 정발행의 경우 임시저장(DRAFTED) 상태의 세금계산서에 대해 발행을 승인합니다.
   *
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param memo
   * 메모
   * @param emailSubject
   * 이메일 제목
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotRequestedStatusException 세금계산서가 역발행 대기 상태가 아닌 경우
   * @throws B2bTaxInvoiceNoSupplierDocumentKeyException 세금계산서에 공급자 문서 번호가 기입되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("issueB2bTaxInvoiceSuspend")
  public suspend fun issueB2bTaxInvoice(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
    memo: String? = null,
    emailSubject: String? = null,
  ): IssueB2bTaxInvoiceResponse {
    val requestBody = IssueB2bTaxInvoiceBody(
      memo = memo,
      emailSubject = emailSubject,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", taxInvoiceKey.toString(), "issue")
        if (brn != null) parameters.append("brn", brn.toString())
        if (taxInvoiceKeyType != null) parameters.append("taxInvoiceKeyType", taxInvoiceKeyType.toString())
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
        is B2bTaxInvoiceNoSupplierDocumentKeyError -> throw B2bTaxInvoiceNoSupplierDocumentKeyException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<IssueB2bTaxInvoiceResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("issueB2bTaxInvoice")
  public suspend fun issueB2bTaxInvoiceFuture(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
    memo: String? = null,
    emailSubject: String? = null,
  ): CompletableFuture<IssueB2bTaxInvoiceResponse> = GlobalScope.future { issueB2bTaxInvoice(taxInvoiceKey, brn, taxInvoiceKeyType, test, memo, emailSubject) }


  /**
   * 세금계산서 국세청 즉시 전송
   *
   * 발행이 완료된 세금계산서를 국세청에 즉시 전송합니다.
   *
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotIssuedStatusException 세금계산서가 발행된(ISSUED) 상태가 아닌 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("sendToNtsB2bTaxInvoiceSuspend")
  public suspend fun sendToNtsB2bTaxInvoice(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): SendToNtsB2bTaxInvoiceResponse {
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", taxInvoiceKey.toString(), "send-to-nts")
        if (brn != null) parameters.append("brn", brn.toString())
        if (taxInvoiceKeyType != null) parameters.append("taxInvoiceKeyType", taxInvoiceKeyType.toString())
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
        json.decodeFromString<SendToNtsB2bTaxInvoiceError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceNotIssuedStatusError -> throw B2bTaxInvoiceNotIssuedStatusException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<SendToNtsB2bTaxInvoiceResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("sendToNtsB2bTaxInvoice")
  public suspend fun sendToNtsB2bTaxInvoiceFuture(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): CompletableFuture<SendToNtsB2bTaxInvoiceResponse> = GlobalScope.future { sendToNtsB2bTaxInvoice(taxInvoiceKey, brn, taxInvoiceKeyType, test) }


  /**
   * 세금계산서 역발행 요청 취소 (공급받는자에 의한 취소)
   *
   * 공급자가 세금계산서 발행을 승인하기 전에 공급받는자가 해당 역발행 요청을 취소합니다.
   *
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param memo
   * 메모
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotRequestedStatusException 세금계산서가 역발행 대기 상태가 아닌 경우
   * @throws B2bTaxInvoiceNoRecipientDocumentKeyException 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("cancelB2bTaxInvoiceRequestSuspend")
  public suspend fun cancelB2bTaxInvoiceRequest(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
    memo: String? = null,
  ): CancelB2bTaxInvoiceRequestResponse {
    val requestBody = CancelB2bTaxInvoiceRequestBody(
      memo = memo,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", taxInvoiceKey.toString(), "cancel-request")
        if (brn != null) parameters.append("brn", brn.toString())
        if (taxInvoiceKeyType != null) parameters.append("taxInvoiceKeyType", taxInvoiceKeyType.toString())
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
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CancelB2bTaxInvoiceRequestResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("cancelB2bTaxInvoiceRequest")
  public suspend fun cancelB2bTaxInvoiceRequestFuture(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
    memo: String? = null,
  ): CompletableFuture<CancelB2bTaxInvoiceRequestResponse> = GlobalScope.future { cancelB2bTaxInvoiceRequest(taxInvoiceKey, brn, taxInvoiceKeyType, test, memo) }


  /**
   * 세금계산서 역발행 취소 (공급자에 의한 취소)
   *
   * 발행 완료된 세금계산서를 공급자가 국세청 전송 전에 취소합니다.
   *
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param memo
   * 메모
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotIssuedStatusException 세금계산서가 발행된(ISSUED) 상태가 아닌 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("cancelB2bTaxInvoiceIssuanceSuspend")
  public suspend fun cancelB2bTaxInvoiceIssuance(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
    memo: String? = null,
  ): CancelB2bTaxInvoiceIssuanceResponse {
    val requestBody = CancelB2bTaxInvoiceIssuanceBody(
      memo = memo,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", taxInvoiceKey.toString(), "cancel-issuance")
        if (brn != null) parameters.append("brn", brn.toString())
        if (taxInvoiceKeyType != null) parameters.append("taxInvoiceKeyType", taxInvoiceKeyType.toString())
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
        json.decodeFromString<CancelB2bTaxInvoiceIssuanceError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceNotIssuedStatusError -> throw B2bTaxInvoiceNotIssuedStatusException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<CancelB2bTaxInvoiceIssuanceResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("cancelB2bTaxInvoiceIssuance")
  public suspend fun cancelB2bTaxInvoiceIssuanceFuture(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
    memo: String? = null,
  ): CompletableFuture<CancelB2bTaxInvoiceIssuanceResponse> = GlobalScope.future { cancelB2bTaxInvoiceIssuance(taxInvoiceKey, brn, taxInvoiceKeyType, test, memo) }


  /**
   * 세금계산서 역발행 요청 거부
   *
   * 공급자가 공급받는자로부터 요청받은 세금계산서 역발행 건을 거부합니다.
   *
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param memo
   * 메모
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotRequestedStatusException 세금계산서가 역발행 대기 상태가 아닌 경우
   * @throws B2bTaxInvoiceNoSupplierDocumentKeyException 세금계산서에 공급자 문서 번호가 기입되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("refuseB2bTaxInvoiceRequestSuspend")
  public suspend fun refuseB2bTaxInvoiceRequest(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
    memo: String? = null,
  ): RefuseB2bTaxInvoiceRequestResponse {
    val requestBody = RefuseB2bTaxInvoiceRequestBody(
      memo = memo,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", taxInvoiceKey.toString(), "refuse-request")
        if (brn != null) parameters.append("brn", brn.toString())
        if (taxInvoiceKeyType != null) parameters.append("taxInvoiceKeyType", taxInvoiceKeyType.toString())
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
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<RefuseB2bTaxInvoiceRequestResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("refuseB2bTaxInvoiceRequest")
  public suspend fun refuseB2bTaxInvoiceRequestFuture(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
    memo: String? = null,
  ): CompletableFuture<RefuseB2bTaxInvoiceRequestResponse> = GlobalScope.future { refuseB2bTaxInvoiceRequest(taxInvoiceKey, brn, taxInvoiceKeyType, test, memo) }


  /**
   * 세금 계산서 다건조회
   *
   * 조회 기간 내 등록된 세금 계산서를 다건 조회합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param pageNumber
   * 페이지 번호
   *
   * 0부터 시작하는 페이지 번호. 기본 값은 0.
   * @param pageSize
   * 페이지 크기
   *
   * 각 페이지 당 포함할 객체 수. 기본 값은 500이며 최대 1000까지 요청가능합니다.
   * @param filter
   * 필터
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bTaxInvoicesSuspend")
  public suspend fun getB2bTaxInvoices(
    test: Boolean? = null,
    pageNumber: Int? = null,
    pageSize: Int? = null,
    filter: GetB2bTaxInvoicesBodyFilter? = null,
  ): GetB2bTaxInvoicesResponse {
    val requestBody = GetB2bTaxInvoicesBody(
      test = test,
      pageNumber = pageNumber,
      pageSize = pageSize,
      filter = filter,
    )
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices")
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
        json.decodeFromString<GetB2bTaxInvoicesError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bTaxInvoicesResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bTaxInvoices")
  public suspend fun getB2bTaxInvoicesFuture(
    test: Boolean? = null,
    pageNumber: Int? = null,
    pageSize: Int? = null,
    filter: GetB2bTaxInvoicesBodyFilter? = null,
  ): CompletableFuture<GetB2bTaxInvoicesResponse> = GlobalScope.future { getB2bTaxInvoices(test, pageNumber, pageSize, filter) }


  /**
   * 세금 계산서 팝업 URL 조회
   *
   * 등록된 세금 계산서 팝업 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.
   *
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bTaxInvoicePopupUrlSuspend")
  public suspend fun getB2bTaxInvoicePopupUrl(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    includeMenu: Boolean? = null,
    test: Boolean? = null,
  ): GetB2bTaxInvoicePopupUrlResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", taxInvoiceKey.toString(), "popup-url")
        if (brn != null) parameters.append("brn", brn.toString())
        if (taxInvoiceKeyType != null) parameters.append("taxInvoiceKeyType", taxInvoiceKeyType.toString())
        if (includeMenu != null) parameters.append("includeMenu", includeMenu.toString())
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
        json.decodeFromString<GetB2bTaxInvoicePopupUrlError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bTaxInvoicePopupUrlResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bTaxInvoicePopupUrl")
  public suspend fun getB2bTaxInvoicePopupUrlFuture(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    includeMenu: Boolean? = null,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bTaxInvoicePopupUrlResponse> = GlobalScope.future { getB2bTaxInvoicePopupUrl(taxInvoiceKey, brn, taxInvoiceKeyType, includeMenu, test) }


  /**
   * 세금 계산서 프린트 URL 조회
   *
   * 등록된 세금 계산서 프린트 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.
   *
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bTaxInvoicePrintUrlSuspend")
  public suspend fun getB2bTaxInvoicePrintUrl(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): GetB2bTaxInvoicePrintUrlResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", taxInvoiceKey.toString(), "print-url")
        if (brn != null) parameters.append("brn", brn.toString())
        if (taxInvoiceKeyType != null) parameters.append("taxInvoiceKeyType", taxInvoiceKeyType.toString())
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
        json.decodeFromString<GetB2bTaxInvoicePrintUrlError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bTaxInvoicePrintUrlResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bTaxInvoicePrintUrl")
  public suspend fun getB2bTaxInvoicePrintUrlFuture(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bTaxInvoicePrintUrlResponse> = GlobalScope.future { getB2bTaxInvoicePrintUrl(taxInvoiceKey, brn, taxInvoiceKeyType, test) }


  /**
   * 세금 계산서 PDF 다운로드 URL 조회
   *
   * 등록된 세금 계산서 PDF 다운로드 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.
   *
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bTaxInvoicePdfDownloadUrlSuspend")
  public suspend fun getB2bTaxInvoicePdfDownloadUrl(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): GetB2bTaxInvoicePdfDownloadUrlResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", taxInvoiceKey.toString(), "pdf-download-url")
        if (brn != null) parameters.append("brn", brn.toString())
        if (taxInvoiceKeyType != null) parameters.append("taxInvoiceKeyType", taxInvoiceKeyType.toString())
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
        json.decodeFromString<GetB2bTaxInvoicePdfDownloadUrlError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bTaxInvoicePdfDownloadUrlResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bTaxInvoicePdfDownloadUrl")
  public suspend fun getB2bTaxInvoicePdfDownloadUrlFuture(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bTaxInvoicePdfDownloadUrlResponse> = GlobalScope.future { getB2bTaxInvoicePdfDownloadUrl(taxInvoiceKey, brn, taxInvoiceKeyType, test) }


  /**
   * 세금계산서 임시저장 수정
   *
   * 임시 저장된 세금계산서를 수정합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param brn
   * 사업자등록번호
   *
   * taxInvoiceKeyType이 TAX_INVOICE_ID가 아닌 경우 필수 값입니다.
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   * @param taxInvoice
   * 세금계산서 임시저장 수정 정보
   * @param modification
   * 수정 세금계산서 입력 정보
   * @param memo
   * 메모
   *
   * @throws B2BCannotChangeTaxTypeException 세금계산서 과세 유형을 수정할 수 없는 경우
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bIdAlreadyExistsException ID가 이미 사용중인 경우
   * @throws B2bModificationNotProvidedException 세금계산서 수정 입력 정보를 찾을 수 없는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bOriginalTaxInvoiceNotFoundException 원본 세금계산서가 존재하지 않은 경우
   * @throws B2bRecipientNotFoundException 공급받는자가 존재하지 않은 경우
   * @throws B2bSupplierNotFoundException 공급자가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotDraftedStatusException 세금계산서가 임시저장 상태가 아닌 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedException 세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
   * @throws B2BTaxInvoiceStatusNotSendingCompletedException 원본 세금계산서가 전송완료 상태가 아닌 경우
   * @throws B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedException 세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("updateB2bTaxInvoiceDraftSuspend")
  public suspend fun updateB2bTaxInvoiceDraft(
    test: Boolean? = null,
    brn: String? = null,
    taxInvoiceKey: String,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    taxInvoice: B2bTaxInvoiceInput,
    modification: B2bTaxInvoiceModificationUpdateBody? = null,
    memo: String? = null,
  ): UpdateB2bTaxInvoiceDraftResponse {
    val requestBody = UpdateB2bTaxInvoiceDraftBody(
      brn = brn,
      taxInvoiceKey = taxInvoiceKey,
      taxInvoiceKeyType = taxInvoiceKeyType,
      taxInvoice = taxInvoice,
      modification = modification,
      memo = memo,
    )
    val httpResponse = client.put(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", "draft")
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
        json.decodeFromString<UpdateB2bTaxInvoiceDraftError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2BCannotChangeTaxTypeError -> throw B2BCannotChangeTaxTypeException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bIdAlreadyExistsError -> throw B2bIdAlreadyExistsException(httpBodyDecoded)
        is B2bModificationNotProvidedError -> throw B2bModificationNotProvidedException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bOriginalTaxInvoiceNotFoundError -> throw B2bOriginalTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bRecipientNotFoundError -> throw B2bRecipientNotFoundException(httpBodyDecoded)
        is B2bSupplierNotFoundError -> throw B2bSupplierNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceNotDraftedStatusError -> throw B2bTaxInvoiceNotDraftedStatusException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError -> throw B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedException(httpBodyDecoded)
        is B2BTaxInvoiceStatusNotSendingCompletedError -> throw B2BTaxInvoiceStatusNotSendingCompletedException(httpBodyDecoded)
        is B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError -> throw B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<UpdateB2bTaxInvoiceDraftResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("updateB2bTaxInvoiceDraft")
  public suspend fun updateB2bTaxInvoiceDraftFuture(
    test: Boolean? = null,
    brn: String? = null,
    taxInvoiceKey: String,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    taxInvoice: B2bTaxInvoiceInput,
    modification: B2bTaxInvoiceModificationUpdateBody? = null,
    memo: String? = null,
  ): CompletableFuture<UpdateB2bTaxInvoiceDraftResponse> = GlobalScope.future { updateB2bTaxInvoiceDraft(test, brn, taxInvoiceKey, taxInvoiceKeyType, taxInvoice, modification, memo) }


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
   * @param modification
   * 수정 세금계산서 입력 정보
   * @param memo
   * 메모
   *
   * @throws B2BCannotChangeTaxTypeException 세금계산서 과세 유형을 수정할 수 없는 경우
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bIdAlreadyExistsException ID가 이미 사용중인 경우
   * @throws B2bModificationNotProvidedException 세금계산서 수정 입력 정보를 찾을 수 없는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bOriginalTaxInvoiceNotFoundException 원본 세금계산서가 존재하지 않은 경우
   * @throws B2bRecipientNotFoundException 공급받는자가 존재하지 않은 경우
   * @throws B2bSupplierNotFoundException 공급자가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedException 세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
   * @throws B2BTaxInvoiceStatusNotSendingCompletedException 원본 세금계산서가 전송완료 상태가 아닌 경우
   * @throws B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedException 세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("draftB2bTaxInvoiceSuspend")
  public suspend fun draftB2bTaxInvoice(
    test: Boolean? = null,
    taxInvoice: B2bTaxInvoiceInput,
    modification: B2bTaxInvoiceModificationCreateBody? = null,
    memo: String? = null,
  ): DraftB2bTaxInvoiceResponse {
    val requestBody = DraftB2bTaxInvoiceBody(
      taxInvoice = taxInvoice,
      modification = modification,
      memo = memo,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", "draft")
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
        json.decodeFromString<DraftB2bTaxInvoiceError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2BCannotChangeTaxTypeError -> throw B2BCannotChangeTaxTypeException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bIdAlreadyExistsError -> throw B2bIdAlreadyExistsException(httpBodyDecoded)
        is B2bModificationNotProvidedError -> throw B2bModificationNotProvidedException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bOriginalTaxInvoiceNotFoundError -> throw B2bOriginalTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bRecipientNotFoundError -> throw B2bRecipientNotFoundException(httpBodyDecoded)
        is B2bSupplierNotFoundError -> throw B2bSupplierNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError -> throw B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedException(httpBodyDecoded)
        is B2BTaxInvoiceStatusNotSendingCompletedError -> throw B2BTaxInvoiceStatusNotSendingCompletedException(httpBodyDecoded)
        is B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError -> throw B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<DraftB2bTaxInvoiceResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("draftB2bTaxInvoice")
  public suspend fun draftB2bTaxInvoiceFuture(
    test: Boolean? = null,
    taxInvoice: B2bTaxInvoiceInput,
    modification: B2bTaxInvoiceModificationCreateBody? = null,
    memo: String? = null,
  ): CompletableFuture<DraftB2bTaxInvoiceResponse> = GlobalScope.future { draftB2bTaxInvoice(test, taxInvoice, modification, memo) }


  /**
   * 세금계산서 역발행 요청
   *
   * 임시저장(REGISTERED) 상태의 역발행 세금계산서를 공급자에게 발행 요청합니다. 요청이 완료되면 (역)발행대기 상태로 전환됩니다.
   *
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2BCannotChangeTaxTypeException 세금계산서 과세 유형을 수정할 수 없는 경우
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bModificationNotProvidedException 세금계산서 수정 입력 정보를 찾을 수 없는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bOriginalTaxInvoiceNotFoundException 원본 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNotDraftedStatusException 세금계산서가 임시저장 상태가 아닌 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws B2bTaxInvoiceNoRecipientDocumentKeyException 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
   * @throws B2BTaxInvoiceStatusNotSendingCompletedException 원본 세금계산서가 전송완료 상태가 아닌 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("requestB2bTaxInvoiceSuspend")
  public suspend fun requestB2bTaxInvoice(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): RequestB2bTaxInvoiceResponse {
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", taxInvoiceKey.toString(), "request")
        if (brn != null) parameters.append("brn", brn.toString())
        if (taxInvoiceKeyType != null) parameters.append("taxInvoiceKeyType", taxInvoiceKeyType.toString())
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
        json.decodeFromString<requestB2bTaxInvoiceError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2BCannotChangeTaxTypeError -> throw B2BCannotChangeTaxTypeException(httpBodyDecoded)
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bModificationNotProvidedError -> throw B2bModificationNotProvidedException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bOriginalTaxInvoiceNotFoundError -> throw B2bOriginalTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceNotDraftedStatusError -> throw B2bTaxInvoiceNotDraftedStatusException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is B2bTaxInvoiceNoRecipientDocumentKeyError -> throw B2bTaxInvoiceNoRecipientDocumentKeyException(httpBodyDecoded)
        is B2BTaxInvoiceStatusNotSendingCompletedError -> throw B2BTaxInvoiceStatusNotSendingCompletedException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<RequestB2bTaxInvoiceResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("requestB2bTaxInvoice")
  public suspend fun requestB2bTaxInvoiceFuture(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): CompletableFuture<RequestB2bTaxInvoiceResponse> = GlobalScope.future { requestB2bTaxInvoice(taxInvoiceKey, brn, taxInvoiceKeyType, test) }


  /**
   * 파일 업로드 URL 생성
   *
   * S3 파일 업로드를 위한 URL을 생성합니다.
   *
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param fileName
   * 파일 이름
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("createB2bFileUploadUrlSuspend")
  public suspend fun createB2bFileUploadUrl(
    test: Boolean? = null,
    fileName: String,
  ): CreateB2bFileUploadUrlPayload {
    val requestBody = CreateB2bFileUploadUrlBody(
      fileName = fileName,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("b2b", "file-upload-url")
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
        json.decodeFromString<CreateB2bFileUploadUrlError>(httpBody)
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
      json.decodeFromString<CreateB2bFileUploadUrlPayload>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("createB2bFileUploadUrl")
  public suspend fun createB2bFileUploadUrlFuture(
    test: Boolean? = null,
    fileName: String,
  ): CompletableFuture<CreateB2bFileUploadUrlPayload> = GlobalScope.future { createB2bFileUploadUrl(test, fileName) }


  /**
   * 세금계산서 파일 첨부
   *
   * 세금계산서에 파일을 첨부합니다.
   *
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   * @param fileId
   * 파일 아이디
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bFileNotFoundException 업로드한 파일을 찾을 수 없는 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotDraftedStatusException 세금계산서가 임시저장 상태가 아닌 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("attachB2bTaxInvoiceFileSuspend")
  public suspend fun attachB2bTaxInvoiceFile(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
    fileId: String,
  ) {
    val requestBody = AttachB2bTaxInvoiceFileBody(
      fileId = fileId,
    )
    val httpResponse = client.post(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", taxInvoiceKey.toString(), "attach-file")
        if (brn != null) parameters.append("brn", brn.toString())
        if (taxInvoiceKeyType != null) parameters.append("taxInvoiceKeyType", taxInvoiceKeyType.toString())
        if (test != null) parameters.append("test", test.toString())
      }
      headers {
        append(HttpHeaders.Authorization, "PortOne $apiSecret")
      }
      contentType(ContentType.Application.Json)
      userAgent(USER_AGENT)
      setBody(json.encodeToString(requestBody))
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
        is B2bTaxInvoiceNotDraftedStatusError -> throw B2bTaxInvoiceNotDraftedStatusException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
  }

  /** @suppress */
  @JvmName("attachB2bTaxInvoiceFile")
  public suspend fun attachB2bTaxInvoiceFileFuture(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
    fileId: String,
  ): CompletableFuture<Unit> = GlobalScope.future { attachB2bTaxInvoiceFile(taxInvoiceKey, brn, taxInvoiceKeyType, test, fileId) }


  /**
   * 세금계산서 첨부파일 목록 조회
   *
   * 세금계산서에 첨부된 파일 목록을 조회합니다.
   *
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param brn
   * 사업자등록번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("getB2bTaxInvoiceAttachmentsSuspend")
  public suspend fun getB2bTaxInvoiceAttachments(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): GetB2bTaxInvoiceAttachmentsResponse {
    val httpResponse = client.get(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", taxInvoiceKey.toString(), "attachments")
        if (brn != null) parameters.append("brn", brn.toString())
        if (taxInvoiceKeyType != null) parameters.append("taxInvoiceKeyType", taxInvoiceKeyType.toString())
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
        json.decodeFromString<GetB2bTaxInvoiceAttachmentsError>(httpBody)
      }
      catch (_: Exception) {
        throw UnknownException("Unknown API error: $httpBody")
      }
      when (httpBodyDecoded) {
        is B2bExternalServiceError -> throw B2bExternalServiceException(httpBodyDecoded)
        is B2bNotEnabledError -> throw B2bNotEnabledException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
    val httpBody = httpResponse.body<String>()
    return try {
      json.decodeFromString<GetB2bTaxInvoiceAttachmentsResponse>(httpBody)
    }
    catch (_: Exception) {
      throw UnknownException("Unknown API response: $httpBody")
    }
  }

  /** @suppress */
  @JvmName("getB2bTaxInvoiceAttachments")
  public suspend fun getB2bTaxInvoiceAttachmentsFuture(
    taxInvoiceKey: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): CompletableFuture<GetB2bTaxInvoiceAttachmentsResponse> = GlobalScope.future { getB2bTaxInvoiceAttachments(taxInvoiceKey, brn, taxInvoiceKeyType, test) }


  /**
   * 세금계산서 첨부파일 삭제
   *
   * 세금계산서 첨부파일을 삭제합니다.
   *
   * @param taxInvoiceKey
   * 세금계산서 문서 번호
   * @param attachmentId
   * 첨부파일 아이디
   * @param brn
   * 사업자등록번호
   * @param taxInvoiceKeyType
   * 문서 번호 유형
   *
   * query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
   * @param test
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   *
   * @throws B2bExternalServiceException 외부 서비스에서 에러가 발생한 경우
   * @throws B2bNotEnabledException B2B 기능이 활성화되지 않은 경우
   * @throws B2bTaxInvoiceAttachmentNotFoundException 세금계산서의 첨부파일을 찾을 수 없는 경우
   * @throws B2bTaxInvoiceNotDraftedStatusException 세금계산서가 임시저장 상태가 아닌 경우
   * @throws B2bTaxInvoiceNotFoundException 세금계산서가 존재하지 않은 경우
   * @throws ForbiddenException 요청이 거절된 경우
   * @throws InvalidRequestException 요청된 입력 정보가 유효하지 않은 경우
   * @throws UnauthorizedException 인증 정보가 올바르지 않은 경우
   * @throws UnknownException API 응답이 알 수 없는 형식인 경우
   */
  @JvmName("deleteB2bTaxInvoiceAttachmentSuspend")
  public suspend fun deleteB2bTaxInvoiceAttachment(
    taxInvoiceKey: String,
    attachmentId: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ) {
    val httpResponse = client.delete(apiBase) {
      url {
        appendPathSegments("b2b", "tax-invoices", taxInvoiceKey.toString(), "attachments", attachmentId.toString())
        if (brn != null) parameters.append("brn", brn.toString())
        if (taxInvoiceKeyType != null) parameters.append("taxInvoiceKeyType", taxInvoiceKeyType.toString())
        if (test != null) parameters.append("test", test.toString())
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
        is B2bTaxInvoiceNotDraftedStatusError -> throw B2bTaxInvoiceNotDraftedStatusException(httpBodyDecoded)
        is B2bTaxInvoiceNotFoundError -> throw B2bTaxInvoiceNotFoundException(httpBodyDecoded)
        is ForbiddenError -> throw ForbiddenException(httpBodyDecoded)
        is InvalidRequestError -> throw InvalidRequestException(httpBodyDecoded)
        is UnauthorizedError -> throw UnauthorizedException(httpBodyDecoded)
      }
    }
  }

  /** @suppress */
  @JvmName("deleteB2bTaxInvoiceAttachment")
  public suspend fun deleteB2bTaxInvoiceAttachmentFuture(
    taxInvoiceKey: String,
    attachmentId: String,
    brn: String? = null,
    taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
    test: Boolean? = null,
  ): CompletableFuture<Unit> = GlobalScope.future { deleteB2bTaxInvoiceAttachment(taxInvoiceKey, attachmentId, brn, taxInvoiceKeyType, test) }

  internal fun close() {
    client.close()
  }
}
