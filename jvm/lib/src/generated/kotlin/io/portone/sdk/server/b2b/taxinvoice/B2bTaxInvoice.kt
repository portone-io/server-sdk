package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceAdditionalContact
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceCompany
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceDocumentModificationType
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceIssuanceType
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceItem
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceModification
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoicePurposeType
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceStatus
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceTaxationType
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 */
@Serializable
public data class B2bTaxInvoice(
  /** 세금계산서 아이디 */
  val id: String,
  /** 상태 */
  val status: B2bTaxInvoiceStatus,
  /** 과세 유형 */
  val taxationType: B2bTaxInvoiceTaxationType,
  /** 문서 유형 */
  val documentModificationType: B2bTaxInvoiceDocumentModificationType,
  /** 지연 발행 여부 */
  val isDelayed: Boolean? = null,
  /** 발행 유형 */
  val issuanceType: B2bTaxInvoiceIssuanceType,
  /** 일괄 발행 아이디 */
  val bulkTaxInvoiceId: String? = null,
  /** 일련번호 */
  val serialNumber: String? = null,
  /**
   * 책번호 - 권
   *
   * 입력 범위(4자리) : 0 ~ 9999
   */
  val bookVolume: Int? = null,
  /**
   * 책번호 - 호
   *
   * 입력 범위(4자리) : 0 ~ 9999
   */
  val bookIssue: Int? = null,
  /**
   * 작성일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val writeDate: String,
  /**
   * 발행 마감일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val issuanceDueDate: String,
  /** 영수/청구 */
  val purposeType: B2bTaxInvoicePurposeType,
  /** 공급가액 합계 */
  val totalSupplyAmount: Long,
  /** 세액 합계 */
  val totalTaxAmount: Long,
  /** 합계 금액 */
  val totalAmount: Long,
  /** 현금 */
  val cashAmount: Long? = null,
  /** 수표 */
  val checkAmount: Long? = null,
  /** 외상 */
  val creditAmount: Long? = null,
  /** 어음 */
  val noteAmount: Long? = null,
  /**
   * 비고
   *
   * 최대 3개
   */
  val remarks: List<String>,
  /** 공급자 문서번호 */
  val supplierDocumentKey: String? = null,
  /** 공급자 */
  val supplier: B2bTaxInvoiceCompany,
  /** 공급받는자 문서번호 */
  val recipientDocumentKey: String? = null,
  /** 공급받는자 */
  val recipient: B2bTaxInvoiceCompany,
  /** 문자 전송 여부 */
  val sendSms: Boolean? = null,
  /** 수정 사유 기재 */
  val modification: B2bTaxInvoiceModification? = null,
  /**
   * 품목
   *
   * 최대 99개
   */
  val items: List<B2bTaxInvoiceItem>,
  /**
   * 추가 담당자
   *
   * 최대 3개
   */
  val additionalContacts: List<B2bTaxInvoiceAdditionalContact>,
  /** 메모 */
  val memo: String? = null,
  /** 임시 저장 일시 */
  val draftedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 발행 요청 일시 */
  val requestedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 발행 일시 */
  val issuedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 상태 변경 일시 */
  val statusUpdatedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 국세청 전송 일시 */
  val ntsSentAt: @Serializable(InstantSerializer::class) Instant? = null,
  /**
   * 국세청 승인번호
   *
   * 세금계산서 발행(전자서명) 시점에 자동으로 부여
   */
  val ntsApprovalNumber: String? = null,
  /** 국세청 전송 결과 */
  val ntsResult: String? = null,
  /**
   * 국세청 결과 코드
   *
   * 국세청 발급 결과 코드로 영문 3자리 + 숫자 3자리로 구성됨
   */
  val ntsResultCode: String? = null,
  /** 국세청 결과 수신 일시 */
  val ntsResultReceivedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 삭제 일시 */
  val deletedAt: @Serializable(InstantSerializer::class) Instant? = null,
)


