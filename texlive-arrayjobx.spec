Name:		texlive-arrayjobx
Version:	18125
Release:	2
Summary:	Array data structures for (La)TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/arrayjobx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arrayjobx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arrayjobx.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides array data structures in (La)TeX, in the
meaning of the classical procedural programming languages like
Fortran, Ada or C, and macros to manipulate them. Arrays can be
mono or bi-dimensional. This is useful for applications which
require high level programming techniques, like algorithmic
graphics programmed in the TeX language. The package supersedes
the arrayjob package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/arrayjobx/arrayjob.sty
%{_texmfdistdir}/tex/generic/arrayjobx/arrayjobx.sty
%doc %{_texmfdistdir}/doc/generic/arrayjobx/README
%doc %{_texmfdistdir}/doc/generic/arrayjobx/arrayjob.pdf
%doc %{_texmfdistdir}/doc/generic/arrayjobx/arrayjob.tex
%doc %{_texmfdistdir}/doc/generic/arrayjobx/arrayjobx.pdf
%doc %{_texmfdistdir}/doc/generic/arrayjobx/arrayjobx.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
