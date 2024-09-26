import type { B2bCertificateType } from "#generated/b2b/B2bCertificateType"

export type B2bCertificate = {
	/**
	 * 등록일시
	 * (RFC 3339 date-time)
	 */
	registeredAt: string
	/**
	 * 만료일시
	 * (RFC 3339 date-time)
	 */
	expiredAt: string
	/** 발행자명 */
	issuerDn: string
	/** 본인명 */
	subjectDn: string
	/** 인증서 타입 */
	certificateType: B2bCertificateType
	/** OID */
	oid: string
	/** 등록 담당자 성명 */
	registrantContactName: string
	/** 등록 담당자 ID */
	registrantContactId: string
}
