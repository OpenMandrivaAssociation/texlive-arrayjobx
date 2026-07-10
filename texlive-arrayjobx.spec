%global tl_name arrayjobx
%global tl_revision 18125

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.04
Release:	%{tl_revision}.1
Summary:	Array data structures for (La)TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/arrayjobx
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arrayjobx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arrayjobx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides array data structures in (La)TeX, in the meaning
of the classical procedural programming languages like Fortran, Ada or
C, and macros to manipulate them. Arrays can be mono or bi-dimensional.
This is useful for applications which require high level programming
techniques, like algorithmic graphics programmed in the TeX language.
The package supersedes the arrayjob package.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/arrayjobx
%dir %{_datadir}/texmf-dist/tex/generic/arrayjobx
%doc %{_datadir}/texmf-dist/doc/generic/arrayjobx/README
%doc %{_datadir}/texmf-dist/doc/generic/arrayjobx/arrayjob.pdf
%doc %{_datadir}/texmf-dist/doc/generic/arrayjobx/arrayjob.tex
%doc %{_datadir}/texmf-dist/doc/generic/arrayjobx/arrayjobx.pdf
%doc %{_datadir}/texmf-dist/doc/generic/arrayjobx/arrayjobx.tex
%{_datadir}/texmf-dist/tex/generic/arrayjobx/arrayjob.sty
%{_datadir}/texmf-dist/tex/generic/arrayjobx/arrayjobx.sty
