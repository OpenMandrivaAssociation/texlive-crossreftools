Name:		texlive-crossreftools
Version:	55879
Release:	1
Summary:	Expandable extraction of cleveref data
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/crossreftools
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossreftools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossreftools.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package extracts information from cross-referencing
labels, especially those from cleveref, in an expandable
manner.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/crossreftools
%doc %{_texmfdistdir}/doc/latex/crossreftools

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
