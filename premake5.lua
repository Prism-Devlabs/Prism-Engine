include "./vendor/premake/premake_customization/solution_items.lua"
include "Dependencies.lua"

workspace "PrismEngine"
	architecture "x86_64"
    startproject "PrismEditor"

    configurations
    {
        "Debug",
        "Release",
        "Dist"
    }

	solution_items
	{
		".editorconfig"
	}

	flags
	{
		"MultiProcessorCompile"
	}

outputdir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

group "Dependencies"
	include "vendor/premake"
group ""

group "Core"
	include "PrismEngine"
group ""

group "Tools"
	include "PrismEditor"
group ""
