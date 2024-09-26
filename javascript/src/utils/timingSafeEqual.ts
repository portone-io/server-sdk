export function timingSafeEqual(
	a: ArrayBufferView | ArrayBufferLike | DataView,
	b: ArrayBufferView | ArrayBufferLike | DataView,
): boolean {
	if (a.byteLength !== b.byteLength) return false;

	const aDataView =
		a instanceof DataView
			? a
			: ArrayBuffer.isView(a)
				? new DataView(a.buffer, a.byteOffset, a.byteLength)
				: new DataView(a);
	const bDataView =
		b instanceof DataView
			? b
			: ArrayBuffer.isView(b)
				? new DataView(b.buffer, b.byteOffset, b.byteLength)
				: new DataView(b);

	const length = aDataView.byteLength;
	let out = 0;
	let i = -1;
	while (++i < length) {
		out |= aDataView.getUint8(i) ^ bDataView.getUint8(i);
	}

	return out === 0;
}
