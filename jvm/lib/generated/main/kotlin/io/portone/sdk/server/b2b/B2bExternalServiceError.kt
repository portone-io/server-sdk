package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 외부 서비스에서 에러가 발생한 경우 */
@Serializable
@SerialName("B2B_EXTERNAL_SERVICE")
public data class B2bExternalServiceError(
  override val message: String,
): AttachB2bTaxInvoiceFileError,
  ): CancelB2bTaxInvoiceIssuanceError,
    ): CancelB2bTaxInvoiceRequestError,
      ): DeleteB2bTaxInvoiceAttachmentError,
        ): DeleteB2bTaxInvoiceError,
          ): GetB2bAccountHolderError,
            ): GetB2bCertificateError,
              ): GetB2bCertificateRegistrationUrlError,
                ): GetB2bCompanyStateError,
                  ): GetB2bMemberCompanyContactError,
                    ): GetB2bMemberCompanyError,
                      ): GetB2bTaxInvoiceAttachmentsError,
                        ): GetB2bTaxInvoiceError,
                          ): GetB2bTaxInvoicePdfDownloadUrlError,
                            ): GetB2bTaxInvoicePopupUrlError,
                              ): GetB2bTaxInvoicePrintUrlError,
                                ): GetB2bTaxInvoicesError,
                                  ): IssueB2bTaxInvoiceError,
                                    ): RefuseB2bTaxInvoiceRequestError,
                                      ): RegisterB2bMemberCompanyError,
                                        ): RequestB2bTaxInvoiceRegisterError,
                                          ): RequestB2bTaxInvoiceReverseIssuanceError,
                                            ): UpdateB2bMemberCompanyContactError,
                                              ): getB2bContactIdExistenceError,
                                                ): requestB2bTaxInvoiceError,
