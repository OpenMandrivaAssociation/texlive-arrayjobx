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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides array data structures in (La)TeX, in the meaning
of the classical procedural programming languages like Fortran, Ada or
C, and macros to manipulate them. Arrays can be mono or bi-dimensional.
This is useful for applications which require high level programming
techniques, like algorithmic graphics programmed in the TeX language.
The package supersedes the arrayjob package.

