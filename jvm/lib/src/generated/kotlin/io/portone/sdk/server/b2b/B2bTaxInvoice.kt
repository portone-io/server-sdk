package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bModification
import io.portone.sdk.server.b2b.B2bTaxInvoiceAdditionalContact
import io.portone.sdk.server.b2b.B2bTaxInvoiceCompany
import io.portone.sdk.server.b2b.B2bTaxInvoiceItem
import io.portone.sdk.server.b2b.B2bTaxInvoicePurposeType
import io.portone.sdk.server.b2b.B2bTaxType
import java.time.Instant
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("status")
public sealed interface B2bTaxInvoice {
  /** 과세 유형 */
  public val taxType: B2bTaxType
  /** 일련번호 */
  public val serialNum: String?
  /**
   * 책번호 - 권
   *
   * 입력 범위(4자리) : 0 ~ 9999
   */
  public val bookVolume: Int?
  /**
   * 책번호 - 호
   *
   * 입력 범위(4자리) : 0 ~ 9999
   */
  public val bookIssue: Int?
  /**
   * 작성일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  public val writeDate: String
  /** 영수/청구 */
  public val purposeType: B2bTaxInvoicePurposeType
  /** 공급가액 합계 */
  public val supplyCostTotalAmount: Long
  /** 세액 합계 */
  public val taxTotalAmount: Long
  /** 합계 금액 */
  public val totalAmount: Long
  /** 현금 */
  public val cashAmount: Long?
  /** 수표 */
  public val checkAmount: Long?
  /** 외상 */
  public val creditAmount: Long?
  /** 수표 */
  public val noteAmount: Long?
  /**
   * 비고
   *
   * 최대 3개
   */
  public val remarks: List<String>
  /** 공급자 문서번호 */
  public val supplierDocumentKey: String?
  /** 공급자 */
  public val supplier: B2bTaxInvoiceCompany
  /** 공급받는자 문서번호 */
  public val recipientDocumentKey: String?
  /** 공급받는자 */
  public val recipient: B2bTaxInvoiceCompany
  /** 문자 전송 여부 */
  public val sendSms: Boolean
  /** 수정 사유 기재 */
  public val modification: B2bModification?
  /**
   * 품목
   *
   * 최대 99개
   */
  public val items: List<B2bTaxInvoiceItem>
  /**
   * 추가 담당자
   *
   * 최대 3개
   */
  public val contacts: List<B2bTaxInvoiceAdditionalContact>
  /** 상태 변경 일시 */
  public val statusUpdatedAt: Instant
}
