/** @type {import('typedoc').TypeDocOptions} */
export default {
	entryPoints: ["src/index.ts"],
	emit: "docs",
	out: "./docs",
	tsconfig: "./tsconfig.json",
	sort: ["source-order"],
};
