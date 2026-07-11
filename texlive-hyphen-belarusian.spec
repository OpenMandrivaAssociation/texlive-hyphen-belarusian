%global tl_name hyphen-belarusian
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Belarusian hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-belarusian
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-belarusian.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Belarusian hyphenation patterns in T2A and UTF-8 encodings

