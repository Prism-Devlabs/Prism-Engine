project "PrismEngine"
    kind "SharedLib"
		language "C++"
		cppdialect "C++17"
		staticruntime "off"

		targetdir ("%{wks.location}/bin/" .. outputdir .. "/%{prj.name}")
		objdir ("%{wks.location}/bin-int/" .. outputdir .. "/%{prj.name}")

		pchheader "pmpch.h"
		pchsource "src/pmpch.cpp"

		files
		{
			"src/**.h",
			"src/**.cpp"
		}

		defines
		{
			"_CRT_SECURE_NO_WARNINGS"
			-- "GLFW_INCLUDE_NONE"
		}

		includedirs
		{
			"src",
		}

		links
		{
		}

		filter "system:windows"
			systemversion "latest"

			defines
			{
				"PM_SUPPORT_DLL",
				"PM_BUILD_DLL"
			}

			links
			{
				-- "opengl32.lib"
			}

			postbuildcommands
			{
				("{COPY} %{cfg.buildtarget.relpath} \"../bin/" .. outputdir .. "/PrismEditor/\"")
			}

		filter "system:macosx"
			systemversion "10.0"

			defines
			{
				-- "SPDLOG_DISABLE_TID_CACHING",
				-- "SPDLOG_NO_TLS"
			}

			links
			{
				-- "CoreGraphics.framework",
				-- "IOKit.framework",
				-- "AppKit.framework",
				-- "Cocoa.framework",
				--  "OpenGL.framework"
			}

			postbuildcommands
			{
				("{COPY} %{cfg.buildtarget.relpath} \"../bin/" .. outputdir .. "/\"")
			}

		filter "configurations:Debug"
			defines "PM_DEBUG"
			runtime "Debug"
			symbols "on"

			links
			{
			}

		filter "configurations:Release"
			defines "PM_RELEASE"
			runtime "Release"
			optimize "on"

			links
			{
			}

		filter "configurations:Dist"
			defines "PM_DIST"
			runtime "Release"
			optimize "Full"

			links
			{
			}
