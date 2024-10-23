package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceAdditionalContact
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceCompany
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceItem
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoicePurposeType
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceTaxationType
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 생성 요청 정보 */
@Serializable
public data class B2bTaxInvoiceInput(
  /** 과세 유형 */
  val taxationType: B2bTaxInvoiceTaxationType,
  /**
   * 작성일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  val writeDate: String,
  /** 영수/청구 */
  val purposeType: B2bTaxInvoicePurposeType,
  /** 공급가액 합계 */
  val totalSupplyAmount: Long,
  /** 세액 합계 */
  val totalTaxAmount: Long,
  /** 합계 금액 */
  val totalAmount: Long,
  /** 공급자 */
  val supplier: B2bTaxInvoiceCompany,
  /** 공급받는자 */
  val recipient: B2bTaxInvoiceCompany,
  /** 일련번호 */
  val serialNumber: String? = null,
  /** 권 */
  val bookVolume: Int? = null,
  /** 호 */
  val bookIssue: Int? = null,
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
  val remarks: List<String>? = null,
  /**
   * 공급자 문서번호
   *
   * 영문 대소문자, 숫자, 특수문자('-','_')만 이용 가능
   */
  val supplierDocumentKey: String? = null,
  /**
   * 공급받는자 문서번호
   *
   * 영문 대소문자, 숫자, 특수문자('-','_')만 이용 가능
   */
  val recipientDocumentKey: String? = null,
  /**
   * 문자 전송 여부
   *
   * 공급자 담당자 휴대폰번호 {supplier.contact.mobile_phone_number} 값으로 문자 전송 전송시 포인트 차감되며, 실패시 환불 처리 기본값은 false
   */
  val sendSms: Boolean? = null,
  /**
   * 품목
   *
   * 최대 99개
   */
  val items: List<B2bTaxInvoiceItem>? = null,
  /**
   * 추가 담당자
   *
   * 최대 3개
   */
  val additionalContacts: List<B2bTaxInvoiceAdditionalContact>? = null,
)
