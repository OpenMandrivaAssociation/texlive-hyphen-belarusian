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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Belarusian hyphenation patterns in T2A and UTF-8 encodings


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-belarusian:
belarusian loadhyph-be.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-belarusian:
\addlanguage{belarusian}{loadhyph-be.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-belarusian:
['belarusian'] = {
	loader = 'loadhyph-be.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-be.pat.txt',
},
TL_HYPHEN_EOF
