/** 사용자 정의 속성이 존재 하지 않는 경우 */
export type PlatformUserDefinedPropertyNotFoundError = {
	type: "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND"
	message?: string
}
