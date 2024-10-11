package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** B2B 기능이 활성화되지 않은 경우 */
@Serializable
@SerialName("B2B_NOT_ENABLED")
public data class B2bNotEnabledError(
  override val message: String? = null,
): AttachB2bTaxInvoiceFileError,
  ): CancelB2bTaxInvoiceIssuanceError,
    ): CancelB2bTaxInvoiceRequestError,
      ): CreateB2bTaxInvoiceFileUploadLinkCreateError,
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
                                                ): UpdateB2bMemberCompanyError,
                                                  ): getB2bContactIdExistenceError,
                                                    ): requestB2bTaxInvoiceError,
