# Generated by go2rpm 1.11.1
%bcond_without check
%global debug_package %{nil}

# https://github.com/rivo/uniseg
%global goipath         github.com/rivo/uniseg
Version:                0.4.7

%gometa -L -f

%global common_description %{expand:
Unicode Text Segmentation, Word Wrapping, and String Width Calculation in Go.}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           golang-github-rivo-uniseg
Release:        %autorelease
Summary:        Unicode Text Segmentation, Word Wrapping, and String Width Calculation in Go

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/uniseg %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
