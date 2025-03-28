package io.portone.sdk.server.build

import org.gradle.api.DefaultTask
import org.gradle.api.file.DirectoryProperty
import org.gradle.api.provider.Property
import org.gradle.api.tasks.Input
import org.gradle.api.tasks.OutputDirectory
import org.gradle.api.tasks.TaskAction
import java.io.File

abstract class GenerateVersionCodeTask : DefaultTask() {
    @get:Input
    abstract val version: Property<String>

    @get:OutputDirectory
    abstract val outputDirectory: DirectoryProperty

    @TaskAction
    fun generateVersionCode() {
        val outputDir = outputDirectory.get().asFile
        if (!outputDir.exists()) {
            outputDir.mkdirs()
        }
        
        val packageDir = File(outputDir, "io/portone/sdk/server")
        if (!packageDir.exists()) {
            packageDir.mkdirs()
        }
        
        val versionFile = File(packageDir, "Version.kt")
        val content = """
            package io.portone.sdk.server

            internal const val USER_AGENT = "portone-server-sdk-jvm/${version.get()}"
        """.trimIndent() + "\n"
        
        versionFile.writeText(content)
    }
}
